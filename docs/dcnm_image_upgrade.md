# dcnm_image_upgrade

???+ "Details"

    - author
        - Allen Robel (@quantumonion)
    - description
        - Stage, validate, upgrade images. 
        - Attach, detach, image policies. 
        - Query device issu details.
    - short_description
        - Image management for Nexus switches
    - version_added
        - 3.5.0


## options

???+ "Details"


### config

???+ "Details"

    - description
        - A dictionary containing the image policy configuration.
    - required
        - True

#### options

???+ "Details"

    - description
        - A dictionary containing options for each of the upgrade types

##### epld

???+ "Details"

    - description
        - A dictionary containing epld upgrade options

###### golden

???+ "Details"

    - default
        - False
    - description
        - Enable (True) or disable (False) reverting to the golden EPLD image
    - required
        - False
    - type
        - bool

###### module

???+ "Details"

    - default
        - ALL
    - description
        - The switch module to upgrade 
        - Choose between ALL, or integer values
    - required
        - False
    - type
        - str
    - type
        - dict

##### nxos

???+ "Details"

    - description
        - A dictionary containing nxos upgrade options

###### bios_force

???+ "Details"

    - default
        - False
    - description
        - Force BIOS upgrade
    - required
        - False
    - type
        - bool

###### mode

???+ "Details"

    - default
        - distruptive
    - description
        - nxos upgrade mode 
        - Choose between distruptive, non_disruptive, force_non_disruptive
    - required
        - False
    - type
        - str
    - type
        - dict

##### package

???+ "Details"

    - description
        - A dictionary containing package upgrade options

###### install

???+ "Details"

    - default
        - False
    - description
        - Install the package
    - required
        - False
    - type
        - bool

###### uninstall

???+ "Details"

    - default
        - False
    - description
        - Uninstall the package
    - required
        - False
    - type
        - bool
    - type
        - dict

##### reboot

???+ "Details"

    - description
        - A dictionary containing reboot options

###### config_reload

???+ "Details"

    - default
        - False
    - description
        - Reload the configuration
    - required
        - False
    - type
        - bool

###### write_erase

???+ "Details"

    - default
        - False
    - description
        - Erase the startup configuration
    - required
        - False
    - type
        - bool
    - type
        - dict
    - type
        - dict

#### policy

???+ "Details"

    - description
        - Image policy name
    - required
        - True
    - type
        - str

#### reboot

???+ "Details"

    - default
        - False
    - description
        - Reboot the switch after upgrade
    - required
        - False
    - type
        - bool

#### stage

???+ "Details"

    - default
        - True
    - description
        - Stage (True) or unstage (False) an image policy
    - required
        - False
    - type
        - bool

#### switches

???+ "Details"

    - description
        - A list of devices to attach the image policy to.
    - elements
        - dict
    - required
        - True

##### ip_address

???+ "Details"

    - description
        - The IP address of the device to which the policy will be attached.
    - required
        - True
    - type
        - str

##### options

???+ "Details"

    - description
        - A dictionary containing options for each of the upgrade types

###### epld

???+ "Details"

    - description
        - A dictionary containing epld upgrade options

####### golden

???+ "Details"

    - default
        - False
    - description
        - Enable (True) or disable (False) reverting to the golden EPLD image
    - required
        - False
    - type
        - bool

####### module

???+ "Details"

    - default
        - ALL
    - description
        - The switch module to upgrade 
        - Choose between ALL, or integer values
    - required
        - False
    - type
        - str
    - type
        - dict

###### nxos

???+ "Details"

    - description
        - A dictionary containing nxos upgrade options

####### bios_force

???+ "Details"

    - default
        - False
    - description
        - Force BIOS upgrade
    - required
        - False
    - type
        - bool

####### mode

???+ "Details"

    - default
        - distruptive
    - description
        - nxos upgrade mode 
        - Choose between distruptive, non_disruptive, force_non_disruptive
    - required
        - False
    - type
        - str
    - type
        - dict

###### package

???+ "Details"

    - description
        - A dictionary containing package upgrade options

####### install

???+ "Details"

    - default
        - False
    - description
        - Install the package
    - required
        - False
    - type
        - bool

####### uninstall

???+ "Details"

    - default
        - False
    - description
        - Uninstall the package
    - required
        - False
    - type
        - bool
    - type
        - dict

###### reboot

???+ "Details"

    - description
        - A dictionary containing reboot options

####### config_reload

???+ "Details"

    - default
        - False
    - description
        - Reload the configuration
    - required
        - False
    - type
        - bool

####### write_erase

???+ "Details"

    - default
        - False
    - description
        - Erase the startup configuration
    - required
        - False
    - type
        - bool
    - type
        - dict
    - type
        - dict

##### policy

???+ "Details"

    - description
        - Image policy name
    - required
        - True
    - type
        - str

##### reboot

???+ "Details"

    - default
        - False
    - description
        - Reboot the switch after upgrade
    - required
        - False
    - type
        - bool

##### stage

???+ "Details"

    - default
        - True
    - description
        - Stage (True) or unstage (False) an image policy
    - required
        - False
    - type
        - bool

##### upgrade

???+ "Details"

    - description
        - A dictionary containing upgrade toggles for nxos and epld

###### epld

???+ "Details"

    - default
        - False
    - description
        - Enable (True) or disable (False) EPLD upgrade 
        - If upgrade.nxos is false, epld and packages cannot both be true 
        - If epld is true, nxos_option must be disruptive
    - required
        - False
    - type
        - bool

###### nxos

???+ "Details"

    - default
        - True
    - description
        - Enable (True) or disable (False) image upgrade
    - required
        - False
    - type
        - bool
    - type
        - dict

##### validate

???+ "Details"

    - default
        - True
    - description
        - Validate (True) or do not validate (False) the image 
        - after staging
    - required
        - False
    - type
        - bool
    - type
        - list

#### upgrade

???+ "Details"

    - description
        - A dictionary containing upgrade toggles for nxos and epld

##### epld

???+ "Details"

    - default
        - False
    - description
        - Enable (True) or disable (False) EPLD upgrade 
        - If upgrade.nxos is false, epld and packages cannot both be true 
        - If epld is true, options.nxos.mode must be set to disruptive
    - required
        - False
    - type
        - bool

##### nxos

???+ "Details"

    - default
        - True
    - description
        - Enable (True) or disable (False) image upgrade
    - required
        - False
    - type
        - bool
    - type
        - dict

#### validate

???+ "Details"

    - default
        - True
    - description
        - Validate (True) or do not validate (False) the image after staging. 
        - If True, triggers NX-OS to validate that the image is compatible with the switch platform hardware.
    - required
        - False
    - type
        - bool
    - type
        - dict

### state

???+ "Details"

    - choices
        - merged
        - deleted
        - query
    - default
        - merged
    - description
        - The state of the feature or object after module completion. 
        - I(merged), I(deleted), and I(query) states are supported.
    - type
        - str

## Examples

???+ "Details"

``` yaml
---
# This module supports the following states:

# merged:
#   Attach image policy to one or more devices.
#   Stage image on one or more devices.
#   Validate image on one or more devices.
#   Upgrade image on one or more devices.

# query:
#   Return ISSU details for one or more devices.

# deleted:
#   Delete image policy from one or more devices


# Attach image policy NR3F to two devices
# Stage and validate the image on two devices but do not upgrade
    -   name: stage/validate images
        cisco.dcnm.dcnm_image_upgrade:
            state: merged
            config:
                policy: NR3F
                stage: true
                validate: true
                upgrade:
                    nxos: false
                    epld: false
                switches:
                -   ip_address: 192.168.1.1
                -   ip_address: 192.168.1.2

# Attach image policy NR1F to device 192.168.1.1
# Attach image policy NR2F to device 192.168.1.2
# Stage the image on device 192.168.1.1, but do not upgrade
# Stage the image and upgrade device 192.168.1.2
    -   name: stage/upgrade devices
        cisco.dcnm.dcnm_image_upgrade:
            state: merged
            config:
                validate: false
                stage: false
                upgrade:
                    nxos: false
                    epld: false
                options:
                    nxos:
                        mode: disruptive
                    epld:
                        module: ALL
                        golden: false
                switches:
                    -   ip_address: 192.168.1.1
                        policy: NR1F
                        stage: true
                        validate: true
                        upgrade:
                            nxos: true
                            epld: false
                    -   ip_address: 192.168.1.2
                        policy: NR2F
                        stage: true
                        validate: true
                        upgrade:
                            nxos: true
                            epld: true
                        options:
                            nxos:
                                mode: disruptive
                            epld:
                                module: ALL
                                golden: false

# Detach image policy NR3F from two devices
    -   name: stage/upgrade devices
        cisco.dcnm.dcnm_image_upgrade:
            state: deleted
            config:
                policy: NR3F
                switches:
                -   ip_address: 192.168.1.1
                -   ip_address: 192.168.1.2

# Query ISSU details for three devices
    -   name: query switch ISSU status
        cisco.dcnm.dcnm_image_upgrade:
            state: query
            config:
                policy: KMR5
                switches:
                -   ip_address: 192.168.1.1
                    policy: OR1F
                -   ip_address: 192.168.1.2
                    policy: NR2F
                -   ip_address: 192.168.1.3 # will query policy KMR5
        register: result
    -   name: print result
        ansible.builtin.debug:
            var: result

```
