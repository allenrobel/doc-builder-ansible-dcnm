#!/usr/bin/env python
import copy
import re
import sys
import json
import yaml
from typing import Any, Dict, List, Union

def load_yaml(input_file: str) -> Union[str, Dict[str, Any]]:
    yaml_content = None
    try:
        with open(input_file, 'r') as f:
            yaml_content = f.read()
    except FileNotFoundError:
        return f"Error: Could not find file {input_file}"
    except Exception as e:
        return f"Error: {str(e)}"
    return yaml_content

def fix_default(content):
    """
    The default value for a list or dictionary is not quoted, so
    pyyaml interprets it as a list or dictionary.  This function
    adds quotes so that pyyaml interprets it as a string.

    default: []
    default: {}

    Becomes:

    default: "[]"
    default: "{}"
    """
    re_default_list = re.compile(r"^.*default: \[\]")
    re_default_dict = re.compile(r"^.*default: \{\}")
    new_content = ""
    for line in content.split("\n"):
        if re_default_list.match(line):
            line = re.sub(r'default: \[\]', 'default: "[]"', line)
        if re_default_dict.match(line):
            line = re.sub(r'default: \{\}', 'default: "{}"', line)
        new_content += line + "\n"
    return new_content

def fix_bootstrap_multisubnet(content):
    """
    The "#" character below is causing the Mkdocs TOC to not display the
    remaining content.  This function removes the "#" character.

    Replace the following text:
    #Scope_Start_IP
    
    With
    
    Scope_Start_IP
    """
    re_scope_start_ip = re.compile(r"^.*#Scope_Start_IP.*$")
    new_content = ""
    for line in content.split("\n"):
        if re_scope_start_ip.match(line):
            line = re.sub("#Scope_Start_IP", "Scope_Start_IP", line)
        new_content += line + "\n"
    return new_content

def fix_descriptions(content):
    """
    content is a text file with YAML content.

    This function fixes descriptions that span multiple lines.
    It removes the '-' character (if any) and concatenates the lines
    into a single line.  The '-' character is removed since later
    processing would interpret it as a list item.

    For example:

    description: |
        - This is a description
        - that spans multiple lines.
    
    Becomes:

    description: This is a description that spans multiple lines.
    """
    re_description = re.compile(r"^\s*description:")
    description = ""
    gobble = False
    new_content = ""
    for line in content.split("\n"):
        # print(f"Processing line {line}")
        # HERE
        if re_description.match(line):
            # print(f"Found description {line}")
            line = re.sub("- ", "ESC_HYPHEN", line)
            line = line.rstrip()
            description += line + " "
            gobble = True
            continue
        if not gobble:
            new_content += line + "\n"
            continue
        if ":" in line:
            gobble = False
            new_content += description + "\n"
            description = ""
            new_content += line + "\n"
            continue
        line = re.sub("- ", "ESC_HYPHEN", line)
        description += line.strip() + " "
        # print(f"Gobbled into description {description}")
    return new_content

def leading_spaces(line):
    """
    Returns the number of leading spaces in a line.
    """
    return len(line) - len(line.lstrip(' '))

def yaml2dict(yaml_string: str) -> Dict[str, Any]:
    """
    Given a string containing yaml content, return a python dictionary.
    """
    return yaml.safe_load(yaml_string)

def top_level_keys(d: Dict[str, Any]):
    """
    Process the top-level keys of the module parameters.

    1.  Print the module name as top-level heading.
    2.  Add the other top-level keys as code block
        with Material for Mkdocs TOC admonition
        ('???+ "Details"').
    3.  Escape the '-' character in the description
        so that pyyaml does not interpret is as a list.

    See also:

    -   dict2markdown which converts ESC_HYPHEN
        back to '-'.
    """
    skip_keys = ["doclevel", "options", "suboptions"]
    for key, value in d.items():
        if key in skip_keys:
            continue
        if key == "module":
            print(f"# {value}\n")
            print('???+ "Details"\n')
            continue
        if key == "description":
            print(f"    - {key}")
            for subitem in value.split("ESC_HYPHEN"):
                if subitem == "":
                    continue
                print(f"{' ' * 3}     - {subitem}")
            continue
        print(f"    - {key}")
        print(f"        - {value}")
    print("")

def dict2markdown(d: Dict[str, Any]) -> str:
    """
    Given a python dictionary containing doclevel keys,
    return markdown content.
    
    The value of doclevel is based on the depth of the dictionary relative
    to the top level dictionary.
    """
    dict_keys = ["choices", "default", "description", "elements", "required", "type"]
    #skip_keys = ["options", "suboptions"]
    skip_keys = ["suboptions"]
    def add_details():
        print("")
        print('???+ "Details"')
        print("")
    def recurse(d, level):
        for key, value in d.items():
            if isinstance(value, dict):
                doclevel = value.get('doclevel', 0)
                if key in skip_keys:
                    level -= 1
                else:
                    print("")
                    print(f"{'#' * int(doclevel)} {key}")
                    add_details()
                recurse(value, level + 1)
            if isinstance(value, list):
                item_count = 0
                for item in value:
                    if isinstance(item, dict):
                        # We're currently not hitting this code block.
                        # Consider removing it later.
                        if item in skip_keys:
                            level -= 1
                        else:
                            print("")
                            print(f"{'#' * int(doclevel)} {item}")
                            add_details()
                        recurse(item, level + 1)
                        continue
                    if item_count == 0:
                        print(f"{' ' * 3} - {key}")
                        print(f"{' ' * 3}     - {item}")
                        item_count += 1
                        continue
                    else:
                        print(f"{' ' * 3}     - {item}")
                        continue
                continue
            if key in dict_keys and level > 1:
                if not isinstance(value, (str, int, bool)):
                    continue
                print(f"{' ' * 3} - {key}")
                if key == "description":
                    for subitem in value.split("ESC_HYPHEN"):
                        if subitem == "":
                            continue
                        print(f"{' ' * 3}     - {subitem}")
                else:
                    print(f"{' ' * 3}     - {value}")
    recurse(d, 1)

def impose_heading_levels(d: Dict[str, Any]) -> Dict[str, Any]:
    """
    Given a python dictionary, add the following key to all
    dictionaries in the dictionary: doclevel.
    
    The value of doclevel is based on the depth of the dictionary
    relative to the top level dictionary.
    """
    def recurse(d, level):
        for key, value in d.items():
            if isinstance(value, dict):
                if key == "suboptions":
                    # Don't increment for suboptions key since it's not a heading.
                    # Eventually, we want to remove this key, but will work on
                    # that later.
                    level -= 1
                value['doclevel'] = level
                recurse(value, level + 1)
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        item['doclevel'] = level
                        recurse(item, level + 1)
    recurse(d, 2)
    d['doclevel'] = 1
    return d

def remove_suboptions(md: str) -> str:
    """
    Given markdown content, remove headings containing
    the string "suboptions".
    """
    new_md = ""
    for line in md.split("\n"):
        if "suboptions" in line:
            continue
        new_md += line + "\n"
    return new_md

input_file = sys.argv[1]
content = load_yaml(input_file)
content = fix_descriptions(content)
content = fix_default(content)
if input_file == "dcnm_fabric.yaml":
    content = fix_bootstrap_multisubnet(content)
content_dict = yaml2dict(content)
content_dict = impose_heading_levels(content_dict)
top_level_keys(content_dict)
dict2markdown(content_dict)
