# dcnm_inventory

???+ "Details"

    - short_description
        - Add and remove Switches from a DCNM managed VXLAN fabric.
    - version_added
        - 0.9.0
    - description
        - "Add and remove Switches from a DCNM managed VXLAN fabric."
    - author
        - Karthik Babu Harichandra Babu(@kharicha), Praveen Ramoorthy(@praveenramoorthy)


## options

???+ "Details"


### fabric

???+ "Details"

    - description
        - Name of the target fabric for Inventory operations
    - type
        - str
    - required
        - True

### state

???+ "Details"

    - description
        - The state of DCNM after module completion. 
        - I(merged) and I(query) are the only states supported for POAP. 
        - I(merged) is the only state supported for RMA.
    - type
        - str
    - choices
        - merged
        - overridden
        - deleted
        - query
    - default
        - merged

### save

???+ "Details"

    - description
        - Save/Recalculate the configuration of the fabric after the inventory is updated
    - type
        - bool
    - required
        - False
    - default
        - True

### deploy

???+ "Details"

    - description
        - Deploy the pending configuration of the fabric after inventory is updated
    - type
        - bool
    - required
        - False
    - default
        - True

### config

???+ "Details"

    - description
        - List of switches being managed. Not required for state deleted
    - type
        - list
    - elements
        - dict

#### seed_ip

???+ "Details"

    - description
        - Seed Name(support both IP address and dns_name) of the switch which needs to be added to the DCNM Fabric
    - type
        - str
    - required
        - True

#### auth_proto

???+ "Details"

    - description
        - Name of the authentication protocol to be used. 
        - For POAP and RMA configurations authentication protocol should be I(MD5).
    - choices
        - MD5
        - SHA
        - MD5_DES
        - MD5_AES
        - SHA_DES
        - SHA_AES
    - type
        - str
    - required
        - False
    - default
        - MD5

#### user_name

???+ "Details"

    - description
        - Login username to the switch. 
        - For POAP and RMA configurations username should be I(admin)
    - type
        - str
    - required
        - True

#### password

???+ "Details"

    - description
        - Login password to the switch
    - type
        - str
    - required
        - True

#### max_hops

???+ "Details"

    - description
        - Maximum Hops to reach the switch. 
        - This parameter is deprecated(as on 2024-03-06) 
        - Defaults to 0 irrespective of configured value.
    - type
        - int
    - required
        - False
    - default
        - 0

#### role

???+ "Details"

    - description
        - Role which needs to be assigned to the switch
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
    - type
        - str
    - required
        - False
    - default
        - leaf

#### preserve_config

???+ "Details"

    - description
        - Set this to false for greenfield deployment and true for brownfield deployment
    - type
        - bool
    - required
        - False
    - default
        - False

#### poap

???+ "Details"

    - description
        - Configurations of switch to Bootstrap/Pre-provision. 
        - Please note that POAP and DHCP configurations needs to enabled in fabric configuration before adding/preprovisioning switches through POAP. 
        - Idempotence checks against inventory is only for B(IP Address) for Preprovision configs. 
        - Idempotence checks against inventory is only for B(IP Address) and B(Serial Number) for Bootstrap configs.
    - type
        - list
    - elements
        - dict

##### discovery_username

???+ "Details"

    - description
        - Username for device discovery during POAP and RMA discovery
    - type
        - str
    - required
        - False

##### discovery_password

???+ "Details"

    - description
        - Password for device discovery during POAP and RMA discovery
    - type
        - str
    - required
        - False

##### serial_number

???+ "Details"

    - description
        - Serial number of switch to Bootstrap. 
        - When C(preprovision_serial) is provided along with C(serial_number), then the Preprovisioned switch(with serial number as in C(preprovision_serial)) will be swapped with a actual switch(with serial number in C(serial_number)) through bootstrap. 
        - Swap feature is supported only on NDFC and is not supported on DCNM 11.x versions.
    - type
        - str
    - required
        - False

##### preprovision_serial

???+ "Details"

    - description
        - Serial number of switch to Pre-provision. 
        - When C(preprovision_serial) is provided along with C(serial_number), then the Preprovisioned switch(with serial number as in C(preprovision_serial)) will be swapped with a actual switch(with serial number in C(serial_number)) through bootstrap. 
        - Swap feature is supported only on NDFC and is not supported on DCNM 11.x versions.
    - type
        - str
    - required
        - False

##### model

???+ "Details"

    - description
        - Model of switch to Bootstrap/Pre-provision.
    - type
        - str
    - required
        - False

##### version

???+ "Details"

    - description
        - Software version of switch to Bootstrap/Pre-provision.
    - type
        - str
    - required
        - False

##### hostname

???+ "Details"

    - description
        - Hostname of switch to Bootstrap/Pre-provision.
    - type
        - str
    - required
        - False

##### image_policy

???+ "Details"

    - description
        - Name of the image policy to be applied on switch during Bootstrap/Pre-provision.
    - type
        - str
    - required
        - False

##### config_data

???+ "Details"

    - description
        - Basic config data of switch to Bootstrap/Pre-provision. 
        - C(modulesModel) and C(gateway) are mandatory. 
        - C(modulesModel) is list of model of modules in switch to Bootstrap/Pre-provision. 
        - C(gateway) is the gateway IP with mask for the switch to Bootstrap/Pre-provision. 
        - For other supported config data please refer to NDFC/DCNM configuration guide.
    - type
        - dict
    - required
        - False

#### rma

???+ "Details"

    - description
        - RMA an existing switch with a new one 
        - Please note that the existing switch should be configured and deployed in maintenance mode 
        - Please note that the existing switch being replaced should be shutdown state or out of network
    - type
        - list
    - elements
        - dict

##### discovery_username

???+ "Details"

    - description
        - Username for device discovery during POAP and RMA discovery
    - type
        - str
    - required
        - False

##### discovery_password

???+ "Details"

    - description
        - Password for device discovery during POAP and RMA discovery
    - type
        - str
    - required
        - False

##### serial_number

???+ "Details"

    - description
        - Serial number of switch to Bootstrap for RMA.
    - type
        - str
    - required
        - True

##### old_serial

???+ "Details"

    - description
        - Serial number of switch to be replaced by RMA.
    - type
        - str
    - required
        - True

##### model

???+ "Details"

    - description
        - Model of switch to Bootstrap for RMA.
    - type
        - str
    - required
        - True

##### version

???+ "Details"

    - description
        - Software version of switch to Bootstrap for RMA.
    - type
        - str
    - required
        - True

##### image_policy

???+ "Details"

    - description
        - Name of the image policy to be applied on switch during Bootstrap for RMA.
    - type
        - str
    - required
        - False

##### config_data

???+ "Details"

    - description
        - Basic config data of switch to Bootstrap for RMA. 
        - C(modulesModel) and C(gateway) are mandatory. 
        - C(modulesModel) is list of model of modules in switch to Bootstrap for RMA. 
        - C(gateway) is the gateway IP with mask for the switch to Bootstrap for RMA. 
        - For other supported config data please refer to NDFC/DCNM configuration guide.
    - type
        - dict
    - required
        - True

### query_poap

???+ "Details"

    - description
        - Query for Bootstrap(POAP) capable switches available.
    - type
        - bool
    - required
        - False
    - default
        - False
