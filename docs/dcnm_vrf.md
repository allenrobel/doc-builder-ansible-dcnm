# dcnm_vrf

???+ "Details"

    - author
        - Shrishail Kariyappanavar(@nkshrishail), Karthik Babu Harichandra Babu (@kharicha), Praveen Ramoorthy(@praveenramoorthy)
    - description
        - Add and remove VRFs and VRF Lite Extension from a DCNM managed VXLAN fabric. 
        - In Multisite fabrics, VRFs can be created only on Multisite fabric 
        - In Multisite fabrics, VRFs cannot be created on member fabric
    - short_description
        - Add and remove VRFs from a DCNM managed VXLAN fabric.
    - version_added
        - 0.9.0


## options

???+ "Details"


### config

???+ "Details"

    - description
        - List of details of vrfs being managed. Not required for state deleted
    - elements
        - dict

#### adv_default_routes

???+ "Details"

    - default
        - True
    - description
        - Flag to Control Advertisement of Default Route Internally
    - required
        - False
    - type
        - bool

#### adv_host_routes

???+ "Details"

    - default
        - False
    - description
        - Flag to Control Advertisement of /32 and /128 Routes to Edge Routers
    - required
        - False
    - type
        - bool

#### attach

???+ "Details"

    - description
        - List of vrf attachment details
    - elements
        - dict

##### deploy

???+ "Details"

    - default
        - True
    - description
        - Per switch knob to control whether to deploy the attachment 
        - This knob has been deprecated from Ansible NDFC Collection Version 2.1.0 onwards. There will not be any functional impact if specified in playbook.
    - type
        - bool

##### export_evpn_rt

???+ "Details"

    - description
        - export evpn route-target 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - required
        - False
    - type
        - str

##### import_evpn_rt

???+ "Details"

    - description
        - import evpn route-target 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - required
        - False
    - type
        - str

##### ip_address

???+ "Details"

    - description
        - IP address of the switch where vrf will be attached or detached
    - required
        - True

###### vrf_lite

???+ "Details"

    - description
        - VRF Lite Extensions options
    - elements
        - dict
    - required
        - False

####### dot1q

???+ "Details"

    - description
        - DOT1Q Id
    - required
        - False
    - type
        - str

####### interface

???+ "Details"

    - description
        - Interface of the switch which is connected to the edge router
    - required
        - True
    - type
        - str

####### ipv4_addr

???+ "Details"

    - description
        - IP address of the interface which is connected to the edge router
    - required
        - False
    - type
        - str

####### ipv6_addr

???+ "Details"

    - description
        - IPv6 address of the interface which is connected to the edge router
    - required
        - False
    - type
        - str

####### neighbor_ipv4

???+ "Details"

    - description
        - Neighbor IP address of the edge router
    - required
        - False
    - type
        - str

####### neighbor_ipv6

???+ "Details"

    - description
        - Neighbor IPv6 address of the edge router
    - required
        - False
    - type
        - str

####### peer_vrf

???+ "Details"

    - description
        - VRF Name to which this extension is attached
    - required
        - False
    - type
        - str
    - type
        - list
    - type
        - str
    - type
        - list

#### bgp_passwd_encrypt

???+ "Details"

    - choices
        - 3
        - 7
    - default
        - 3
    - description
        - VRF Lite BGP Key Encryption Type 
        - Allowed values are 3 (3DES) and 7 (Cisco)
    - required
        - False
    - type
        - int

#### bgp_password

???+ "Details"

    - description
        - VRF Lite BGP neighbor password 
        - Password should be in Hex string format
    - required
        - False
    - type
        - str

#### deploy

???+ "Details"

    - default
        - True
    - description
        - Global knob to control whether to deploy the attachment 
        - Ansible NDFC Collection Behavior for Version 2.0.1 and earlier 
        - This knob will create and deploy the attachment in DCNM only when set to "True" in playbook 
        - Ansible NDFC Collection Behavior for Version 2.1.0 and later 
        - Attachments specified in the playbook will always be created in DCNM. This knob, when set to "True",  will deploy the attachment in DCNM, by pushing the configs to switch. If set to "False", the attachments will be created in DCNM, but will not be deployed
    - type
        - bool

#### disable_rt_auto

???+ "Details"

    - default
        - False
    - description
        - Disable RT Auto-Generate 
        - supported on NDFC only
    - required
        - False
    - type
        - bool

#### export_evpn_rt

???+ "Details"

    - description
        - EVPN routes to export 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - required
        - False
    - type
        - str

#### export_mvpn_rt

???+ "Details"

    - description
        - MVPN routes to export 
        - supported on NDFC only 
        - Can be configured only when TRM is enabled 
        - Use ',' to separate multiple route-targets
    - required
        - False
    - type
        - str

#### export_vpn_rt

???+ "Details"

    - description
        - VPN routes to export 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - required
        - False
    - type
        - str

#### import_evpn_rt

???+ "Details"

    - description
        - EVPN routes to import 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - required
        - False
    - type
        - str

#### import_mvpn_rt

???+ "Details"

    - description
        - MVPN routes to import 
        - supported on NDFC only 
        - Can be configured only when TRM is enabled 
        - Use ',' to separate multiple route-targets
    - required
        - False
    - type
        - str

#### import_vpn_rt

???+ "Details"

    - description
        - VPN routes to import 
        - supported on NDFC only 
        - Use ',' to separate multiple route-targets
    - required
        - False
    - type
        - str

#### ipv6_linklocal_enable

???+ "Details"

    - default
        - True
    - description
        - Enable IPv6 link-local Option
    - required
        - False
    - type
        - bool

#### loopback_route_tag

???+ "Details"

    - default
        - 12345
    - description
        - Loopback Routing Tag
    - required
        - False
    - type
        - int

#### max_bgp_paths

???+ "Details"

    - default
        - 1
    - description
        - Max BGP Paths
    - required
        - False
    - type
        - int

#### max_ibgp_paths

???+ "Details"

    - default
        - 2
    - description
        - Max iBGP Paths
    - required
        - False
    - type
        - int

#### netflow_enable

???+ "Details"

    - default
        - False
    - description
        - Enable netflow on VRF-LITE Sub-interface 
        - Netflow is supported only if it is enabled on fabric 
        - Netflow configs are supported on NDFC only
    - required
        - False
    - type
        - bool

#### nf_monitor

???+ "Details"

    - description
        - Netflow Monitor 
        - Netflow configs are supported on NDFC only
    - required
        - False
    - type
        - str

#### no_rp

???+ "Details"

    - default
        - False
    - description
        - No RP, only SSM is used 
        - supported on NDFC only
    - required
        - False
    - type
        - bool

#### overlay_mcast_group

???+ "Details"

    - description
        - Underlay IPv4 Multicast group (224.0.0.0/4 to 239.255.255.255/4) 
        - Can be configured only when TRM is enabled
    - required
        - False
    - type
        - str

#### redist_direct_rmap

???+ "Details"

    - default
        - FABRIC-RMAP-REDIST-SUBNET
    - description
        - Redistribute Direct Route Map
    - required
        - False
    - type
        - str

#### rp_address

???+ "Details"

    - description
        - IPv4 Address of RP 
        - Can be configured only when TRM is enabled
    - required
        - False
    - type
        - str

#### rp_external

???+ "Details"

    - default
        - False
    - description
        - Specifies if RP is external to the fabric 
        - Can be configured only when TRM is enabled
    - required
        - False
    - type
        - bool

#### rp_loopback_id

???+ "Details"

    - description
        - loopback ID of RP 
        - Can be configured only when TRM is enabled
    - required
        - False
    - type
        - int

#### service_vrf_template

???+ "Details"

    - default
        - None
    - description
        - Service vrf template
    - type
        - str

#### static_default_route

???+ "Details"

    - default
        - True
    - description
        - Flag to Control Static Default Route Configuration
    - required
        - False
    - type
        - bool

#### trm_bgw_msite

???+ "Details"

    - default
        - False
    - description
        - Enable TRM on Border Gateway Multisite 
        - Can be configured only when TRM is enabled
    - required
        - False
    - type
        - bool

#### trm_enable

???+ "Details"

    - default
        - False
    - description
        - Enable Tenant Routed Multicast
    - required
        - False
    - type
        - bool

#### underlay_mcast_ip

???+ "Details"

    - description
        - Underlay IPv4 Multicast Address 
        - Can be configured only when TRM is enabled
    - required
        - False
    - type
        - str

#### vlan_id

???+ "Details"

    - description
        - vlan ID for the vrf attachment 
        - If not specified in the playbook, DCNM will auto-select an available vlan_id
    - required
        - False
    - type
        - int

#### vrf_description

???+ "Details"

    - description
        - VRF Description
    - required
        - False
    - type
        - str

#### vrf_extension_template

???+ "Details"

    - default
        - Default_VRF_Extension_Universal
    - description
        - Name of the extension config template to be used
    - type
        - str

#### vrf_id

???+ "Details"

    - description
        - ID of the vrf being managed
    - required
        - False
    - type
        - int

#### vrf_int_mtu

???+ "Details"

    - default
        - 9216
    - description
        - VRF interface MTU
    - required
        - False
    - type
        - int

#### vrf_intf_desc

???+ "Details"

    - description
        - VRF Intf Description
    - required
        - False
    - type
        - str

#### vrf_name

???+ "Details"

    - description
        - Name of the vrf being managed
    - required
        - True
    - type
        - str

#### vrf_template

???+ "Details"

    - default
        - Default_VRF_Universal
    - description
        - Name of the config template to be used
    - type
        - str

#### vrf_vlan_name

???+ "Details"

    - description
        - VRF Vlan Name 
        - if > 32 chars enable 
        - system vlan long-name
    - required
        - False
    - type
        - str
    - type
        - list

### fabric

???+ "Details"

    - description
        - Name of the target fabric for vrf operations
    - required
        - True
    - type
        - str

### state

???+ "Details"

    - choices
        - merged
        - replaced
        - overridden
        - deleted
        - query
    - default
        - merged
    - description
        - The state of DCNM after module completion.
    - type
        - str

## Examples

???+ "Details"

``` yaml
---
# This module supports the following states:
#
# Merged:
#   VRFs defined in the playbook will be merged into the target fabric.
#     - If the VRF does not exist it will be added.
#     - If the VRF exists but properties managed by the playbook are different
#       they will be updated if possible.
#     - VRFs that are not specified in the playbook will be untouched.
#
# Replaced:
#   VRFs defined in the playbook will be replaced in the target fabric.
#     - If the VRF does not exist it will be added.
#     - If the VRF exists but properties managed by the playbook are different
#       they will be updated if possible.
#     - Properties that can be managed by the module but are  not specified
#       in the playbook will be deleted or defaulted if possible.
#     - VRFs that are not specified in the playbook will be untouched.
#
# Overridden:
#   VRFs defined in the playbook will be overridden in the target fabric.
#     - If the VRF does not exist it will be added.
#     - If the VRF exists but properties managed by the playbook are different
#       they will be updated if possible.
#     - Properties that can be managed by the module but are not specified
#       in the playbook will be deleted or defaulted if possible.
#     - VRFs that are not specified in the playbook will be deleted.
#
# Deleted:
#   VRFs defined in the playbook will be deleted.
#   If no VRFs are provided in the playbook, all VRFs present on that DCNM fabric will be deleted.
#
# Query:
#   Returns the current DCNM state for the VRFs listed in the playbook.
#
# rollback functionality:
# This module supports task level rollback functionality. If any task runs into failures, as part of failure
# handling, the module tries to bring the state of the DCNM back to the state captured in have structure at the
# beginning of the task execution. Following few lines provide a logical description of how this works,
# if (failure)
#     want data = have data
#     have data = get state of DCNM
#     Run the module in override state with above set of data to produce the required set of diffs
#     and push the diff payloads to DCNM.
# If rollback fails, the module does not attempt to rollback again, it just quits with appropriate error messages.

# The two VRFs below will be merged into the target fabric.
- name: Merge vrfs
  cisco.dcnm.dcnm_vrf:
    fabric: vxlan-fabric
    state: merged
    config:
    - vrf_name: ansible-vrf-r1
      vrf_id: 9008011
      vrf_template: Default_VRF_Universal
      vrf_extension_template: Default_VRF_Extension_Universal
      vlan_id: 2000
      service_vrf_template: null
      attach:
      - ip_address: 192.168.1.224
      - ip_address: 192.168.1.225
    - vrf_name: ansible-vrf-r2
      vrf_id: 9008012
      vrf_template: Default_VRF_Universal
      vrf_extension_template: Default_VRF_Extension_Universal
      service_vrf_template: null
      attach:
      - ip_address: 192.168.1.224
      - ip_address: 192.168.1.225

# VRF LITE Extension attached
- name: Merge vrfs
  cisco.dcnm.dcnm_vrf:
    fabric: vxlan-fabric
    state: merged
    config:
    - vrf_name: ansible-vrf-r1
      vrf_id: 9008011
      vrf_template: Default_VRF_Universal
      vrf_extension_template: Default_VRF_Extension_Universal
      vlan_id: 2000
      service_vrf_template: null
      attach:
      - ip_address: 192.168.1.224
      - ip_address: 192.168.1.225
        vrf_lite:
          - peer_vrf: test_vrf_1 # optional
            interface: Ethernet1/16 # mandatory
            ipv4_addr: 10.33.0.2/30 # optional
            neighbor_ipv4: 10.33.0.1 # optional
            ipv6_addr: 2010::10:34:0:7/64 # optional
            neighbor_ipv6: 2010::10:34:0:3 # optional
            dot1q: 2 # dot1q can be got from dcnm/optional
          - peer_vrf: test_vrf_2 # optional
            interface: Ethernet1/17 # mandatory
            ipv4_addr: 20.33.0.2/30 # optional
            neighbor_ipv4: 20.33.0.1 # optional
            ipv6_addr: 3010::10:34:0:7/64 # optional
            neighbor_ipv6: 3010::10:34:0:3 # optional
            dot1q: 3 # dot1q can be got from dcnm/optional

# The two VRFs below will be replaced in the target fabric.
- name: Replace vrfs
  cisco.dcnm.dcnm_vrf:
    fabric: vxlan-fabric
    state: replaced
    config:
    - vrf_name: ansible-vrf-r1
      vrf_id: 9008011
      vrf_template: Default_VRF_Universal
      vrf_extension_template: Default_VRF_Extension_Universal
      vlan_id: 2000
      service_vrf_template: null
      attach:
      - ip_address: 192.168.1.224
      # Delete this attachment
      # - ip_address: 192.168.1.225
      # Create the following attachment
      - ip_address: 192.168.1.226
    # Dont touch this if its present on DCNM
    # - vrf_name: ansible-vrf-r2
    #   vrf_id: 9008012
    #   vrf_template: Default_VRF_Universal
    #   vrf_extension_template: Default_VRF_Extension_Universal
    #   attach:
    #   - ip_address: 192.168.1.224
    #   - ip_address: 192.168.1.225

# The two VRFs below will be overridden in the target fabric.
- name: Override vrfs
  cisco.dcnm.dcnm_vrf:
    fabric: vxlan-fabric
    state: overridden
    config:
    - vrf_name: ansible-vrf-r1
      vrf_id: 9008011
      vrf_template: Default_VRF_Universal
      vrf_extension_template: Default_VRF_Extension_Universal
      vlan_id: 2000
      service_vrf_template: null
      attach:
      - ip_address: 192.168.1.224
      # Delete this attachment
      # - ip_address: 192.168.1.225
      # Create the following attachment
      - ip_address: 192.168.1.226
    # Delete this vrf
    # - vrf_name: ansible-vrf-r2
    #   vrf_id: 9008012
    #   vrf_template: Default_VRF_Universal
    #   vrf_extension_template: Default_VRF_Extension_Universal
    #   vlan_id: 2000
    #   service_vrf_template: null
    #   attach:
    #   - ip_address: 192.168.1.224
    #   - ip_address: 192.168.1.225

- name: Delete selected vrfs
  cisco.dcnm.dcnm_vrf:
    fabric: vxlan-fabric
    state: deleted
    config:
    - vrf_name: ansible-vrf-r1
      vrf_id: 9008011
      vrf_template: Default_VRF_Universal
      vrf_extension_template: Default_VRF_Extension_Universal
      vlan_id: 2000
      service_vrf_template: null
    - vrf_name: ansible-vrf-r2
      vrf_id: 9008012
      vrf_template: Default_VRF_Universal
      vrf_extension_template: Default_VRF_Extension_Universal
      vlan_id: 2000
      service_vrf_template: null

- name: Delete all the vrfs
  cisco.dcnm.dcnm_vrf:
    fabric: vxlan-fabric
    state: deleted

- name: Query vrfs
  cisco.dcnm.dcnm_vrf:
    fabric: vxlan-fabric
    state: query
    config:
    - vrf_name: ansible-vrf-r1
    - vrf_name: ansible-vrf-r2
```
