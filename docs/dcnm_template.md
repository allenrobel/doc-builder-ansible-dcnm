# dcnm_template

???+ "Details"

    - short_description
        - DCNM Ansible Module for managing templates.
    - version_added
        - 1.1.0
    - description
        - DCNM Ansible Module for creating, deleting and modifying template service 
        - operations
    - author
        - Mallik Mudigonda(@mmudigon)


## options

???+ "Details"


### state

???+ "Details"

    - description
        - The required state of the configuration after module completion.
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
        - A dictionary of template operations
    - type
        - list
    - elements
        - dict
    - required
        - True

#### name

???+ "Details"

    - description
        - Name of the template.
    - type
        - str

#### description1

???+ "Details"

    - description
        - Description of the template. The description may include the details regarding the content
    - type
        - str
    - default
        - 

#### tags

???+ "Details"

    - description
        - User defined labels for identifying the templates
    - type
        - str
    - default
        - 

#### content

???+ "Details"

    - description
        - Multiple line configuration snip that can be used to associate to devices as policy
    - type
        - str

#### type

???+ "Details"

    - description
        - Type of the template content either CLI or Python
    - type
        - str
    - choices
        - cli
        - python
    - default
        - cli
