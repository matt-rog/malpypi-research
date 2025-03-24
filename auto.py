import pandas as pd
import subprocess
import os
import json
from openai import OpenAI
import traceback

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def unpack(path):
    if path.endswith(".gz"):
        out = path.replace(".tar.gz", "")
        if not os.path.exists(out):
            os.makedirs(out)
        ans = subprocess.call(["tar", "-xvzf", path, "-C", out])
        return path, out
    else:
        out = path.replace(".whl", "")
        if not os.path.exists(out):
            os.makedirs(out)
        ans = subprocess.call(["wheel", "unpack", path, "-d", out])
        return path, out


def main():
    xlsx = "tasks/malicious_package_dataset_preparation/supports/Randomized_Package_List.xlsx"
    sheet = "Sheet3"
    df = pd.read_excel(xlsx, sheet_name=sheet)

    malrepo_path = "tasks/malicious_package_dataset_preparation/supports/ref_malicious_packages/pypi_malregistry"
    dataset_path = "tasks/malicious_package_dataset_preparation/core/dataset_files/pypi"

    df = df.reset_index(drop=True)
    errored = {}
    c = 0
    for index, row in df.iterrows():
        if str(row["Devs"]).strip() == "Matthew" and row["Finished"] != 1:
            c += 1
            continue
            pkg_name = row["Package Name"].strip().split(" ")[-1].strip()
            print("=> Processing: ", pkg_name)

            unpack_in, unpack_out = None, None

            try:
                root_folder_path = os.path.join(malrepo_path, pkg_name)
                for potdir in os.scandir(root_folder_path):
                    if potdir.is_dir():
                        for potdir2 in os.scandir(potdir):
                            if not potdir2.is_dir():
                                unpack_in, unpack_out = unpack(potdir2.path)

                    else:
                        unpack_in, unpack_out = unpack(potdir.path)

                break

                if unpack_out is not None:  # walk through files
                    templ = {
                        "package_name": pkg_name,
                        "package_version": "package_version_val",
                        "identifier": "identifier_val",
                        "approx_date": "yyyymmdd",
                        "ecosystem": "pypi",
                        "code_ref": f"https://github.com/lxyeternal/pypi_malregistry/tree/main{unpack_in.replace(malrepo_path, '')}",
                        "prompts_and_responses": [],
                        "observation_object": {
                            "observations": [],
                            "observation_types": [],
                            "summary": "",
                        },
                    }

                    for root, dirs, files in os.walk(unpack_out):
                        for f in files:
                            if f.lower().endswith(".py"):
                                with open(os.path.join(root, f)) as fi:
                                    lines = fi.readlines()
                                    contents = "\n".join(lines)

                                # Conduct base simple prompt
                                init_prompt = (
                                    contents
                                    + "\nplease analyze the above code which is the content of a python file of a pypi package. please review the code base rigorously and provide me the code blocks & snippets along with the associated explanation that indicate that this is a malicious package."
                                )

                                response = client.responses.create(
                                    model="gpt-4o-mini-2024-07-18",
                                    input=init_prompt,
                                )

                                templ["prompts_and_responses"].append(
                                    {
                                        "platform": "chatgpt",
                                        "prompt": init_prompt,
                                        "response": response.output_text,
                                    }
                                )

                                # Conduct observation_type prompt
                                with open("system.txt") as fi:
                                    system = fi.read()

                                response = client.responses.create(
                                    model="gpt-4o",
                                    instructions=system,
                                    input=contents,
                                ).output_text

                                # clean occ json mkdn
                                response = response.replace("```json", "").replace(
                                    "```", ""
                                )

                                if response != "NULL":
                                    obs = json.loads(response)

                                    for o in obs:
                                        line_content = ""
                                        for no in o["line_no"]:
                                            line_content += lines[no]

                                        templ["observation_object"][
                                            "observations"
                                        ].append(
                                            {
                                                "observation_type": o[
                                                    "observation_type"
                                                ],
                                                "file_name": f,
                                                "line_content": line_content,
                                                "line_no": o["line_no"],
                                                "observation_details": o[
                                                    "observation_details"
                                                ],
                                            }
                                        )

                            elif "PKG-INFO" in f:
                                with open(os.path.join(root, f)) as fi:
                                    for line in fi:
                                        if line.startswith("Version:"):
                                            templ["package_version"] = line.split(
                                                "Version:"
                                            )[1].strip()

                    last = int(
                        sorted(
                            f
                            for f in os.listdir(dataset_path)
                            if os.path.isfile(os.path.join(dataset_path, f))
                        )[-1]
                        .replace(".json", "")
                        .replace("pypi_pkg_", "")
                    )
                    curr = f"pypi_pkg_{(last + 1):04d}.json"
                    with open(os.path.join(dataset_path, curr), "w") as f:
                        json.dump(templ, f, indent=4)
                    df.at[index, "Finished"] = 1
            except Exception:
                errored["pkg_name"] = traceback.format_exc()
            with open("errored.json", "w") as f:
                json.dump(errored, f, indent=4)

    df.to_excel(xlsx, sheet_name=sheet, index=False)
    print(c)


if __name__ == "__main__":
    main()
