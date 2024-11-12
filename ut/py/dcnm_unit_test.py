#!/usr/bin/python
# Some comments and license info.
from __future__ import absolute_import, division, print_function
__metaclass__ = type
__copyright__ = "Copyright (c) 2024 Cisco and/or its affiliates."
__author__ = "Allen Robel"

DOCUMENTATION = """
---
module: dcnm_unit_test
short_description: Test documentation.
version_added: "3.5.0"
author: Allen Robel (@quantumonion)
description: This module is used to test the documentation generation process.
    - It contains special-case bits of YAML that are encountered in the ansible-dcnm docs.
    - If we can convert this to Markdown, we should be able to convert the rest of the docs.
options:
    state:
        choices:
        - deleted
        - merged
        - query
        - replaced
        default: merged
        description:
            - The state of the feature or object after module completion
        type: str
    config:
        description:
            - A list of fabric configuration dictionaries
        type: list
        elements: dict
        default: []
        suboptions:
            description:
                description:
                    This is the first challenging bit of YAML.
                    We have to perform some special handling if the key name is `descr`.
                type: str
                required: true
            type:
                description:
                    -   This is the second challenging bit of YAML.
                    -   We have to perform some special handling if the key name is
                        `type`.
                type: str
                required: false
                default: water
                choices:
                - water
                - fire
                - earth
                - air
            option_with_suboptions:
                description: A dictionary containing suboptions.
                    - Verifies that we can handle nested dictionaries.
                type: dict
                suboptions:
                    suboption1:
                        description: A suboption of the suboption.
                        type: str
                        required: true
                    suboption2:
                        description: Another suboption of the suboption.
                        type: str
                        required: false
                        default: "default value"
"""

EXAMPLES = """
# This is an example for merged state.
- name: merged-state example
    dcnm_unit_test:
        state: merged
        config:
        - description: "This is a test."
            type: water
            option_with_suboptions:
                suboption1: "value"
                suboption2: "value2"

# This is an example for replaced state.
- name: replaced-state example
    dcnm_unit_test:
        state: replaced
        config:
        - description: "This is a test."
            type: fire
            option_with_suboptions:
                suboption1: "value"
                suboption2: "value2"

# This is an example for deleted state.
- name: deleted-state example
    dcnm_unit_test:
        state: deleted
        config:
        - description: "This is a test."
            type: earth
            option_with_suboptions:
                suboption1: "value"
                suboption2: "value2"

# This is an example for query state.
- name: query-state example
    dcnm_unit_test:
        state: query
        config:
        - description: "This is a test."
            type: air
            option_with_suboptions:
                suboption1: "value"
                suboption2: "value2"
"""

RETURN = """
response:
    description:
    - Success or Error Data retrieved from DCNM
    returned: always
    type: list
    elements: dict
"""

class Bar:
    def __init__(self):
        pass
    def foo(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()
