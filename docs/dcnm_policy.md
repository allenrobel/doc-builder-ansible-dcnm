# dcnm_policy

???+ "Details"

    - short_description
        - DCNM Ansible Module for managing policies.
    - version_added
        - 1.1.0
    - description
        - DCNM Ansible Module for Creating, Deleting, Querying and Modifying policies
    - author
        - Mallik Mudigonda(@mmudigon)


## options

???+ "Details"


### fabric

???+ "Details"

    - description
        - Name of the target fabric for policy operations
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

### use_desc_as_key

???+ "Details"

    - description
        - Flag to enforce using the description parameter as the unique key for policy management. 
        - When set to True, the description parameter must be unique and non-empty for each policy in the playbook. The module will also use the description to find the policy to modify or delete. If exsiting policies have the same description, the module will raise an error. If the existing policy with the matching description is using differnet template name, the module will delete the existing policy and create a new one.
    - type
        - bool
    - required
        - False
    - default
        - False

### deploy

???+ "Details"

    - description
        - A flag specifying if a policy is to be deployed on the switches
    - type
        - bool
    - required
        - False
    - default
        - True

### config

???+ "Details"

    - description
        - A list of dictionaries containing policy and switch information
    - type
        - list
    - elements
        - dict

#### name

???+ "Details"

    - description
        - This can be one of the following a) Template Name 
        - A unique name identifying the template. Please note that a template name can be used by multiple policies and hence a template name does not identify a policy uniquely. b) Policy ID     
        - A unique ID identifying a policy. Policy ID MUST be used for modifying policies since template names cannot uniquely identify a policy
    - type
        - str
    - required
        - True

#### description1

???+ "Details"

    - description
        - Description of the policy. The description may include the details regarding the policy i.e. the arguments if any etc.
    - type
        - str
    - required
        - False
    - default
        - 

#### priority

???+ "Details"

    - description
        - Priority associated with the policy
    - type
        - str
    - required
        - False
    - default
        - 500

#### create_additional_policy

???+ "Details"

    - description
        - A flag indicating if a policy is to be created even if an identical policy already exists
    - type
        - bool
    - required
        - False
    - default
        - True

#### policy_vars

???+ "Details"

    - description
        - A set of arguments required for creating and deploying policies. The arguments are specific to each policy and depends on the tmeplate that is used by the policy.
    - type
        - dict
    - required
        - False
    - default
        - {}

#### switch

???+ "Details"

    - description
        - A dictionary of switches and associated policy information. All switches in this list will be deployed with only those policies that are included under "policies" object i.e. 'policies' object will override the list of policies for this particular switch. If 'policies' object is not included, then other policies specified in the configurstion will be deployed to these switches.
    - type
        - list
    - elements
        - dict

##### ip

???+ "Details"

    - description
        - IP address of the switch where the policy is to be deployed. This can be IPV4 address, IPV6 address or hostname
    - type
        - str
    - required
        - True

##### policies

???+ "Details"

    - description
        - A list of policies to be deployed on the switch. Note only policies included here will be deployed on the switch irrespective of other polcies included in the configuration.
    - type
        - list
    - elements
        - dict
    - required
        - False
    - default
        - []

###### name

???+ "Details"

    - description
        - This can be one of the following a) Template Name 
        - A unique name identifying the template. Please note that a template name can be used by multiple policies and hence a template name does not identify a policy uniquely. b) Policy ID     
        - A unique ID identifying a policy. Policy ID MUST be used for modifying policies since template names cannot uniquely identify a policy
    - type
        - str
    - required
        - True

###### description1

???+ "Details"

    - description
        - Description of the policy. The description may include the details regarding the policy
    - type
        - str
    - required
        - False
    - default
        - 

###### priority

???+ "Details"

    - description
        - Priority associated with the policy
    - type
        - str
    - required
        - False
    - default
        - 500

###### create_additional_policy

???+ "Details"

    - description
        - A flag indicating if a policy is to be created even if an identical policy already exists
    - type
        - bool
    - required
        - False
    - default
        - True

###### policy_vars

???+ "Details"

    - description
        - A set of arguments required for creating and deploying policies. The arguments are specific to each policy and that depends on the tmeplate that is used by the policy.
    - type
        - dict
    - required
        - False
    - default
        - {}
