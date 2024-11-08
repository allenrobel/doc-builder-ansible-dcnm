# dcnm_image_policy

???+ "Details"

    - short_description
        - Image policy management for Nexus Dashboard Fabric Controller
    - version_added
        - 3.5.0
    - description
        - Create, delete, modify image policies.
    - author
        - Allen Robel (@quantumonion)


## options

???+ "Details"


### state

???+ "Details"

    - description
        - The state of the feature or object after module completion
    - type
        - str
    - choices
        - deleted
        - merged
        - overridden
        - query
        - replaced
    - default
        - merged

### config

???+ "Details"

    - description
        - List of dictionaries containing image policy parameters
    - type
        - list
    - elements
        - dict
    - default
        - []

#### name

???+ "Details"

    - description
        - The image policy name.
    - type
        - str
    - required
        - True

#### agnostic

???+ "Details"

    - description
        - The agnostic flag.
    - type
        - bool
    - default
        - False
    - required
        - False

#### description1

???+ "Details"

    - description
        - The image policy description.
    - type
        - str
    - default
        - 
    - required
        - False

#### epld_image

???+ "Details"

    - description
        - The epld image name.
    - type
        - str
    - default
        - 
    - required
        - False

#### packages

???+ "Details"

    - description
        - A dictionary containing two keys, install and uninstall.
    - type
        - dict
    - required
        - False

##### install

???+ "Details"

    - description
        - A list of packages to install.
    - type
        - list
    - elements
        - str
    - required
        - False

##### uninstall

???+ "Details"

    - description
        - A list of packages to uninstall.
    - type
        - list
    - elements
        - str
    - required
        - False

#### platform

???+ "Details"

    - description
        - The platform to which the image policy applies e.g. N9K.
    - type
        - str
    - required
        - True

#### release

???+ "Details"

    - description
        - The release associated with the image policy. 
        - This is derived from the image name as follows. 
        - From image name nxos64-cs.10.2.5.M.bin 
        - we need to extract version (10.2.5), platform (nxos64-cs), and bits (64bit). 
        - The release string conforms to format (version)_(platform)_(bits) 
        - so the resulting release string will be 10.2.5_nxos64-cs_64bit
    - type
        - str
    - required
        - True

#### type

???+ "Details"

    - description
        - The type of the image policy e.g. PLATFORM.
    - type
        - str
    - default
        - PLATFORM
    - required
        - False
