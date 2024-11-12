# dcnm_rest

???+ "Details"

    - author
        - ['Mike Wiebe (@mikewiebe)']
    - description
        - Send REST API requests to DCNM controller.
    - short_description
        - Send REST API requests to DCNM controller.
    - version_added
        - 0.9.0

    - author
        - Mike Wiebe (@mikewiebe)

## options

???+ "Details"


### data

???+ "Details"

    - aliases
        - json_data
    - description
        - Additional data in JSON or TEXT to include with the REST API call
    - required
        - False
    - type
        - raw

### method

???+ "Details"

    - choices
        - GET
        - POST
        - PUT
        - DELETE
    - description
        - REST API Method
    - required
        - True
    - type
        - str

### path

???+ "Details"

    - description
        - REST API Path Endpoint
    - required
        - True
    - type
        - str

## Examples

???+ "Details"

``` yaml
---
# This module can be used to send any REST API requests that are supported by
# the DCNM controller.
#
# This module is not idempotent but can be used as a stop gap until a feature
# module can be developed for the target DCNM functionality.

- name: Gather List of Fabrics from DCNM
  dcnm_rest:
    method: GET
    path: /rest/control/fabrics

- name: Set deployment to false in lanAttachList for vrf
  dcnm_rest:
    method: POST
    path: /rest/top-down/fabrics/fabric1/vrfs/attachments
    json_data: '[{"vrfName":"sales66_vrf1","lanAttachList":[{"fabric":"fabric1","vrfName":"sales66_vrf1","serialNumber":"FDO21392QKM","vlan":2000,"freeformConfig":"","deployment":false,"extensionValues":"","instanceValues":"{\"loopbackId\":\"\",\"loopbackIpAddress\":\"\",\"loopbackIpV6Address\":\"\"}"}]}]'

# Read payload data from file and validate a template
- set_fact:
    data: "{{ lookup('file', 'validate_payload') }}"

- name: Validate a template
  cisco.dcnm.dcnm_rest:
    method: POST
    path: /fm/fmrest/config/templates/validate
    json_data: "{{ data }}"
    register: result

```

## Return

???+ "Details"

``` yaml
---
response:
    description:
    - Success or Error Data retrieved from DCNM
    returned: always
    type: list
    elements: dict
```
