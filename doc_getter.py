#!/usr/bin/env python

"""
# Summary

This script downloads the latest version of the module from the
develop branch of the ansible-dcnm repository and extract the
documentation and examples from the module.  It will then write
the documentation to the YAML_HOME directory and the examples to
the EXAMPLES_DIR directory.

## Requirements

This script MUST be run through the bash script build_docs.bash
unless the environment variables YAML_HOME and EXAMPLES_DIR are set.

## Usage

``` bash
python doc_getter.py <module_name>
```

Where <module_name> is the name of the module from which to extract
the documentation and examples.

## Example

``` bash
python doc_getter.py dcnm_fabric
```

## Environment Variables

- YAML_HOME: The directory where the documentation will be written.
- EXAMPLES_HOME: The directory where the examples will be written.
"""
import copy
import requests
from os import environ
import sys

YAML_DIR = environ.get("YAML_HOME")
EXAMPLES_DIR = environ.get("EXAMPLES_HOME")

if YAML_DIR is None:
    print("Error: YAML_HOME environment variable not set")
    exit(1)
if EXAMPLES_DIR is None:
    print("Error: EXAMPLES_HOME environment variable not set")
    exit(1)

def get_module(filename: str) -> str:
    base_url = "https://raw.githubusercontent.com/"
    base_url += "CiscoDevNet/ansible-dcnm/refs/heads/develop/plugins/modules/"

    try:
        response = requests.get(f"{base_url}{filename}")
    except requests.exceptions.RequestException as e:
        print("Error: Could not connect to the repository")
        raise SystemExit(e)
    return response.text

def get_documentation(full_content: str) -> str:
    found = False
    content = ""
    for line in full_content.split("\n"):
        if line == '"""' and found is True:
            found = False
            break
        if line == 'DOCUMENTATION = """':
            found = True
            continue
        if found is True:
            content += line + "\n"
    return content

def get_examples(full_content: str) -> str:
    found = False
    content = ""
    for line in full_content.split("\n"):
        if line == '"""' and found is True:
            found = False
            break
        if line == 'EXAMPLES = """':
            found = True
            content += "``` yaml\n"
            content += "---\n"
            continue
        if found is True:
            content += line + "\n"
    content += "```\n"
    return content

if len(sys.argv) != 2:
    print("Example usage:")
    print(f"{sys.argv[0]} dcnm_inventory")
    sys.exit(1)

module = sys.argv[1]
module_content = get_module(f"{module}.py")

documentation = get_documentation(copy.copy(module_content))
with open(f"{YAML_DIR}/{module}.yaml", "w") as f:
    f.write(documentation)

examples = get_examples(copy.copy(module_content))
with open(f"{EXAMPLES_DIR}/{module}.yaml", "w") as f:
    f.write(examples)
