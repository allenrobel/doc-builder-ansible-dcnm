# dcnm_service_node

???+ "Details"

    - short_description
        - Create/Modify/Delete service node based on type and attached interfaces from a DCNM managed VXLAN fabric.
    - version_added
        - 1.2.0
    - description
        - "Create/Modify/Delete service node based on type and attached interfaces from a DCNM managed VXLAN fabric."
    - author
        - Karthik Babu Harichandra Babu(@kharicha)


## options

???+ "Details"


### fabric

???+ "Details"

    - description
        - Name of attached easy fabric to which service node is attached
    - type
        - str
    - required
        - True

### service_fabric

???+ "Details"

    - description
        - Name of external fabric where the service node is located
    - type
        - str
    - required
        - True

### state

???+ "Details"

    - description
        - The state of DCNM after module completion.
    - type
        - str
    - choices
        - merged
        - replaced
        - overridden
        - deleted
        - query
    - default
        - merged

### config

???+ "Details"

    - description
        - List of details of service nodes being managed. Not required for state deleted
    - type
        - list
    - elements
        - dict

#### name

???+ "Details"

    - description
        - Name of service node
    - type
        - str
    - required
        - True

#### type

???+ "Details"

    - description
        - Service node type
    - type
        - str
    - choices
        - firewall
        - load_balancer
        - virtual_network_function
    - default
        - firewall

#### form_factor

???+ "Details"

    - description
        - Name of the form factor of the service node
    - type
        - str
    - choices
        - physical
        - virtual
    - default
        - physical

#### svc_int_name

???+ "Details"

    - description
        - Name of the service interface
    - type
        - str
    - required
        - True

#### switches

???+ "Details"

    - description
        - IP address of the switch where service node will be added/deleted
    - type
        - list
    - elements
        - str
    - required
        - True

#### attach_interface

???+ "Details"

    - description
        - List of switch interfaces where the service node will be attached
    - type
        - str
    - required
        - True
