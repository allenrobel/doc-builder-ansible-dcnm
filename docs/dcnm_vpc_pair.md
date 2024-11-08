# dcnm_vpc_pair

???+ "Details"

    - short_description
        - DCNM Ansible Module for managing VPC switch pairs required for VPC interfaces.
    - version_added
        - 3.5.0
    - description
        - "DCNM Ansible Module for managing VPC switch pairs."
    - author
        - Mallik Mudigonda(@mmudigon)


## options

???+ "Details"


### src_fabric

???+ "Details"

    - description
        - Name of the target fabric for VPC switch pair operations
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
    - choices
        - merged
        - replaced
        - overridden
        - deleted
        - query
        - fetch
    - default
        - merged

### deploy

???+ "Details"

    - description
        - Flag indicating if the configuration must be pushed to the switch.
    - type
        - bool
    - default
        - True

### config

???+ "Details"

    - description
        - A list of dictionaries containing VPC switch pair information
    - type
        - list
    - elements
        - dict
    - default
        - []

#### peerOneId

???+ "Details"

    - description
        - IP Address/Host Name of Peer1 of VPC switch pair.
    - type
        - str
    - required
        - True

#### peerTwoId

???+ "Details"

    - description
        - IP Address/Host Name of Peer2 of VPC switch pair.
    - type
        - str
    - required
        - True

#### templateName

???+ "Details"

    - description
        - Name of the template which inlcudes the required parameters for creating the VPC switch pair. 
        - This parameter is 'mandatory' if the fabric is of type 'LANClassic' or 'External'. It is optional otherwise.
    - type
        - str
    - required
        - True

#### profile

???+ "Details"

    - description
        - A dictionary of additional VPC switch pair related parameters that must be included while creating VPC switch pairs.

##### ADMIN_STATE

???+ "Details"

    - description
        - Flag to enable/disbale administrative state of the interface.
    - type
        - bool
    - required
        - True

##### ALLOWED_VLANS

???+ "Details"

    - description
        - Vlans that are allowed on the VPC peer link port-channel.
    - type
        - str
    - choices
        - none
        - all
        - vlan-range(e.g., 1-2, 3-40)
    - default
        - all

##### DOMAIN_ID

???+ "Details"

    - description
        - VPC domain ID. 
        - Minimum value is 1 and Maximum value is 1000.
    - type
        - int
    - required
        - True

##### FABRIC_NAME

???+ "Details"

    - description
        - Name of the target fabric for VPC switch pair operations.
    - type
        - str
    - required
        - True

##### KEEP_ALIVE_HOLD_TIMEOUT

???+ "Details"

    - description
        - Hold timeout to ignore stale peer keep alive messages. 
        - Minimum value is 3 and Maximum value is 10
    - type
        - int
    - default
        - 3

##### KEEP_ALIVE_VRF

???+ "Details"

    - description
        - Name of the VRF used for keep-alive messages.
    - type
        - str
    - required
        - True

##### PC_MODE

???+ "Details"

    - description
        - Port channel mode.
    - type
        - str
    - choices
        - on
        - active
        - passive
    - default
        - active

##### PEER1_DOMAIN_CONF

???+ "Details"

    - description
        - Additional CLI for PEER1 vPC Domain.
    - type
        - str
    - default
        - 

##### PEER1_KEEP_ALIVE_LOCAL_IP

???+ "Details"

    - description
        - IP address of a L3 interface in non-default VRF on PEER1.
    - type
        - str
    - required
        - True

##### PEER1_MEMBER_INTERFACES

???+ "Details"

    - description
        - A list of member interfaces for PEER1.
    - type
        - list
    - elements
        - str
    - default
        - []

##### PEER1_PCID

???+ "Details"

    - description
        - PEER1 peerlink port-channel number. 
        - Minimum value is 1 and Maximum value is 4096.
    - type
        - int
    - default
        - 1

##### PEER1_PO_CONF

???+ "Details"

    - description
        - Additional CLI for PEER1 vPC peerlink port-channel.
    - type
        - str
    - default
        - 

##### PEER1_PO_DESC

???+ "Details"

    - description
        - Description for the PEER1 port-channel. 
        - Minimum length is 1 and Maximum length is 254.
    - type
        - str
    - default
        - 

##### PEER2_DOMAIN_CONF

???+ "Details"

    - description
        - Additional CLI for PEER2 vPC Domain.
    - type
        - str
    - default
        - 

##### PEER2_KEEP_ALIVE_LOCAL_IP

???+ "Details"

    - description
        - IP address of a L3 interface in non-default VRF on PEER2.
    - type
        - str
    - required
        - True

##### PEER2_MEMBER_INTERFACES

???+ "Details"

    - description
        - A list of member interfaces for PEER2.
    - type
        - list
    - elements
        - str
    - default
        - []

##### PEER2_PCID

???+ "Details"

    - description
        - PEER2 peerlink port-channel number. 
        - Minimum value is 1 and Maximum value is 4096.
    - type
        - int
    - default
        - 1

##### PEER2_PO_CONF

???+ "Details"

    - description
        - Additional CLI for PEER2 vPC peerlink port-channel.
    - type
        - str
    - default
        - 

##### PEER2_PO_DESC

???+ "Details"

    - description
        - Description for the PEER2 port-channel. 
        - Minimum length is 1 and Maximum length is 254.
    - type
        - str
    - default
        - 

### templates

???+ "Details"

    - description
        - List of templates to be fetched. 
        - This is required only if the 'state' is 'fetch'. In this case the list should contain the template names whose details. are to be fetched.
    - type
        - list
    - elements
        - str
    - default
        - []
