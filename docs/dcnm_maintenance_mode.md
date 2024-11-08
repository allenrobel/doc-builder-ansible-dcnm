# dcnm_maintenance_mode

???+ "Details"

    - short_description
        - Manage Maintenance Mode Configuration of NX-OS Switches.
    - version_added
        - 3.6.0
    - author
        - Allen Robel (@quantumonion)
    - description
        - Enable Maintenance or Normal Mode.


## options

???+ "Details"


### state

???+ "Details"

    - choices
        - merged
        - query
    - default
        - merged
    - description
        - The state of the feature or object after module completion
    - type
        - str

### config

???+ "Details"

    - description
        - A dictionary containing the maintenance mode configuration.
    - type
        - dict
    - required
        - True

#### deploy

???+ "Details"

    - default
        - False
    - description
        - Whether to deploy the switch configurations.
    - required
        - False
    - type
        - bool

#### wait_for_mode_change

???+ "Details"

    - default
        - False
    - description
        - If deploy is enabled, whether to wait for NDFC to push the change to the switch.  Ignored if deploy is not enabled.
    - required
        - False
    - type
        - bool

#### mode

???+ "Details"

    - choices
        - maintenance
        - normal
    - default
        - normal
    - description
        - Enable maintenance or normal mode on all switches.
    - required
        - False
    - type
        - bool

#### switches

???+ "Details"

    - description
        - A list of target switches. 
        - Per-switch options override the global options.
    - required
        - True
    - type
        - list
    - elements
        - dict

##### ip_address

???+ "Details"

    - description
        - The IP address of the switch.
    - required
        - True
    - type
        - str

##### mode

???+ "Details"

    - choices
        - maintenance
        - normal
    - default
        - normal
    - description
        - Enable maintenance or normal mode for the switch.
    - required
        - False
    - type
        - str

##### deploy

???+ "Details"

    - default
        - False
    - description
        - Whether to deploy the switch configuration.
    - required
        - False
    - type
        - bool

##### wait_for_mode_change

???+ "Details"

    - default
        - False
    - description
        - If deploy is enabled, whether to wait for NDFC to push the change to the switch. Ignored if deploy is not enabled.
    - required
        - False
    - type
        - bool
