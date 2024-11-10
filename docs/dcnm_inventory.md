# dcnm_inventory

???+ "Details"

    - author
        - Karthik Babu Harichandra Babu(@kharicha), Praveen Ramoorthy(@praveenramoorthy)
    - description
        - Add and remove Switches from a DCNM managed VXLAN fabric.
    - short_description
        - Add and remove Switches from a DCNM managed VXLAN fabric.
    - version_added
        - 0.9.0


## options

???+ "Details"


### config

???+ "Details"

    - description
        - List of switches being managed. Not required for state deleted
    - elements
        - dict

#### auth_proto

???+ "Details"

    - choices
        - MD5
        - SHA
        - MD5_DES
        - MD5_AES
        - SHA_DES
        - SHA_AES
    - default
        - MD5
    - description
        - Name of the authentication protocol to be used. 
        - For POAP and RMA configurations authentication protocol should be I(MD5).
    - required
        - False
    - type
        - str

#### max_hops

???+ "Details"

    - default
        - 0
    - description
        - Maximum Hops to reach the switch. 
        - This parameter is deprecated(as on 2024-03-06) 
        - Defaults to 0 irrespective of configured value.
    - required
        - False
    - type
        - int

#### password

???+ "Details"

    - description
        - Login password to the switch
    - required
        - True
    - type
        - str

#### poap

???+ "Details"

    - description
        - Configurations of switch to Bootstrap/Pre-provision. 
        - Please note that POAP and DHCP configurations needs to enabled in fabric configuration before adding/preprovisioning switches through POAP. 
        - Idempotence checks against inventory is only for B(IP Address) for Preprovision configs. 
        - Idempotence checks against inventory is only for B(IP Address) and B(Serial Number) for Bootstrap configs.
    - elements
        - dict

##### config_data

???+ "Details"

    - description
        - Basic config data of switch to Bootstrap/Pre-provision. 
        - C(modulesModel) and C(gateway) are mandatory. 
        - C(modulesModel) is list of model of modules in switch to Bootstrap/Pre-provision. 
        - C(gateway) is the gateway IP with mask for the switch to Bootstrap/Pre-provision. 
        - For other supported config data please refer to NDFC/DCNM configuration guide.
    - required
        - False
    - type
        - dict

##### discovery_password

???+ "Details"

    - description
        - Password for device discovery during POAP and RMA discovery
    - required
        - False
    - type
        - str

##### discovery_username

???+ "Details"

    - description
        - Username for device discovery during POAP and RMA discovery
    - required
        - False
    - type
        - str

##### hostname

???+ "Details"

    - description
        - Hostname of switch to Bootstrap/Pre-provision.
    - required
        - False
    - type
        - str

##### image_policy

???+ "Details"

    - description
        - Name of the image policy to be applied on switch during Bootstrap/Pre-provision.
    - required
        - False
    - type
        - str

##### model

???+ "Details"

    - description
        - Model of switch to Bootstrap/Pre-provision.
    - required
        - False
    - type
        - str

##### preprovision_serial

???+ "Details"

    - description
        - Serial number of switch to Pre-provision. 
        - When C(preprovision_serial) is provided along with C(serial_number), then the Preprovisioned switch(with serial number as in C(preprovision_serial)) will be swapped with a actual switch(with serial number in C(serial_number)) through bootstrap. 
        - Swap feature is supported only on NDFC and is not supported on DCNM 11.x versions.
    - required
        - False
    - type
        - str

##### serial_number

???+ "Details"

    - description
        - Serial number of switch to Bootstrap. 
        - When C(preprovision_serial) is provided along with C(serial_number), then the Preprovisioned switch(with serial number as in C(preprovision_serial)) will be swapped with a actual switch(with serial number in C(serial_number)) through bootstrap. 
        - Swap feature is supported only on NDFC and is not supported on DCNM 11.x versions.
    - required
        - False
    - type
        - str

##### version

???+ "Details"

    - description
        - Software version of switch to Bootstrap/Pre-provision.
    - required
        - False
    - type
        - str
    - type
        - list

#### preserve_config

???+ "Details"

    - default
        - False
    - description
        - Set this to false for greenfield deployment and true for brownfield deployment
    - required
        - False
    - type
        - bool

#### rma

???+ "Details"

    - description
        - RMA an existing switch with a new one 
        - Please note that the existing switch should be configured and deployed in maintenance mode 
        - Please note that the existing switch being replaced should be shutdown state or out of network
    - elements
        - dict

##### config_data

???+ "Details"

    - description
        - Basic config data of switch to Bootstrap for RMA. 
        - C(modulesModel) and C(gateway) are mandatory. 
        - C(modulesModel) is list of model of modules in switch to Bootstrap for RMA. 
        - C(gateway) is the gateway IP with mask for the switch to Bootstrap for RMA. 
        - For other supported config data please refer to NDFC/DCNM configuration guide.
    - required
        - True
    - type
        - dict

##### discovery_password

???+ "Details"

    - description
        - Password for device discovery during POAP and RMA discovery
    - required
        - False
    - type
        - str

##### discovery_username

???+ "Details"

    - description
        - Username for device discovery during POAP and RMA discovery
    - required
        - False
    - type
        - str

##### image_policy

???+ "Details"

    - description
        - Name of the image policy to be applied on switch during Bootstrap for RMA.
    - required
        - False
    - type
        - str

##### model

???+ "Details"

    - description
        - Model of switch to Bootstrap for RMA.
    - required
        - True
    - type
        - str

##### old_serial

???+ "Details"

    - description
        - Serial number of switch to be replaced by RMA.
    - required
        - True
    - type
        - str

##### serial_number

???+ "Details"

    - description
        - Serial number of switch to Bootstrap for RMA.
    - required
        - True
    - type
        - str

##### version

???+ "Details"

    - description
        - Software version of switch to Bootstrap for RMA.
    - required
        - True
    - type
        - str
    - type
        - list

#### role

???+ "Details"

    - choices
        - leaf
        - spine
        - border
        - border_spine
        - border_gateway
        - border_gateway_spine
        - super_spine
        - border_super_spine
        - border_gateway_super_spine
        - access
        - aggregation
        - edge_router
        - core_router
        - tor
    - default
        - leaf
    - description
        - Role which needs to be assigned to the switch
    - required
        - False
    - type
        - str

#### seed_ip

???+ "Details"

    - description
        - Seed Name(support both IP address and dns_name) of the switch which needs to be added to the DCNM Fabric
    - required
        - True
    - type
        - str

#### user_name

???+ "Details"

    - description
        - Login username to the switch. 
        - For POAP and RMA configurations username should be I(admin)
    - required
        - True
    - type
        - str
    - type
        - list

### deploy

???+ "Details"

    - default
        - True
    - description
        - Deploy the pending configuration of the fabric after inventory is updated
    - required
        - False
    - type
        - bool

### fabric

???+ "Details"

    - description
        - Name of the target fabric for Inventory operations
    - required
        - True
    - type
        - str

### query_poap

???+ "Details"

    - default
        - False
    - description
        - Query for Bootstrap(POAP) capable switches available.
    - required
        - False
    - type
        - bool

### save

???+ "Details"

    - default
        - True
    - description
        - Save/Recalculate the configuration of the fabric after the inventory is updated
    - required
        - False
    - type
        - bool

### state

???+ "Details"

    - choices
        - merged
        - overridden
        - deleted
        - query
    - default
        - merged
    - description
        - The state of DCNM after module completion. 
        - I(merged) and I(query) are the only states supported for POAP. 
        - I(merged) is the only state supported for RMA.
    - type
        - str

## Examples

???+ "Details"

``` yaml
---
# This module supports the following states:
#
# Merged:
#   Switches defined in the playbook will be merged into the target fabric.
#     - If the switch does not exist it will be added.
#     - Switches that are not specified in the playbook will be untouched.
#
# Overridden:
#   The playbook will serve as source of truth for the target fabric.
#     - If the switch does not exist it will be added.
#     - If the switch is not defined in the playbook but exists in DCNM it will be removed.
#     - If the switch exists, properties that need to be modified and can be modified will be modified.
#
# Deleted:
#   Deletes the list of switches specified in the playbook.
#   If no switches are provided in the playbook, all the switches present on that DCNM fabric will be deleted.
#
# Query:
#   Returns the current DCNM state for the switches listed in the playbook.


# The following two switches will be merged into the existing fabric
- name: Merge switch into fabric
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: merged # merged / deleted / overridden / query
    config:
    - seed_ip: 192.168.0.1
      auth_proto: MD5 # choose from [MD5, SHA, MD5_DES, MD5_AES, SHA_DES, SHA_AES]
      user_name: switch_username
      password: switch_password
      max_hops: 0
      role: spine
      preserve_config: False # boolean, default is  true
    - seed_ip: 192.168.0.2
      auth_proto: MD5 # choose from [MD5, SHA, MD5_DES, MD5_AES, SHA_DES, SHA_AES]
      user_name: switch_username
      password: switch_password
      max_hops: 0
      role: leaf
      preserve_config: False # boolean, default is true

# The following two switches will be added or updated in the existing fabric and all other
# switches will be removed from the fabric
- name: Override Switch
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: overridden # merged / deleted / overridden / query
    config:
    - seed_ip: 192.168.0.1
      auth_proto: MD5 # choose from [MD5, SHA, MD5_DES, MD5_AES, SHA_DES, SHA_AES]
      user_name: switch_username
      password: switch_password
      max_hops: 0
      role: spine
      preserve_config: False # boolean, default is  true
    - seed_ip: 192.168.0.2
      auth_proto: MD5 # choose from [MD5, SHA, MD5_DES, MD5_AES, SHA_DES, SHA_AES]
      user_name: switch_username
      password: switch_password
      max_hops: 0
      role: leaf
      preserve_config: False # boolean, default is true

# The following two switches will be deleted in the existing fabric
- name: Delete selected switches
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: deleted # merged / deleted / overridden / query
    config:
    - seed_ip: 192.168.0.1
    - seed_ip: 192.168.0.2

# All the switches will be deleted in the existing fabric
- name: Delete all the switches
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: deleted # merged / deleted / overridden / query

# The following two switches information will be queried in the existing fabric
- name: Query switch into fabric
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: query # merged / deleted / overridden / query
    config:
    - seed_ip: 192.168.0.1
      role: spine
    - seed_ip: 192.168.0.2
      role: leaf

# All the existing switches will be queried in the existing fabric
- name: Query all the switches in the fabric
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: query # merged / deleted / overridden / query

# The following task will enable Bootstrap and DHCP on an existing fabric.
# Please note that only bootstrap and DHCP configs are present in the below example.
# You have to add other existing fabric configs to the task.
- name: Bootstrap and DHCP Configuration
  cisco.dcnm.dcnm_rest:
    method: PUT
    path: /appcenter/cisco/ndfc/api/v1/lan-fabric/rest/control/fabrics/vxlan-fabric
    json_data: '{"fabricId": "FABRIC-7","fabricName": "vxlan-fabric","id": 7,"nvPairs":{...,"BOOTSTRAP_ENABLE": true,"DHCP_ENABLE": true,"DHCP_IPV6_ENABLE": "DHCPv4","DHCP_START": "192.168.1.10", "DHCP_END": "192.168.1.20","MGMT_GW": "192.168.123.1","MGMT_PREFIX": "24",...},"templateName": "Easy_Fabric"}' # noqa

# The following switch will be Bootstrapped and merged into the existing fabric
- name: Poap switch Configuration
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: merged # Only 2 options supported merged/query for poap config
    config:
    # All the values below are mandatory if poap configuration is being done - state is merged
    - seed_ip: 192.168.0.5
      user_name: switch_username
      password: switch_password
      role: border_gateway
      poap:
        - serial_number: 2A3BCDEFJKL
          model: 'N9K-C9300v'
          version: '9.3(7)'
          hostname: 'POAP_SWITCH'
          image_policy: "poap_image_policy"
          config_data:
            modulesModel: [N9K-X9364v, N9K-vSUP]
            gateway: 192.168.0.1/24

# The following switch will be Pre-provisioned and merged into the existing fabric
- name: Pre-provision switch Configuration
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: merged # Only 2 options supported merged/query for poap config
    config:
    # All the values below are mandatory if poap configuration is being done - state is merged
    - seed_ip: 192.168.0.4
      user_name: switch_username
      password: switch_password
      role: border
      poap:
        - preprovision_serial: 1A2BCDEFGHI
          model: 'N9K-C9300v'
          version: '9.3(7)'
          hostname: 'PREPRO_SWITCH'
          image_policy: "prepro_image_policy"
          config_data:
            modulesModel: [N9K-X9364v, N9K-vSUP]
            gateway: 192.168.0.1/24

- name: Poap, Pre-provision and existing switch Configuration
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: merged # Only 2 options supported merged/query for poap config
    config:
    - seed_ip: 192.168.0.2
      user_name: switch_username
      password: switch_password
      role: border_gateway
      poap:
        - serial_number: 2A3BCDEFGHI
          model: 'N9K-C9300v'
          version: '9.3(7)'
          hostname: 'POAP_SWITCH'
          image_policy: "poap_image_policy"
          config_data:
            modulesModel: [N9K-X9364v, N9K-vSUP]
            gateway: 192.168.0.1/24
    - seed_ip: 192.168.0.3
      user_name: switch_username
      password: switch_password
      auth_proto: MD5
      max_hops: 0
      preserve_config: False
      role: spine
    - seed_ip: 192.168.0.4
      user_name: switch_username
      password: switch_password
      role: border
      poap:
        - preprovision_serial: 1A2BCDEFGHI
          model: 'N9K-C9300v'
          version: '9.3(7)'
          hostname: 'PREPRO_SWITCH'
          image_policy: "prepro_image_policy"
          config_data:
            modulesModel: [N9K-X9364v, N9K-vSUP]
            gateway: 192.168.0.1/24

# The following pre-provisioned switch will be swapped with actual switch in the existing fabric
# No Need to provide any other parameters for swap operation as bootstrap will inherit the preprovision configs
# If other parameters are provided it will be overidden with preprovision switch configs
# This swap feature is supported only in NDFC and not on DCNM 11.x versions
- name: Pre-provision switch Configuration
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: merged # Only 2 options supported merged/query for poap config
    config:
    # All the values below are mandatory if poap configuration is being done - state is merged
    - seed_ip: 192.168.0.4
      user_name: switch_username
      password: switch_password
      role: border
      poap:
        - preprovision_serial: 1A2BCDEFGHI
          serial_number: 2A3BCDEFGHI

# All the existing switches along with available Bootstrap(POAP)
# will be queried in the existing fabric
- name: Query all the switches in the fabric
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: query # merged / query
    query_poap: True

# The following switch which is part of fabric will be replaced with a new switch
# with same configurations through RMA.
# Please note that the existing switch should be configured in maintenance mode and in shutdown state
- name: RMA switch Configuration
  cisco.dcnm.dcnm_inventory:
    fabric: vxlan-fabric
    state: merged # Only merged is supported for rma config
    config:
    - seed_ip: 192.168.0.4
      user_name: switch_username
      password: switch_password
      rma:
        - serial_number: 2A3BCDEFJKL
          old_serial: 2A3BCDEFGHI
          model: 'N9K-C9300v'
          version: '9.3(7)'
          image_policy: "rma_image_policy"
          config_data:
            modulesModel: [N9K-X9364v, N9K-vSUP]
            gateway: 192.168.0.1/24
```
