#!/usr/bin/env python

"""
# Summary

This script downloads the latest version of the module from the
develop branch of the ansible-dcnm repository and extract the
documentation and examples from the module.  It will then write
the documentation to the DOCS_YAML_DIR directory and the examples to
the EXAMPLES_DIR directory.

## Requirements

This script MUST be run through the bash script build_docs.bash
unless the environment variables DOCS_YAML_DIR and EXAMPLES_DIR are set.

## Usage

``` bash
python doc_getter.py --module <module_name>
```

Where <module_name> is the name of the module from which to extract
the documentation and examples.

## Example

``` bash
python doc_getter.py --module dcnm_fabric
```

## Usage for unit tests

If the --unit-test flag is set, the script will read from the
$REPO_HOME/ut/py directory rather than pulling the module from
the ansible-dcnm repository.

``` bash
python doc_getter.py --module dcnm_fabric --unit-test
```

## Environment Variables

- DOCS_YAML_DIR: The directory where the documentation will be written.
- EXAMPLES_HOME: The directory where the examples will be written.
"""
import argparse
import copy
import requests
from os import environ
import sys

def setup_parser() -> argparse.Namespace:
    """
    ### Summary

    Setup script-specific parser

    Returns:
        argparse.Namespace
    """
    help_module = "Name of the module from which to extract documentation. "
    help_module += "Example: --module dcnm_inventory"

    help_unit_test = "If present, read from the location specified in "
    help_unit_test += "the environment variable $MODULES_HOME "
    help_unit_test += "rather than pulling from the repository. "
    help_unit_test += "Example: --unit-test"

    parser = argparse.ArgumentParser(
        description="DESCRIPTION: Options for doc_getter.",
    )
    mandatory = parser.add_argument_group(title="MANDATORY ARGS")
    optional = parser.add_argument_group(title="OPTIONAL ARGS")

    mandatory.add_argument(
        "--module",
        type=str,
        required=True,
        dest="module",
        help=f"{help_module}",
    )
    optional.add_argument(
        "--unit-test",
        dest="unit_test",
        required=False,
        action='store_true',
        help=f"{help_unit_test}",
    )
    return parser.parse_args()


def get_module(filename: str, unit_test: bool) -> str:
    if unit_test is True:
        with open(f"{MODULES_DIR}/{filename}", "r") as f:
            return f.read()

    base_url = "https://raw.githubusercontent.com/"
    base_url += "CiscoDevNet/ansible-dcnm/refs/heads/develop/plugins/modules/"

    try:
        response = requests.get(f"{base_url}{filename}")
    except requests.exceptions.RequestException as e:
        print("Error: Could not connect to the repository")
        raise SystemExit(e)
    return response.text

def get_docs_main(full_content: str) -> str:
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

def get_docs_examples(full_content: str) -> str:
    found = False
    content = ""
    for line in full_content.split("\n"):
        if line == '"""' and found is True:
            found = False
            break
        # special-casing for dcnm_rest.py
        # TODO: Ask Mike if we can remove noqa from this file
        if line == '"""  # noqa' and found is True:
            found = False
            break
        if line == 'EXAMPLES = """':
            found = True
            content += "``` yaml\n"
            content += "---\n"
            continue
        if found is True:
            content += line + "\n"
    if content != "":
        content += "```\n"
    return content

def get_docs_return(full_content: str) -> str:
    found = False
    content = ""
    for line in full_content.split("\n"):
        if line == '"""' and found is True:
            found = False
            break
        if line == 'RETURN = """':
            found = True
            content += "``` yaml\n"
            content += "---\n"
            continue
        if found is True:
            content += line + "\n"
    if content != "":
        content += "```\n"
    return content

EXAMPLES_DIR = environ.get("DOCS_EXAMPLES_DIR")
MODULES_DIR = environ.get("DOCS_MODULES_DIR")
RETURN_DIR = environ.get("DOCS_RETURN_DIR")
YAML_DIR = environ.get("DOCS_YAML_DIR")

args = setup_parser()

if EXAMPLES_DIR is None:
    msg = "Error: DOCS_EXAMPLES_DIR environment variable must be set"
    print(msg)
    exit(1)
if MODULES_DIR is None and args.unit_test is True:
    msg = "Error: DOCS_MODULES_DIR environment variable must be set "
    msg += "if --unit-test is True"
    print(msg)
    exit(1)
if RETURN_DIR is None:
    msg = "Error: DOCS_RETURN_DIR environment variable must be set"
    print(msg)
    exit(1)
if YAML_DIR is None:
    msg = "Error: DOCS_YAML_DIR environment variable must be set"
    print(msg)
    exit(1)

module = args.module
module_content = get_module(f"{module}.py", args.unit_test)

docs_main = get_docs_main(copy.copy(module_content))
with open(f"{YAML_DIR}/{module}.yaml", "w") as f:
    f.write(docs_main)

docs_examples = get_docs_examples(copy.copy(module_content))
with open(f"{EXAMPLES_DIR}/{module}.yaml", "w") as f:
    f.write(docs_examples)

docs_return = get_docs_return(copy.copy(module_content))
if docs_return != "":
    print(f"Writing {RETURN_DIR}/{module}.yaml")
    with open(f"{RETURN_DIR}/{module}.yaml", "w") as f:
        f.write(docs_return)
