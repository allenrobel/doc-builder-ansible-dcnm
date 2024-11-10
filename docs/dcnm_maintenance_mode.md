# dcnm_maintenance_mode

???+ "Details"

    - author
        - Allen Robel (@quantumonion)
    - description
        - Enable Maintenance or Normal Mode.
    - short_description
        - Manage Maintenance Mode Configuration of NX-OS Switches.
    - version_added
        - 3.6.0


## options

???+ "Details"


### config

???+ "Details"

    - description
        - A dictionary containing the maintenance mode configuration.
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
    - elements
        - dict
    - required
        - True

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
    - type
        - list

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
    - type
        - dict

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

## Examples

???+ "Details"

``` yaml
---

# Enable maintenance mode on all switches.
# Do not deploy the configuration on any switch.

- name: Configure switch mode
  cisco.dcnm.dcnm_maintenance_mode:
    state: merged
    config:
        deploy: true
        wait_for_mode_change: true
        mode: maintenance
        switches:
            -   ip_address: 192.168.1.2
            -   ip_address: 192.160.1.3
            -   ip_address: 192.160.1.4
  register: result
- debug:
    var: result

# Enable maintenance mode on two switches.
# Enable normal mode on one switch.
# Deploy the configuration on one switch.

- name: Configure switch mode
  cisco.dcnm.dcnm_maintenance_mode:
    state: merged
    config:
        deploy: false
        mode: maintenance
        switches:
            -   ip_address: 192.168.1.2
                mode: normal
            -   ip_address: 192.160.1.3
                deploy: true
                wait_for_mode_change: true
            -   ip_address: 192.160.1.4
  register: result
- debug:
    var: result


```
