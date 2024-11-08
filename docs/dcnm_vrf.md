# dcnm_vrf

???+ "Details"

    - short_description
        - Add and remove VRFs from a DCNM managed VXLAN fabric.
    - version_added
        - 0.9.0
    - description
        - "Add and remove VRFs and VRF Lite Extension from a DCNM managed VXLAN fabric." 
        - "In Multisite fabrics, VRFs can be created only on Multisite fabric" 
        - "In Multisite fabrics, VRFs cannot be created on member fabric"
    - author
        - Shrishail Kariyappanavar(@nkshrishail), Karthik Babu Harichandra Babu (@kharicha), Praveen Ramoorthy(@praveenramoorthy)


## options

???+ "Details"


### fabric

???+ "Details"

    - description
        - Name of the target fabric for vrf operations
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
        - List of details of vrfs being managed. Not required for state deleted
    - type
        - list
    - elements
        - dict

#### vrf_name

???+ "Details"

    - description
        - Name of the vrf being managed
    - type
        - str
    - required
        - True

#### vrf_id

???+ "Details"

    - description
        - ID of the vrf being managed
    - type
        - int
    - required
        - False

#### vlan_id

???+ "Details"

    - description
        - vlan ID for the vrf attachment 
        - If not specified in the playbook, DCNM will auto-select an available vlan_id
    - type
        - int
    - required
        - False

#### vrf_template

???+ "Details"

    - description
        - Name of the config template to be used
    - type
        - str
    - default
        - Default_VRF_Universal

#### vrf_extension_template

???+ "Details"

    - description
        - Name of the extension config template to be used
    - type
        - str
    - default
        - Default_VRF_Extension_Universal

#### service_vrf_template

???+ "Details"

    - description
        - Service vrf template
    - type
        - str
    - default
        - None

#### vrf_vlan_name

???+ "Details"

    - description
        - VRF Vlan Name 
        - if > 32 chars enable 
        - system vlan long-name
    - type
        - str
    - required
        - False

#### vrf_intf_desc

???+ "Details"

    - description
        - VRF Intf Description
    - type
        - str
    - required
        - False

#### vrf_description

???+ "Details"

    - description
        - VRF Description
    - type
        - str
    - required
        - False

#### vrf_int_mtu

???+ "Details"

    - description
        - VRF interface MTU
    - type
        - int
    - required
        - False
    - default
        - 9216

#### loopback_route_tag

???+ "Details"

    - description
        - Loopback Routing Tag
    - type
        - int
    - required
        - False
    - default
        - 12345

#### redist_direct_rmap

???+ "Details"

    - description
        - Redistribute Direct Route Map
    - type
        - str
    - required
        - False
    - default
        - FABRIC-RMAP-REDIST-SUBNET

#### max_bgp_paths

???+ "Details"

    - description
        - Max BGP Paths
    - type
        - int
    - required
        - False
    - default
        - 1

#### max_ibgp_paths

???+ "Details"

    - description
        - Max iBGP Paths
    - type
        - int
    - required
        - False
    - default
        - 2

#### ipv6_linklocal_enable

???+ "Details"

    - description
        - Enable IPv6 link-local Option
    - type
        - bool
    - required
        - False
    - default
        - True

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

#### no_rp

???+ "Details"

    - description
        - No RP, only SSM is used 
        - supported on NDFC only
    - type
        - bool
    - required
        - False
    - default
        - False

#### rp_external

???+ "Details"

    - description
        - Specifies if RP is external to the fabric 
        - Can be configured only when TRM is enabled
    - type
        - bool
    - required
        - False
    - default
        - False

#### rp_address

???+ "Details"

    - description
        - IPv4 Address of RP 
        - Can be configured only when TRM is enabled
    - type
        - str
    - required
        - False

#### rp_loopback_id

???+ "Details"

    - description
        - loopback ID of RP 
        - Can be configured only when TRM is enabled
    - type
        - int
    - required
        - False

#### underlay_mcast_ip

???+ "Details"

    - description
        - Underlay IPv4 Multicast Address 
        - Can be configured only when TRM is enabled
    - type
        - str
    - required
        - False

#### overlay_mcast_group

???+ "Details"

    - description
        - Underlay IPv4 Multicast group (224.0.0.0/4 to 239.255.255.255/4) 
        - Can be configured only when TRM is enabled
    - type
        - str
    - required
        - False

#### trm_bgw_msite

???+ "Details"

    - description
        - Enable TRM on Border Gateway Multisite 
        - Can be configured only when TRM is enabled
    - type
        - bool
    - required
        - False
    - default
        - False

#### adv_host_routes

???+ "Details"

    - description
        - Flag to Control Advertisement of /32 and /128 Routes to Edge Routers
    - type
        - bool
    - required
        - False
    - default
        - False

#### adv_default_routes

???+ "Details"

    - description
        - Flag to Control Advertisement of Default Route Internally
    - type
        - bool
    - required
        - False
    - default
        - True

#### static_default_route

???+ "Details"

    - description
        - Flag to Control Static Default Route Configuration
    - type
        - bool
    - required
        - False
    - default
        - True

#### bgp_password

???+ "Details"

    - description
        - VRF Lite BGP neighbor password 
        - Password should be in Hex string format
    - type
        - str
    - required
        - False

#### bgp_passwd_encrypt

???+ "Details"

    - description
        - VRF Lite BGP Key Encryption Type 
        - Allowed values are 3 (3DES) and 7 (Cisco)
    - type
        - int
    - choices
        - 3
        - 7
    - required
        - False
    - default
        - 3

#### netflow_enable

???+ "Details"

    - description
        - Enable netflow on VRF-LITE Sub-interface 
        - Netflow is supported only if it is enabled on fabric 
        - Netflow configs are supported on NDFC only
    - type
        - bool
    - required
        - False
    - default
        - False

#### nf_monitor

???+ "Details"

    - description
        - Netflow Monitor 
        - Netflow configs are supported on NDFC only
    - type
        - str
    - required
        - False

#### disable_rt_auto

???+ "Details"

    - description
        - Disable RT Auto-Generate 
        - supported on NDFC only
    - type
        - bool
    - required
        - False
    - default
        - False

#### import_vpn_rt

???+ "Details"

    - description
        - VPN routes to import 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - type
        - str
    - required
        - False

#### export_vpn_rt

???+ "Details"

    - description
        - VPN routes to export 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - type
        - str
    - required
        - False

#### import_evpn_rt

???+ "Details"

    - description
        - EVPN routes to import 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - type
        - str
    - required
        - False

#### export_evpn_rt

???+ "Details"

    - description
        - EVPN routes to export 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - type
        - str
    - required
        - False

#### import_mvpn_rt

???+ "Details"

    - description
        - MVPN routes to import 
        - supported on NDFC only 
        - Can be configured only when TRM is enabled 
        - Use ',' to separate multiple route-targets
    - type
        - str
    - required
        - False

#### export_mvpn_rt

???+ "Details"

    - description
        - MVPN routes to export 
        - supported on NDFC only 
        - Can be configured only when TRM is enabled 
        - Use ',' to separate multiple route-targets
    - type
        - str
    - required
        - False

#### attach

???+ "Details"

    - description
        - List of vrf attachment details
    - type
        - list
    - elements
        - dict

##### ip_address

???+ "Details"

    - description
        - IP address of the switch where vrf will be attached or detached
    - type
        - str
    - required
        - True

###### vrf_lite

???+ "Details"

    - type
        - list
    - description
        - VRF Lite Extensions options
    - elements
        - dict
    - required
        - False

####### peer_vrf

???+ "Details"

    - description
        - VRF Name to which this extension is attached
    - type
        - str
    - required
        - False

####### interface

???+ "Details"

    - description
        - Interface of the switch which is connected to the edge router
    - type
        - str
    - required
        - True

####### ipv4_addr

???+ "Details"

    - description
        - IP address of the interface which is connected to the edge router
    - type
        - str
    - required
        - False

####### neighbor_ipv4

???+ "Details"

    - description
        - Neighbor IP address of the edge router
    - type
        - str
    - required
        - False

####### ipv6_addr

???+ "Details"

    - description
        - IPv6 address of the interface which is connected to the edge router
    - type
        - str
    - required
        - False

####### neighbor_ipv6

???+ "Details"

    - description
        - Neighbor IPv6 address of the edge router
    - type
        - str
    - required
        - False

####### dot1q

???+ "Details"

    - description
        - DOT1Q Id
    - type
        - str
    - required
        - False

##### import_evpn_rt

???+ "Details"

    - description
        - import evpn route-target 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - type
        - str
    - required
        - False

##### export_evpn_rt

???+ "Details"

    - description
        - export evpn route-target 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - type
        - str
    - required
        - False

##### deploy

???+ "Details"

    - description
        - Per switch knob to control whether to deploy the attachment 
        - This knob has been deprecated from Ansible NDFC Collection Version 2.1.0 onwards. There will not be any functional impact if specified in playbook.
    - type
        - bool
    - default
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
