# dcnm_resource_manager

???+ "Details"

    - short_description
        - DCNM ansible module for managing resources.
    - version_added
        - 2.1.0
    - description
        - DCNM ansible module for creating, deleting and querying resources
    - author
        - Mallik Mudigonda (@mmudigon)


## options

???+ "Details"


### fabric

???+ "Details"

    - description
        - 'Name of the target fabric for resource manager operations'
    - type
        - str
    - required
        - True

### state

???+ "Details"

    - description
        - The required state of the configuration after module completion.
    - type
        - str
    - required
        - False
    - choices
        - merged
        - deleted
        - query
    - default
        - merged

### config

???+ "Details"

    - description
        - A list of dictionaries containing resources and switch information
    - type
        - list
    - elements
        - dict

#### entity_name

???+ "Details"

    - description
        - A unique name which identifies the entity to which the resourcce is allocated to. 
        - The format of this parameter depends on the scope_type. The details are provided in 
        - the EXAMPLES section
    - type
        - str
    - required
        - True

#### pool_type

???+ "Details"

    - description
        - Type of resource pool
    - type
        - str
    - required
        - True
    - choices
        - ID
        - IP
        - SUBNET

#### pool_name

???+ "Details"

    - description
        - Name of the resource pool from which the resource is allocated
    - type
        - str
    - required
        - True

#### scope_type

???+ "Details"

    - description
        - Socpe of resource allocation
    - type
        - str
    - required
        - True
    - choices
        - fabric
        - device
        - device_interface
        - device_pair
        - link

#### resource

???+ "Details"

    - description
        - Value of the resource being allocated 
        - The value will be 
        -     an integer if pool_type is ID 
        -     an IPV4/IPV6 address if pool_type is IP 
        -     an IPV4 address/net_mask or IPV6 address/net_maskif pool_type is SUBNET
    - type
        - str
    - required
        - True

#### switch

???+ "Details"

    - description
        - IP address or DNS name of the management interface of the switch to which the allocated resource is assigned to.
    - type
        - list
    - elements
        - str
    - required
        - False
