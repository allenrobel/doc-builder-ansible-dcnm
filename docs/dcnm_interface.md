# dcnm_interface

???+ "Details"

    - short_description
        - DCNM Ansible Module for managing interfaces.
    - version_added
        - 0.9.0
    - description
        - "DCNM Ansible Module for the following interface service operations" 
        - "Create, Delete, Modify PortChannel, VPC, Loopback and Sub-Interfaces" 
        - "Modify Ethernet Interfaces"
    - author
        - Mallik Mudigonda(@mmudigon)


## options

???+ "Details"


### check_deploy

???+ "Details"

    - description
        - Deploy operations may take considerable time in certain cases based on the configuration included in the playbook. A success response from DCNM server does not guarantee the completion of deploy operation. This flag if set indicates that the module should verify if the configured state is in sync with what is requested in playbook. If not set the module will return without verifying the state.
    - type
        - bool
    - required
        - False
    - default
        - False

### fabric

???+ "Details"

    - description
        - Name of the target fabric for interface operations
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
    - choices
        - merged
        - replaced
        - overridden
        - deleted
        - query
    - default
        - merged

### deploy

???+ "Details"

    - description
        - Flag indicating if the configuration must be pushed to the switch. This flag is used to decide the deploy behavior in 'deleted' and 'overridden' states as mentioned below 
        - In 'overridden' state this flag will be used to deploy deleted interfaces. 
        - In 'deleted' state this flag will be used to deploy deleted interfaces when a specific 'config' block is not included. 
        - The 'deploy' flags included with individual interface configuration elements under the 'config' block will take precedence over this global flag.
    - type
        - bool
    - default
        - True

### override_intf_types

???+ "Details"

    - description
        - A list of interface types which will be deleted/defaulted in overridden/deleted state. If this list is empty, then during overridden/deleted state, all interface types will be defaulted/deleted. If this list includes specific interface types, then only those interface types that are included in the list will be deleted/defaulted.
    - type
        - list
    - required
        - False
    - elements
        - str
    - choices
        - pc
        - vpc
        - sub_int
        - lo
        - eth
        - svi
        - st_fex
        - aa_fex
    - default
        - []

### config

???+ "Details"

    - description
        - A dictionary of interface operations
    - type
        - list
    - elements
        - dict
    - default
        - []

#### name

???+ "Details"

    - description
        - Name of the interface. Example, po55, eth2/1, lo100, vpc25, eth1/1.1.
    - type
        - str
    - required
        - True

#### switch

???+ "Details"

    - description
        - IP address or DNS name of the management interface. All switches mentioned in this list will be deployed with the included configuration. For vPC interfaces this list object will contain elements each of which is a list of pair of switches
    - type
        - list
    - elements
        - str
    - required
        - True

#### type

???+ "Details"

    - description
        - Interface type. Example, pc, vpc, sub_int, lo, eth, svi
    - type
        - str
    - required
        - True
    - choices
        - pc
        - vpc
        - sub_int
        - lo
        - eth
        - svi
        - st-fex
        - aa-fex

#### deploy

???+ "Details"

    - description
        - Flag indicating if the configuration must be pushed to the switch. If not included it is considered true by default
    - type
        - bool
    - default
        - True

#### profile_pc

???+ "Details"

    - description
        - Though the key shown here is 'profile_pc' the actual key to be used in playbook is 'profile'. The key 'profile_pc' is used here to logically segregate the interface objects applicable for this profile 
        - Object profile which must be included for port channel interface configurations.

##### mode

???+ "Details"

    - description
        - Interface mode
    - choices
        - trunk
        - access
        - l3
        - monitor
    - type
        - str
    - required
        - True

##### members

???+ "Details"

    - description
        - Member interfaces that are part of this port channel
    - type
        - list
    - elements
        - str
    - required
        - True

##### access_vlan

???+ "Details"

    - description
        - Vlan for the interface. This option is applicable only for interfaces whose 'mode' is 'access'
    - type
        - str
    - default
        - 

##### int_vrf

???+ "Details"

    - description
        - Interface VRF name. This object is applicable only if the 'mode' is 'l3'
    - type
        - str
    - default
        - default

##### ipv4_addr

???+ "Details"

    - description
        - IPV4 address of the interface. This object is applicable only if the 'mode' is 'l3'
    - type
        - str
    - default
        - 

##### ipv4_mask_len

???+ "Details"

    - description
        - IPV4 address mask length. This object is applicable only if the 'mode' is 'l3' 
        - Minimum Value (1), Maximum Value (31)
    - type
        - int
    - default
        - 8

##### route_tag

???+ "Details"

    - description
        - Route tag associated with the interface IP. This object is applicable only if the 'mode' is 'l3'
    - type
        - str
    - default
        - 

##### cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface
    - type
        - list
    - elements
        - str
    - default
        - []

##### description1

???+ "Details"

    - description
        - Description of the interface
    - type
        - str
    - default
        - 

##### admin_state

???+ "Details"

    - description
        - Administrative state of the interface
    - type
        - bool
    - default
        - True

#### profile_vpc

???+ "Details"

    - description
        - Though the key shown here is 'profile_vpc' the actual key to be used in playbook is 'profile'. The key 'profile_vpc' is used here to logically segregate the interface objects applicable for this profile 
        - Object profile which must be included for virtual port channel inetrface configurations.

##### mode

???+ "Details"

    - description
        -  Interface mode
    - choices
        - trunk
        - access
    - type
        - str
    - required
        - True

##### peer1_pcid

???+ "Details"

    - description
        - Port channel identifier of first peer. If this object is not included, then the value defaults to the vPC identifier. This value cannot be changed once vPC is created 
        - Minimum Value (1), Maximum Value (4096) 
        - Default value if not specified is the vPC port identifier
    - type
        - int

##### peer2_pcid

???+ "Details"

    - description
        - Port channel identifier of second peer. If this object is not included, then the value defaults to the vPC identifier. This value cannot be changed once vPC is created 
        - Minimum Value (1), Maximum Value (4096) 
        - Default value if not specified is the vPC port identifier
    - type
        - int

##### peer1_members

???+ "Details"

    - description
        - Member interfaces that are part of this port channel on first peer
    - type
        - list
    - elements
        - str
    - required
        - True

##### peer2_members

???+ "Details"

    - description
        - Member interfaces that are part of this port channel on second peer
    - type
        - list
    - elements
        - str
    - required
        - True

##### pc_mode

???+ "Details"

    - description
        - Port channel mode
    - type
        - str
    - choices
        - active
        - passive
        - on
    - default
        - active

##### bpdu_guard

???+ "Details"

    - description
        - Spanning-tree bpduguard
    - type
        - str
    - choices
        - true
        - false
        - no
    - default
        - true

##### port_type_fast

???+ "Details"

    - description
        - Spanning-tree edge port behavior
    - type
        - bool
    - choices
        - True
        - False
    - default
        - True

##### mtu

???+ "Details"

    - description
        - Interface MTU
    - type
        - str
    - choices
        - default
        - jumbo
    - default
        - jumbo

##### peer1_allowed_vlans

???+ "Details"

    - description
        - Vlans that are allowed on this interface of first peer. This option is applicable only for interfaces whose 'mode' is 'trunk'
    - type
        - str
    - choices
        - none
        - all
        - vlan-range(e.g., 1-2, 3-40)
    - default
        - none

##### peer2_allowed_vlans

???+ "Details"

    - description
        - Vlans that are allowed on this interface of second peer. This option is applicable only for interfaces whose 'mode' is 'trunk'
    - type
        - str
    - choices
        - none
        - all
        - vlan-range(e.g., 1-2, 3-40)
    - default
        - none

##### peer1_access_vlan

???+ "Details"

    - description
        - Vlan for the interface of first peer. This option is applicable only for interfaces whose 'mode' is 'access'
    - type
        - str
    - default
        - 

##### peer2_access_vlan

???+ "Details"

    - description
        - Vlan for the interface of second peer. This option is applicable only for interfaces whose 'mode' is 'access'
    - type
        - str
    - default
        - 

##### peer1_cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface of first peer
    - type
        - list
    - elements
        - str
    - default
        - []

##### peer2_cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface of second peer
    - type
        - list
    - elements
        - str
    - default
        - []

##### peer1_description

???+ "Details"

    - description
        - Description of the interface of first peer
    - type
        - str
    - default
        - 

##### peer2_description

???+ "Details"

    - description
        - Description of the interface of second peer
    - type
        - str
    - default
        - 

##### admin_state

???+ "Details"

    - description
        - Administrative state of the interface
    - type
        - bool
    - default
        - True

#### profile_subint

???+ "Details"

    - description
        - Though the key shown here is 'profile_subint' the actual key to be used in playbook is 'profile'. The key 'profile_subint' is used here to logically segregate the interface objects applicable for this profile 
        - Object profile which must be included for sub-interface configurations.

##### mode

???+ "Details"

    - description
        - Interface mode
    - choices
        - subint
    - type
        - str
    - required
        - True

##### int_vrf

???+ "Details"

    - description
        - Interface VRF name.
    - type
        - str
    - default
        - default

##### ipv4_addr

???+ "Details"

    - description
        - IPV4 address of the interface.
    - type
        - str
    - default
        - 

##### ipv4_mask_len

???+ "Details"

    - description
        - IPV4 address mask length. 
        - Minimum Value (8), Maximum Value (31)
    - type
        - int
    - default
        - 8

##### ipv6_addr

???+ "Details"

    - description
        - IPV6 address of the interface.
    - type
        - str
    - default
        - 

##### ipv6_mask_len

???+ "Details"

    - description
        - IPV6 address mask length. 
        - Minimum Value (1), Maximum Value (31)
    - type
        - int
    - default
        - 8

##### mtu

???+ "Details"

    - description
        - Interface MTU 
        - Minimum Value (567), Maximum Value (9216)
    - type
        - int
    - default
        - 9216

##### vlan

???+ "Details"

    - description
        - DOT1Q vlan id for this interface 
        - Minimum Value (2), Maximum Value (3967)
    - type
        - int
    - default
        - 0

##### cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface
    - type
        - list
    - elements
        - str
    - default
        - []

##### description1

???+ "Details"

    - description
        - Description of the interface
    - type
        - str
    - default
        - 

##### admin_state

???+ "Details"

    - description
        - Administrative state of the interface
    - type
        - bool
    - default
        - True

#### profile_lo

???+ "Details"

    - description
        - Though the key shown here is 'profile_lo' the actual key to be used in playbook is 'profile'. The key 'profile_lo' is used here to logically segregate the interface objects applicable for this profile 
        - Object profile which must be included for loopback interface configurations.

##### mode

???+ "Details"

    - choices
        - lo
        - fabric
        - mpls
    - description
        - There are several modes for loopback interfaces. 
        - Mode 'lo' is used to create, modify and delete non fabric loopback interfaces using policy 'int_loopback'. 
        - Mode 'fabric' is used to modify loopbacks created when the fabric is first created using policy 'int_fabric_loopback_11_1' 
        - Mode 'mpls' is used to modify loopbacks created when the fabric is first created using policy 'int_mpls_loopback' 
        - Mode 'fabric' and 'mpls' interfaces can be modified but not created or deleted.
    - type
        - str
    - required
        - True

##### int_vrf

???+ "Details"

    - description
        - Interface VRF name.
    - type
        - str
    - default
        - default

##### ipv4_addr

???+ "Details"

    - description
        - IPv4 address of the interface.
    - type
        - str
    - default
        - 

##### secondary_ipv4_addr

???+ "Details"

    - description
        - Secondary IP address of the nve interface loopback
    - type
        - str
    - default
        - 

##### ipv6_addr

???+ "Details"

    - description
        - IPv6 address of the interface.
    - type
        - str
    - default
        - 

##### route_tag

???+ "Details"

    - description
        - Route tag associated with the interface IP.
    - type
        - str
    - default
        - 

##### cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface
    - type
        - list
    - elements
        - str
    - default
        - []

##### description1

???+ "Details"

    - description
        - Description of the interface
    - type
        - str
    - default
        - 

##### admin_state

???+ "Details"

    - description
        - Administrative state of the interface
    - type
        - bool
    - default
        - True

#### profile_eth

???+ "Details"

    - description
        - Though the key shown here is 'profile_eth' the actual key to be used in playbook is 'profile'. The key 'profile_eth' is used here to logically segregate the interface objects applicable for this profile 
        - Object profile which must be included for ethernet interface configurations.

##### mode

???+ "Details"

    - description
        - Interface mode
    - choices
        - trunk
        - access
        - routed
        - monitor
        - epl_routed
    - type
        - str
    - required
        - True

##### bpdu_guard

???+ "Details"

    - description
        - Spanning-tree bpduguard
    - type
        - str
    - choices
        - true
        - false
        - no
    - default
        - true

##### port_type_fast

???+ "Details"

    - description
        - Spanning-tree edge port behavior
    - type
        - bool
    - choices
        - True
        - False
    - default
        - True

##### mtu

???+ "Details"

    - description
        - Interface MTU. 
        - Can be specified either "default" or "jumbo" for access and trunk interface types. If not specified, it defaults to "jumbo" 
        - Can be specified with any value within 576 and 9216 for routed interface types. If not specified, it defaults to 9216
    - type
        - str

##### allowed_vlans

???+ "Details"

    - description
        - Vlans that are allowed on this interface. This option is applicable only for interfaces whose 'mode' is 'trunk'
    - type
        - str
    - choices
        - none
        - all
        - vlan-range(e.g., 1-2, 3-40)
    - default
        - none

##### access_vlan

???+ "Details"

    - description
        - Vlan for the interface. This option is applicable only for interfaces whose 'mode' is 'access'
    - type
        - str
    - default
        - 

##### speed

???+ "Details"

    - description
        - Speed of the interface.
    - type
        - str
    - default
        - Auto

##### int_vrf

???+ "Details"

    - description
        - Interface VRF name. This object is applicable only if the 'mode' is 'routed'
    - type
        - str
    - default
        - default

##### ipv4_addr

???+ "Details"

    - description
        - IPV4 address of the interface. This object is applicable only if the 'mode' is 'routed' or 'epl_routed'
    - type
        - str
    - default
        - 

##### ipv4_mask_len

???+ "Details"

    - description
        - IPV4 address mask length. This object is applicable only if the 'mode' is 'routed' or 'epl_routed' 
        - Minimum Value (1), Maximum Value (31)
    - type
        - int
    - default
        - 8

##### ipv6_addr

???+ "Details"

    - description
        - IPV6 address of the interface. This object is applicable only if the 'mode' is 'epl_routed'
    - type
        - str
    - default
        - 

##### ipv6_mask_len

???+ "Details"

    - description
        - IPV6 address mask length. This object is applicable only if the 'mode' is 'epl_routed' 
        - Minimum Value (1), Maximum Value (31)
    - type
        - int
    - default
        - 8

##### route_tag

???+ "Details"

    - description
        - Route tag associated with the interface IP. This object is applicable only if the 'mode' is 'routed' or 'epl_routed'
    - type
        - str
    - default
        - 

##### cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface
    - type
        - list
    - elements
        - str
    - default
        - []

##### description1

???+ "Details"

    - description
        - Description of the interface
    - type
        - str
    - default
        - 

##### admin_state

???+ "Details"

    - description
        - Administrative state of the interface
    - type
        - bool
    - default
        - True

#### profile_svi

???+ "Details"

    - description
        - Though the key shown here is 'profile_svi' the actual key to be used in playbook is 'profile'. The key 'profile_svi' is used here to logically segregate the interface objects applicable for this profile 
        - Object profile which must be included for SVI interface configurations.

##### mode

???+ "Details"

    - description
        - Interface mode.
    - choices
        - vlan
    - type
        - str
    - required
        - True

##### int_vrf

???+ "Details"

    - description
        - Interface VRF name.
    - type
        - str
    - default
        - default

##### ipv4_addr

???+ "Details"

    - description
        - IPV4 address of the interface.
    - type
        - str
    - default
        - 

##### ipv4_mask_len

???+ "Details"

    - description
        - IPV4 address mask length. This parameter is required if 'ipv4_addr' is included. 
        - Minimum Value (1), Maximum Value (31)
    - type
        - int

##### cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface.
    - type
        - list
    - elements
        - str
    - default
        - []

##### description1

???+ "Details"

    - description
        - Description of the interface.
    - type
        - str
    - default
        - 

##### admin_state

???+ "Details"

    - description
        - Administrative state of the interface.
    - type
        - bool
    - required
        - True

##### route_tag

???+ "Details"

    - description
        - Route tag associated with the interface IP.
    - type
        - str
    - default
        - 

##### mtu

???+ "Details"

    - description
        - Interface MTU.
    - type
        - int
    - default
        - 9216

##### disable_ip_redirects

???+ "Details"

    - description
        - Flag to enable/disable IP redirects.
    - type
        - bool
    - default
        - False

##### enable_hsrp

???+ "Details"

    - description
        - Flag to enable/disable HSRP on the interface.
    - type
        - bool
    - default
        - False

##### hsrp_vip

???+ "Details"

    - description
        - Virtual IP address for HSRP. This parameter is required if "enable_hsrp" is True.
    - type
        - str
    - default
        - 

##### hsrp_group

???+ "Details"

    - description
        - HSRP group. This parameter is required if "enable_hsrp" is True.
    - type
        - str
    - default
        - 

##### hsrp_priority

???+ "Details"

    - description
        - HSRP priority.
    - type
        - str
    - default
        - 

##### hsrp_vmac

???+ "Details"

    - description
        - HSRP virtual MAC.
    - type
        - str
    - default
        - 

##### dhcp_server_addr1

???+ "Details"

    - description
        - DHCP relay server address.
    - type
        - str
    - default
        - 

##### vrf_dhcp1

???+ "Details"

    - description
        - VRF to reach DHCP server. This parameter is required if "dhcp_server_addr1" is included.
    - type
        - str
    - default
        - 

##### dhcp_server_addr2

???+ "Details"

    - description
        - DHCP relay server address.
    - type
        - str
    - default
        - 

##### vrf_dhcp2

???+ "Details"

    - description
        - VRF to reach DHCP server. This parameter is required if "dhcp_server_addr2" is included.
    - type
        - str
    - default
        - 

##### dhcp_server_addr3

???+ "Details"

    - description
        - DHCP relay server address.
    - type
        - str
    - default
        - 

##### vrf_dhcp3

???+ "Details"

    - description
        - VRF to reach DHCP server. This parameter is required if "dhcp_server_addr3" is included.
    - type
        - str
    - default
        - 

##### adv_subnet_in_underlay

???+ "Details"

    - description
        - Flag to enable/disable advertisements of subnets into underlay.
    - type
        - bool
    - default
        - False

##### enable_netflow

???+ "Details"

    - description
        - Flag to enable netflow.
    - type
        - bool
    - default
        - False

##### netflow_monitor

???+ "Details"

    - description
        - Name of netflow monitor. This parameter is required if "enable_netflow" is True.
    - type
        - str
    - default
        - 

##### hsrp_version

???+ "Details"

    - description
        - HSRP protocol version.
    - type
        - int
    - default
        - 1
    - choices
        - 1
        - 2

##### preempt

???+ "Details"

    - description
        - Flag to enable/disable overthrow of low priority active routers. This parameter is valid only if "enable_hsrp" is True.
    - type
        - bool
    - default
        - False

#### profile_st_fex

???+ "Details"

    - description
        - Though the key shown here is 'profile_st_fex' the actual key to be used in playbook is 'profile'. The key 'profile_st_fex' is used here to logically segregate the interface objects applicable for this profile 
        - Object profile which must be included for straigth-through FEX interface configurations.

##### mode

???+ "Details"

    - description
        - Interface mode
    - choices
        - port_channel_st
    - type
        - str
    - required
        - True

##### mtu

???+ "Details"

    - description
        - Interface MTU.
    - type
        - str
    - choices
        - default
        - jumbo
    - default
        - jumbo

##### members

???+ "Details"

    - description
        - Member interfaces that are part of this FEX
    - type
        - list
    - elements
        - str
    - required
        - True

##### cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface
    - type
        - list
    - elements
        - str
    - default
        - []

##### description1

???+ "Details"

    - description
        - Description of the FEX interface
    - type
        - str
    - default
        - 

##### po_description

???+ "Details"

    - description
        - Description of the port-channel which is part of the FEX interface
    - type
        - str
    - default
        - 

##### admin_state

???+ "Details"

    - description
        - Administrative state of the interface
    - type
        - bool
    - default
        - True

##### enable_netflow

???+ "Details"

    - description
        - Flag to enable netflow.
    - type
        - bool
    - default
        - False

##### netflow_monitor

???+ "Details"

    - description
        - Name of netflow monitor. This parameter is required if "enable_netflow" is True.
    - type
        - str
    - default
        - 

#### profile_aa_fex

???+ "Details"

    - description
        - Though the key shown here is 'profile_aa_fex' the actual key to be used in playbook is 'profile'. The key 'profile_aa_fex' is used here to logically segregate the interface objects applicable for this profile 
        - Object profile which must be included for active-active FEX inetrface configurations.

##### description1

???+ "Details"

    - description
        - Description of the FEX interface
    - type
        - str
    - default
        - 

##### mode

???+ "Details"

    - description
        -  Interface mode
    - choices
        - port_channel_aa
    - type
        - str
    - required
        - True

##### peer1_members

???+ "Details"

    - description
        - Member interfaces that are part of this port channel on first peer
    - type
        - list
    - elements
        - str
    - required
        - True

##### peer2_members

???+ "Details"

    - description
        - Member interfaces that are part of this port channel on second peer
    - type
        - list
    - elements
        - str
    - required
        - True

##### mtu

???+ "Details"

    - description
        - Interface MTU
    - type
        - str
    - choices
        - default
        - jumbo
    - default
        - jumbo

##### peer1_cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface of first peer
    - type
        - list
    - elements
        - str
    - default
        - []

##### peer2_cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under this interface of second peer
    - type
        - list
    - elements
        - str
    - default
        - []

##### peer1_po_description

???+ "Details"

    - description
        - Description of the port-channel interface of first peer
    - type
        - str
    - default
        - 

##### peer2_po_description

???+ "Details"

    - description
        - Description of the port-channel interface of second peer
    - type
        - str
    - default
        - 

##### admin_state

???+ "Details"

    - description
        - Administrative state of the interface
    - type
        - bool
    - default
        - True

##### enable_netflow

???+ "Details"

    - description
        - Flag to enable netflow.
    - type
        - bool
    - default
        - False

##### netflow_monitor

???+ "Details"

    - description
        - Name of netflow monitor. This parameter is required if "enable_netflow" is True.
    - type
        - str
    - default
        - 
