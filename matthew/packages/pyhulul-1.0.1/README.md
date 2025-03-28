﻿# sss
>An API Management tool written in Python.

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/requests.svg)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/pywol.svg)
![CircleCI branch](https://img.shields.io/circleci/project/github/erberlin/pywol/master.svg)

pystob allows for API Authorization Management and allows to build REST-Based API with custom JSON syntax.
pystob can be used as a plugin for many API Repository such as [FRPC](https://github.com/seznam/fastrpc) and many others.

## Installation

```console
$ pip install pystob
```

## Usage examples
As an API Management Tool :
```console
$ pywool -u api.redacted.com -t "FRPC_BASED" -l -vv
Retrieve list from [api.redacted.com] | AUTHORIZATION: None | BASED: FRPC_TECH
$
$ pywool -u api.redacted.com -t "REST_BASED" -d "JSON" -auth <AUTH_EXAMPLE> -l -vv
Retrieve list from [api.redacted.com] | AUTHORIZATION: <AUTH_EXAMPLE> | BASED: REST_API
$
$ pywool --help
Usage: pywool -u API_URL [OPTIONS]

  API Management for the Pywool package.

  Please don't type any hypertext protocol such as "https://" or "http://" because they can 
  corrupt the results. The standard URL_TYPE is <SUBDOMAIN>.<BASE>.<DOMAIN>:<PORT>

Options:
  -u, --url URL  Please respect the standards described above
  -p, --port PORT      Target port.
  -vv, --verbose
  -t, --technology OPTIONS
  -l, --list
  -b, --build URL Please check documentation to build your own API with Pywool Tool
  -d, --data OPTIONS
  --help                   Show this message and exit.
```
## Why create API Builder and Manager ?
I needed one and this was an opportunity to learn some stuff.

## Meta

 Kevin Jonsson- jonsson.dev@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.
