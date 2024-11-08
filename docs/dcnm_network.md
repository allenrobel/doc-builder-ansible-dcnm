# dcnm_network

???+ "Details"

    - short_description
        - Add and remove Networks from a DCNM managed VXLAN fabric.
    - version_added
        - 0.9.0
    - description
        - "Add and remove Networks from a DCNM managed VXLAN fabric." 
        - "In Multisite fabrics, Networks can be created only on Multisite fabric"
    - author
        - Chris Van Heuveln(@chrisvanheuveln), Shrishail Kariyappanavar(@nkshrishail) Praveen Ramoorthy(@praveenramoorthy)


## options

???+ "Details"


### fabric

???+ "Details"

    - description
        - Name of the target fabric for network operations
    - type
        - str
    - required
        - True

### state

???+ "Details"

    - description
        - The state of DCNM after module completion.
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

### config

???+ "Details"

    - description
        - List of details of networks being managed. Not required for state deleted
    - type
        - list
    - elements
        - dict

#### net_name

???+ "Details"

    - description
        - Name of the network being managed
    - type
        - str
    - required
        - True

#### vrf_name

???+ "Details"

    - description
        - Name of the VRF to which the network belongs to 
        - This field is required for L3 Networks. VRF name should not be specified or may be specified as "" for L2 networks
    - type
        - str

#### net_id

???+ "Details"

    - description
        - ID of the network being managed 
        - If not specified in the playbook, DCNM will auto-select an available net_id
    - type
        - int
    - required
        - False

#### net_template

???+ "Details"

    - description
        - Name of the config template to be used
    - type
        - str
    - default
        - Default_Network_Universal

#### net_extension_template

???+ "Details"

    - description
        - Name of the extension config template to be used
    - type
        - str
    - default
        - Default_Network_Extension_Universal

#### vlan_id

???+ "Details"

    - description
        - VLAN ID for the network. 
        - If not specified in the playbook, DCNM will auto-select an available vlan_id
    - type
        - int
    - required
        - False

#### routing_tag

???+ "Details"

    - description
        - Routing Tag for the network profile
    - type
        - int
    - required
        - False
    - default
        - 12345

#### gw_ip_subnet

???+ "Details"

    - description
        - Gateway with subnet for the network
    - type
        - str
    - required
        - False

#### is_l2only

???+ "Details"

    - description
        - Layer 2 only network 
        - If specified as true, VRF Name(vrf_name) should not be specified or can be specified as ""
    - type
        - bool
    - required
        - False
    - default
        - False

#### vlan_name

???+ "Details"

    - description
        - Name of the vlan configured 
        - if > 32 chars enable, system vlan long-name on switch
    - type
        - str
    - required
        - False

#### int_desc

???+ "Details"

    - description
        - Description for the interface
    - type
        - str
    - required
        - False

#### mtu_l3intf

???+ "Details"

    - description
        - MTU for Layer 3 interfaces 
        - Configured MTU value should be in range 68-9216
    - type
        - int
    - required
        - False

#### arp_suppress

???+ "Details"

    - description
        - ARP suppression 
        - ARP suppression is only supported if SVI is present when Layer-2-Only is not enabled
    - type
        - bool
    - required
        - False
    - default
        - False

#### dhcp_srvr1_ip

???+ "Details"

    - description
        - DHCP relay IP address of the first DHCP server
    - type
        - str
    - required
        - False

#### dhcp_srvr1_vrf

???+ "Details"

    - description
        - VRF ID of first DHCP server
    - type
        - str
    - required
        - False

#### dhcp_srvr2_ip

???+ "Details"

    - description
        - DHCP relay IP address of the second DHCP server
    - type
        - str
    - required
        - False

#### dhcp_srvr2_vrf

???+ "Details"

    - description
        - VRF ID of second DHCP server
    - type
        - str
    - required
        - False

#### dhcp_srvr3_ip

???+ "Details"

    - description
        - DHCP relay IP address of the third DHCP server
    - type
        - str
    - required
        - False

#### dhcp_srvr3_vrf

???+ "Details"

    - description
        - VRF ID of third DHCP server
    - type
        - str
    - required
        - False

#### dhcp_loopback_id

???+ "Details"

    - description
        - Loopback ID for DHCP Relay interface 
        - Configured ID value should be in range 0-1023
    - type
        - int
    - required
        - False

#### multicast_group_address

???+ "Details"

    - description
        - The multicast IP address for the network
    - type
        - str
    - required
        - False

#### gw_ipv6_subnet

???+ "Details"

    - description
        - IPv6 Gateway with prefix for the network
    - type
        - str
    - required
        - False

#### secondary_ip_gw1

???+ "Details"

    - description
        - IP address with subnet for secondary gateway 1
    - type
        - str
    - required
        - False

#### secondary_ip_gw2

???+ "Details"

    - description
        - IP address with subnet for secondary gateway 2
    - type
        - str
    - required
        - False

#### secondary_ip_gw3

???+ "Details"

    - description
        - IP address with subnet for secondary gateway 3
    - type
        - str
    - required
        - False

#### secondary_ip_gw4

???+ "Details"

    - description
        - IP address with subnet for secondary gateway 4
    - type
        - str
    - required
        - False

#### trm_enable

???+ "Details"

    - description
        - Enable Tenant Routed Multicast
    - type
        - bool
    - required
        - False
    - default
        - False

#### route_target_both

???+ "Details"

    - description
        - Enable both L2 VNI Route-Target
    - type
        - bool
    - required
        - False
    - default
        - False

#### l3gw_on_border

???+ "Details"

    - description
        - Enable L3 Gateway on Border
    - type
        - bool
    - required
        - False
    - default
        - False

#### netflow_enable

???+ "Details"

    - description
        - Enable Netflow 
        - Netflow is supported only if it is enabled on fabric 
        - Netflow configs are supported on NDFC only
    - type
        - bool
    - required
        - False
    - default
        - False

#### intfvlan_nf_monitor

???+ "Details"

    - description
        - Interface Vlan Netflow Monitor 
        - Applicable only if 'Layer 2 Only' is not enabled. Provide monitor name defined in fabric setting for Layer 3 Record 
        - Netflow configs are supported on NDFC only
    - type
        - str
    - required
        - False

#### vlan_nf_monitor

???+ "Details"

    - description
        - Vlan Netflow Monitor 
        - Provide monitor name defined in fabric setting for Layer 3 Record 
        - Netflow configs are supported on NDFC only
    - type
        - str
    - required
        - False

#### attach

???+ "Details"

    - description
        - List of network attachment details
    - type
        - list
    - elements
        - dict

##### ip_address

???+ "Details"

    - description
        - IP address of the switch where the network will be attached or detached
    - type
        - str
    - required
        - True

##### ports

???+ "Details"

    - description
        - List of switch interfaces where the network will be attached
    - type
        - list
    - elements
        - str
    - required
        - True

##### deploy

???+ "Details"

    - description
        - Per switch knob to control whether to deploy the attachment 
        - This knob has been deprecated from Ansible NDFC Collection Version 2.1.0 onwards. There will not be any functional impact if specified in playbook.
    - type
        - bool
    - default
        - True

##### tor_ports

???+ "Details"

    - description
        - List of interfaces in the paired TOR switch for this leaf where the network will be attached 
        - Please attach the same set of TOR ports to both the VPC paired switches.
    - type
        - list
    - elements
        - dict
    - required
        - False

###### ip_address

???+ "Details"

    - description
        - IP address of the TOR switch where the network will be attached
    - type
        - str
    - required
        - True

###### ports

???+ "Details"

    - description
        - List of TOR switch interfaces where the network will be attached
    - type
        - list
    - elements
        - str
    - required
        - True

#### deploy

???+ "Details"

    - description
        - Global knob to control whether to deploy the attachment 
        - Ansible NDFC Collection Behavior for Version 2.0.1 and earlier 
        - This knob will create and deploy the attachment in DCNM only when set to "True" in playbook 
        - Ansible NDFC Collection Behavior for Version 2.1.0 and later 
        - Attachments specified in the playbook will always be created in DCNM. This knob, when set to "True",  will deploy the attachment in DCNM, by pushing the configs to switch. If set to "False", the attachments will be created in DCNM, but will not be deployed
    - type
        - bool
    - default
        - True
