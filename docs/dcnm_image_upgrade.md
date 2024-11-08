# dcnm_image_upgrade

???+ "Details"

    - short_description
        - Image management for Nexus switches
    - version_added
        - 3.5.0
    - description
        - Stage, validate, upgrade images. 
        - Attach, detach, image policies. 
        - Query device issu details.
    - author
        - Allen Robel (@quantumonion)


## options

???+ "Details"


### state

???+ "Details"

    - description
        - The state of the feature or object after module completion. 
        - I(merged), I(deleted), and I(query) states are supported.
    - type
        - str
    - choices
        - merged
        - deleted
        - query
    - default
        - merged

### config

???+ "Details"

    - description
        - A dictionary containing the image policy configuration.
    - type
        - dict
    - required
        - True

#### policy

???+ "Details"

    - description
        - Image policy name
    - type
        - str
    - required
        - True

#### stage

???+ "Details"

    - description
        - Stage (True) or unstage (False) an image policy
    - type
        - bool
    - required
        - False
    - default
        - True

#### validate

???+ "Details"

    - description
        - Validate (True) or do not validate (False) the image after staging. 
        - If True, triggers NX-OS to validate that the image is compatible with the switch platform hardware.
    - type
        - bool
    - required
        - False
    - default
        - True

#### reboot

???+ "Details"

    - description
        - Reboot the switch after upgrade
    - type
        - bool
    - required
        - False
    - default
        - False

#### upgrade

???+ "Details"

    - description
        - A dictionary containing upgrade toggles for nxos and epld
    - type
        - dict

##### nxos

???+ "Details"

    - description
        - Enable (True) or disable (False) image upgrade
    - type
        - bool
    - required
        - False
    - default
        - True

##### epld

???+ "Details"

    - description
        - Enable (True) or disable (False) EPLD upgrade 
        - If upgrade.nxos is false, epld and packages cannot both be true 
        - If epld is true, options.nxos.mode must be set to disruptive
    - type
        - bool
    - required
        - False
    - default
        - False

#### options

???+ "Details"

    - description
        - A dictionary containing options for each of the upgrade types
    - type
        - dict

##### nxos

???+ "Details"

    - description
        - A dictionary containing nxos upgrade options
    - type
        - dict

###### mode

???+ "Details"

    - description
        - nxos upgrade mode 
        - Choose between distruptive, non_disruptive, force_non_disruptive
    - type
        - str
    - required
        - False
    - default
        - distruptive

###### bios_force

???+ "Details"

    - description
        - Force BIOS upgrade
    - type
        - bool
    - required
        - False
    - default
        - False

##### epld

???+ "Details"

    - description
        - A dictionary containing epld upgrade options
    - type
        - dict

###### module

???+ "Details"

    - description
        - The switch module to upgrade 
        - Choose between ALL, or integer values
    - type
        - str
    - required
        - False
    - default
        - ALL

###### golden

???+ "Details"

    - description
        - Enable (True) or disable (False) reverting to the golden EPLD image
    - type
        - bool
    - required
        - False
    - default
        - False

##### reboot

???+ "Details"

    - description
        - A dictionary containing reboot options
    - type
        - dict

###### config_reload

???+ "Details"

    - description
        - Reload the configuration
    - type
        - bool
    - required
        - False
    - default
        - False

###### write_erase

???+ "Details"

    - description
        - Erase the startup configuration
    - type
        - bool
    - required
        - False
    - default
        - False

##### package

???+ "Details"

    - description
        - A dictionary containing package upgrade options
    - type
        - dict

###### install

???+ "Details"

    - description
        - Install the package
    - type
        - bool
    - required
        - False
    - default
        - False

###### uninstall

???+ "Details"

    - description
        - Uninstall the package
    - type
        - bool
    - required
        - False
    - default
        - False

#### switches

???+ "Details"

    - description
        - A list of devices to attach the image policy to.
    - type
        - list
    - elements
        - dict
    - required
        - True

##### ip_address

???+ "Details"

    - description
        - The IP address of the device to which the policy will be attached.
    - type
        - str
    - required
        - True

##### policy

???+ "Details"

    - description
        - Image policy name
    - type
        - str
    - required
        - True

##### stage

???+ "Details"

    - description
        - Stage (True) or unstage (False) an image policy
    - type
        - bool
    - required
        - False
    - default
        - True

##### validate

???+ "Details"

    - description
        - Validate (True) or do not validate (False) the image 
        - after staging
    - type
        - bool
    - required
        - False
    - default
        - True

##### reboot

???+ "Details"

    - description
        - Reboot the switch after upgrade
    - type
        - bool
    - required
        - False
    - default
        - False

##### upgrade

???+ "Details"

    - description
        - A dictionary containing upgrade toggles for nxos and epld
    - type
        - dict

###### nxos

???+ "Details"

    - description
        - Enable (True) or disable (False) image upgrade
    - type
        - bool
    - required
        - False
    - default
        - True

###### epld

???+ "Details"

    - description
        - Enable (True) or disable (False) EPLD upgrade 
        - If upgrade.nxos is false, epld and packages cannot both be true 
        - If epld is true, nxos_option must be disruptive
    - type
        - bool
    - required
        - False
    - default
        - False

##### options

???+ "Details"

    - description
        - A dictionary containing options for each of the upgrade types
    - type
        - dict

###### nxos

???+ "Details"

    - description
        - A dictionary containing nxos upgrade options
    - type
        - dict

####### mode

???+ "Details"

    - description
        - nxos upgrade mode 
        - Choose between distruptive, non_disruptive, force_non_disruptive
    - type
        - str
    - required
        - False
    - default
        - distruptive

####### bios_force

???+ "Details"

    - description
        - Force BIOS upgrade
    - type
        - bool
    - required
        - False
    - default
        - False

###### epld

???+ "Details"

    - description
        - A dictionary containing epld upgrade options
    - type
        - dict

####### module

???+ "Details"

    - description
        - The switch module to upgrade 
        - Choose between ALL, or integer values
    - type
        - str
    - required
        - False
    - default
        - ALL

####### golden

???+ "Details"

    - description
        - Enable (True) or disable (False) reverting to the golden EPLD image
    - type
        - bool
    - required
        - False
    - default
        - False

###### reboot

???+ "Details"

    - description
        - A dictionary containing reboot options
    - type
        - dict

####### config_reload

???+ "Details"

    - description
        - Reload the configuration
    - type
        - bool
    - required
        - False
    - default
        - False

####### write_erase

???+ "Details"

    - description
        - Erase the startup configuration
    - type
        - bool
    - required
        - False
    - default
        - False

###### package

???+ "Details"

    - description
        - A dictionary containing package upgrade options
    - type
        - dict

####### install

???+ "Details"

    - description
        - Install the package
    - type
        - bool
    - required
        - False
    - default
        - False

####### uninstall

???+ "Details"

    - description
        - Uninstall the package
    - type
        - bool
    - required
        - False
    - default
        - False
