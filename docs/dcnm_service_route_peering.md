# dcnm_service_route_peering

???+ "Details"

    - short_description
        - DCNM Ansible Module for managing Service Route Peerings.
    - version_added
        - 1.2.0
    - description
        - DCNM Ansible Module for Creating, Deleting, Querying and Modifying Route Peerings
    - author
        - Mallik Mudigonda (@mmudigon)


## options

???+ "Details"


### fabric

???+ "Details"

    - description
        - 'Name of the target fabric for route peering operations'
    - type
        - str
    - required
        - True

### service_fabric

???+ "Details"

    - description
        - 'Name of the external fabric attached to the service node for route peering operations'
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
        - replaced
        - overridden
        - deleted
        - query
    - default
        - merged

### attach

???+ "Details"

    - description
        - A flag specifying if the given route peering is to be attached to the specified service node
    - type
        - bool
    - required
        - False
    - default
        - True

### deploy

???+ "Details"

    - description
        - A flag specifying if a route peering is to be deployed on the switches
    - type
        - bool
    - required
        - False
    - default
        - True

### config

???+ "Details"

    - description
        - A list of dictionaries containing route peering and switch information
    - type
        - list
    - elements
        - dict

#### name

???+ "Details"

    - description
        - A unique name which identifies the route peering
    - type
        - str
    - required
        - True

#### node_name

???+ "Details"

    - description
        - Name of the service node where the route peering is to be deployed
    - type
        - str
    - required
        - True

#### deploy_mode

???+ "Details"

    - description
        - Type of service node.
    - type
        - str
    - required
        - True
    - choices
        - intra_tenant_fw
        - inter_tenant_fw
        - one_arm_adc
        - two_arm_adc

#### peering_option

???+ "Details"

    - description
        - Specifies the type of peering 
        - This parameter is applicable only when 'deploy_mode' is either 'inter_tenant_fw' or 'one_arm_adc' or 'two_arm_adc'
    - type
        - str
    - required
        - False
    - default
        - static
    - choices
        - static
        - ebgp

#### next_hop

???+ "Details"

    - description
        - Nexthop IPV4 information, e.g., 192.168.1.100 
        - This parameter is applicable only when 'deploy_mode' is 'intra_tenant_fw'
    - type
        - int
    - required
        - True

#### reverse_next_hop

???+ "Details"

    - description
        - Reverse Nexthop IPV4 information, e.g., 192.169.1.100 
        - This parameter is applicable only when 'deploy_mode' is either 'intra_tenant_fw' or 'one_arm_adc' or 'two_arm_adc'
    - type
        - str
    - required
        - False
    - default
        - 

#### inside_network

???+ "Details"

    - description
        - Details regarding inside network of the route peering 
        - This parameter is applicable only when 'deploy_mode' is 'intra_tenant_fw' or 'inter_tenant_fw'
    - type
        - dict
    - required
        - True

##### vrf

???+ "Details"

    - description
        - VRF name for the inside network
    - type
        - str
    - required
        - True

##### name

???+ "Details"

    - description
        - Network name
    - type
        - str
    - required
        - True

##### vlan_id

???+ "Details"

    - description
        - Vlan Id for the inside network 
        - If this object is included and if it is already in use, then the module will allocate a new VLAN ID and create the Route Peering. The user provided 'vlan_id' will be ignored.
    - type
        - int
    - required
        - False
    - default
        - 0

##### profile

???+ "Details"

    - description
        - Profile information for the inside network
    - type
        - dict
    - required
        - True

###### ipv4_gw

???+ "Details"

    - description
        - IPV4 gateway information including the mask e.g. 192.168.1.1/24
    - type
        - str
    - required
        - True

###### ipv6_gw

???+ "Details"

    - description
        - IPV6 gateway information including the mask e.g., 2000:01:01::01/64
    - type
        - str
    - required
        - False
    - default
        - 

###### vlan_name

???+ "Details"

    - description
        - Vlan name
    - type
        - str
    - required
        - False
    - default
        - 

###### int_descr

???+ "Details"

    - description
        - Description of the interface
    - type
        - str
    - required
        - False
    - default
        - 

###### tag

???+ "Details"

    - description
        - Route tag information
    - type
        - int
    - required
        - False
    - default
        - 12345

###### static_route

???+ "Details"

    - description
        - Static route information 
        - This parameter is applicable only when 'peering_option' is 'static'
    - type
        - list
    - elements
        - dict
    - required
        - False
    - default
        - []

####### subnet

???+ "Details"

    - description
        - Subnet information, for e.g., 11.0.0.0/24
    - type
        - str
    - required
        - True

####### next_hop

???+ "Details"

    - description
        - Gateway IP addresses, for e.g., 192.168.1.1
    - type
        - list
    - elements
        - str
    - required
        - True

###### ipv4_neighobor

???+ "Details"

    - description
        - IPv4 neighbor address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - True

###### ipv4_lo

???+ "Details"

    - description
        - IPv4 loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - True

###### ipv4_vpc_peer_lo

???+ "Details"

    - description
        - IPv4 vpc peer loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'. This parameter is mandatory if the service node is part of VPC switch pair
    - type
        - str
    - required
        - False
    - default
        - 

###### ipv6_neighbor

???+ "Details"

    - description
        - IPv6 neighbor address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - False
    - default
        - 

###### ipv6_lo

???+ "Details"

    - description
        - IPv6 loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - False
    - default
        - 

###### ipv6_vpc_peer_lo

???+ "Details"

    - description
        - IPv6 vpc peer loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'. This object is mandatory if the service node switch is part of VPC pair
    - type
        - str
    - required
        - False
    - default
        - 

###### route_map_tag

???+ "Details"

    - description
        - Route Tag 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - int
    - default
        - 12345

###### neigh_int_descr

???+ "Details"

    - description
        - Description of the interface 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - False
    - default
        - 

###### local_asn

???+ "Details"

    - description
        - Local ASN number 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - int
    - required
        - False
    - default
        - 12345

###### adv_host

???+ "Details"

    - description
        - Flag indicating if the host is to be advertised 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - bool
    - required
        - False
    - default
        - True

#### outside_network

???+ "Details"

    - description
        - Details regarding outside network of the route peering 
        - This parameter is applicable only when 'deploy_mode' is 'intra_tenant_fw' or 'inter_tenant_fw'
    - type
        - dict
    - required
        - True

##### vrf

???+ "Details"

    - description
        - VRF name for the outside network
    - type
        - str
    - required
        - True

##### name

???+ "Details"

    - description
        - Network name
    - type
        - str
    - required
        - True

##### vlan_id

???+ "Details"

    - description
        - Vlan Id for the outside network 
        - If this object is included and if it is already in use, then the module will allocate a new VLAN ID and create the Route Peering. The user provided 'vlan_id' will be ignored.
    - type
        - int
    - required
        - False
    - default
        - 0

##### profile

???+ "Details"

    - description
        - Profile information for the outside network
    - type
        - dict
    - required
        - True

###### ipv4_gw

???+ "Details"

    - description
        - IPV4 gateway information including the mask e.g. 192.168.1.1/24
    - type
        - str
    - required
        - True

###### ipv6_gw

???+ "Details"

    - description
        - IPV6 gateway information including the mask e.g., 2000:01:01::01/64
    - type
        - str
    - required
        - False
    - default
        - 

###### vlan_name

???+ "Details"

    - description
        - Vlan name
    - type
        - str
    - required
        - False
    - default
        - 

###### int_descr

???+ "Details"

    - description
        - Description of the interface
    - type
        - str
    - required
        - False
    - default
        - 

###### tag

???+ "Details"

    - description
        - Route tag information
    - type
        - int
    - required
        - False
    - default
        - 12345

###### static_route

???+ "Details"

    - description
        - Static route information 
        - This parameter is applicable only when 'peering_option' is 'static' and 'deploy_mode' is 'intra_tenant_fw'
    - type
        - list
    - elements
        - dict
    - required
        - False
    - default
        - []

####### subnet

???+ "Details"

    - description
        - Subnet information, for e.g., 11.0.0.0/24
    - type
        - str
    - required
        - True

####### next_hop

???+ "Details"

    - description
        - Gateway IP addresses, for e.g., 192.168.1.1
    - type
        - list
    - elements
        - str
    - required
        - True

###### ipv4_neighobor

???+ "Details"

    - description
        - IPv4 neighbor address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - True

###### ipv4_lo

???+ "Details"

    - description
        - IPv4 loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - True

###### ipv4_vpc_peer_lo

???+ "Details"

    - description
        - IPv4 vpc peer loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'. This parameter is mandatory if the service node is part of VPC switch pair
    - type
        - str
    - required
        - False
    - default
        - 

###### ipv6_neighbor

???+ "Details"

    - description
        - IPv6 neighbor address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - False
    - default
        - 

###### ipv6_lo

???+ "Details"

    - description
        - IPv6 loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - False
    - default
        - 

###### ipv6_vpc_peer_lo

???+ "Details"

    - description
        - IPv6 vpc peer loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp' This parameter is mandatory if the service node is part of VPC switch pair
    - type
        - str
    - required
        - False
    - default
        - 

###### route_map_tag

???+ "Details"

    - description
        - Route Tag 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - int
    - default
        - 12345

###### neigh_int_descr

???+ "Details"

    - description
        - Description of the interface 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - False
    - default
        - 

###### local_asn

???+ "Details"

    - description
        - Local ASN number 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - int
    - required
        - False
    - default
        - 12345

###### adv_host

???+ "Details"

    - description
        - Flag indicating if the host is to be advertised 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - bool
    - required
        - False
    - default
        - True

#### first_arm

???+ "Details"

    - description
        - Details regarding first arm of the route peering 
        - This parameter is applicable only when 'deploy_mode' is either 'one_arm_adc' or 'two_arm_adc'
    - type
        - dict
    - required
        - True

##### vrf

???+ "Details"

    - description
        - VRF name for the first arm
    - type
        - str
    - required
        - True

##### name

???+ "Details"

    - description
        - Network name
    - type
        - str
    - required
        - True

##### vlan_id

???+ "Details"

    - description
        - Vlan Id for the  first arm 
        - If this object is included and if it is already in use, then the module will allocate a new VLAN ID and create the Route Peering. The user provided 'vlan_id' will be ignored.
    - type
        - int
    - required
        - False
    - default
        - 0

##### profile

???+ "Details"

    - description
        - Profile information for the first arm
    - type
        - dict
    - required
        - True

###### ipv4_gw

???+ "Details"

    - description
        - IPV4 gateway information including the mask e.g. 192.168.1.1/24
    - type
        - str
    - required
        - True

###### ipv6_gw

???+ "Details"

    - description
        - IPV6 gateway information including the mask e.g., 2000:01:01::01/64
    - type
        - str
    - required
        - False
    - default
        - 

###### vlan_name

???+ "Details"

    - description
        - Vlan name
    - type
        - str
    - required
        - False
    - default
        - 

###### int_descr

???+ "Details"

    - description
        - Description of the interface
    - type
        - str
    - required
        - False
    - default
        - 

###### tag

???+ "Details"

    - description
        - Route tag information
    - type
        - int
    - required
        - False
    - default
        - 12345

###### static_route

???+ "Details"

    - description
        - Static route information 
        - This parameter is applicable only when 'peering_option' is 'static'
    - type
        - list
    - elements
        - dict
    - required
        - False
    - default
        - []

####### subnet

???+ "Details"

    - description
        - Subnet information, for e.g., 11.0.0.0/24
    - type
        - str
    - required
        - True

####### next_hop

???+ "Details"

    - description
        - Gateway IP addresses, for e.g., 192.168.1.1
    - type
        - list
    - elements
        - str
    - required
        - True

###### ipv4_neighobor

???+ "Details"

    - description
        - IPv4 neighbor address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - True

###### ipv4_lo

???+ "Details"

    - description
        - IPv4 loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - True

###### ipv4_vpc_peer_lo

???+ "Details"

    - description
        - IPv4 vpc peer loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp' This parameter is mandatory if the service node is part of VPC switch pair
    - type
        - str
    - required
        - False
    - default
        - 

###### ipv6_neighbor

???+ "Details"

    - description
        - IPv6 neighbor address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - False
    - default
        - 

###### ipv6_lo

???+ "Details"

    - description
        - IPv6 loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - False
    - default
        - 

###### ipv6_vpc_peer_lo

???+ "Details"

    - description
        - IPv6 vpc peer loopback address 
        - This parameter is applicable only when 'peering_option' is 'ebgp' This parameter is mandatory if the service node is part of VPC switch pair
    - type
        - str
    - required
        - False
    - default
        - 

###### route_map_tag

???+ "Details"

    - description
        - Route Tag 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - int
    - default
        - 12345

###### neigh_int_descr

???+ "Details"

    - description
        - Description of the interface 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - str
    - required
        - False
    - default
        - 

###### local_asn

???+ "Details"

    - description
        - Local ASN number 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - int
    - required
        - False
    - default
        - 12345

###### adv_host

???+ "Details"

    - description
        - Flag indicating if the host is to be advertised 
        - This parameter is applicable only when 'peering_option' is 'ebgp'
    - type
        - bool
    - required
        - False
    - default
        - True

#### second_arm

???+ "Details"

    - description
        - Details regarding second arm of the route peering 
        - This parameter is applicable only when 'deploy_mode' is either 'one_arm_adc' or 'two_arm_adc'
    - type
        - dict
    - required
        - True

##### vrf

???+ "Details"

    - description
        - VRF name for the second arm
    - type
        - str
    - required
        - True

##### name

???+ "Details"

    - description
        - Network name
    - type
        - str
    - required
        - True

##### vlan_id

???+ "Details"

    - description
        - Vlan Id for the second arm 
        - If this object is included and if it is already in use, then the module will allocate a new VLAN ID and create the Route Peering. The user provided 'vlan_id' will be ignored.
    - type
        - int
    - required
        - False
    - default
        - 0

##### profile

???+ "Details"

    - description
        - Profile information for the second arm
    - type
        - dict
    - required
        - True

###### ipv4_gw

???+ "Details"

    - description
        - IPV4 gateway information including the mask e.g. 192.168.1.1/24
    - type
        - str
    - required
        - True

###### ipv6_gw

???+ "Details"

    - description
        - IPV6 gateway information including the mask e.g., 2000:01:01::01/64
    - type
        - str
    - required
        - False
    - default
        - 

###### vlan_name

???+ "Details"

    - description
        - Vlan name
    - type
        - str
    - required
        - False
    - default
        - 

###### int_descr

???+ "Details"

    - description
        - Description of the interface
    - type
        - str
    - required
        - False
    - default
        - 

###### tag

???+ "Details"

    - description
        - Route tag information
    - type
        - int
    - required
        - False
    - default
        - 12345
