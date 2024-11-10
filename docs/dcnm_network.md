# dcnm_network

???+ "Details"

    - author
        - Chris Van Heuveln(@chrisvanheuveln), Shrishail Kariyappanavar(@nkshrishail) Praveen Ramoorthy(@praveenramoorthy)
    - description
        - Add and remove Networks from a DCNM managed VXLAN fabric. 
        - In Multisite fabrics, Networks can be created only on Multisite fabric
    - short_description
        - Add and remove Networks from a DCNM managed VXLAN fabric.
    - version_added
        - 0.9.0


## options

???+ "Details"


### config

???+ "Details"

    - description
        - List of details of networks being managed. Not required for state deleted
    - elements
        - dict

#### arp_suppress

???+ "Details"

    - default
        - False
    - description
        - ARP suppression 
        - ARP suppression is only supported if SVI is present when Layer-2-Only is not enabled
    - required
        - False
    - type
        - bool

#### attach

???+ "Details"

    - description
        - List of network attachment details
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

##### ip_address

???+ "Details"

    - description
        - IP address of the switch where the network will be attached or detached
    - required
        - True
    - type
        - str

##### ports

???+ "Details"

    - description
        - List of switch interfaces where the network will be attached
    - elements
        - str
    - required
        - True
    - type
        - list

##### tor_ports

???+ "Details"

    - description
        - List of interfaces in the paired TOR switch for this leaf where the network will be attached 
        - Please attach the same set of TOR ports to both the VPC paired switches.
    - elements
        - dict
    - required
        - False

###### ip_address

???+ "Details"

    - description
        - IP address of the TOR switch where the network will be attached
    - required
        - True
    - type
        - str

###### ports

???+ "Details"

    - description
        - List of TOR switch interfaces where the network will be attached
    - elements
        - str
    - required
        - True
    - type
        - list
    - type
        - list
    - type
        - list

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

#### dhcp_loopback_id

???+ "Details"

    - description
        - Loopback ID for DHCP Relay interface 
        - Configured ID value should be in range 0-1023
    - required
        - False
    - type
        - int

#### dhcp_srvr1_ip

???+ "Details"

    - description
        - DHCP relay IP address of the first DHCP server
    - required
        - False
    - type
        - str

#### dhcp_srvr1_vrf

???+ "Details"

    - description
        - VRF ID of first DHCP server
    - required
        - False
    - type
        - str

#### dhcp_srvr2_ip

???+ "Details"

    - description
        - DHCP relay IP address of the second DHCP server
    - required
        - False
    - type
        - str

#### dhcp_srvr2_vrf

???+ "Details"

    - description
        - VRF ID of second DHCP server
    - required
        - False
    - type
        - str

#### dhcp_srvr3_ip

???+ "Details"

    - description
        - DHCP relay IP address of the third DHCP server
    - required
        - False
    - type
        - str

#### dhcp_srvr3_vrf

???+ "Details"

    - description
        - VRF ID of third DHCP server
    - required
        - False
    - type
        - str

#### gw_ip_subnet

???+ "Details"

    - description
        - Gateway with subnet for the network
    - required
        - False
    - type
        - str

#### gw_ipv6_subnet

???+ "Details"

    - description
        - IPv6 Gateway with prefix for the network
    - required
        - False
    - type
        - str

#### int_desc

???+ "Details"

    - description
        - Description for the interface
    - required
        - False
    - type
        - str

#### intfvlan_nf_monitor

???+ "Details"

    - description
        - Interface Vlan Netflow Monitor 
        - Applicable only if 'Layer 2 Only' is not enabled. Provide monitor name defined in fabric setting for Layer 3 Record 
        - Netflow configs are supported on NDFC only
    - required
        - False
    - type
        - str

#### is_l2only

???+ "Details"

    - default
        - False
    - description
        - Layer 2 only network 
        - If specified as true, VRF Name(vrf_name) should not be specified or can be specified as ""
    - required
        - False
    - type
        - bool

#### l3gw_on_border

???+ "Details"

    - default
        - False
    - description
        - Enable L3 Gateway on Border
    - required
        - False
    - type
        - bool

#### mtu_l3intf

???+ "Details"

    - description
        - MTU for Layer 3 interfaces 
        - Configured MTU value should be in range 68-9216
    - required
        - False
    - type
        - int

#### multicast_group_address

???+ "Details"

    - description
        - The multicast IP address for the network
    - required
        - False
    - type
        - str

#### net_extension_template

???+ "Details"

    - default
        - Default_Network_Extension_Universal
    - description
        - Name of the extension config template to be used
    - type
        - str

#### net_id

???+ "Details"

    - description
        - ID of the network being managed 
        - If not specified in the playbook, DCNM will auto-select an available net_id
    - required
        - False
    - type
        - int

#### net_name

???+ "Details"

    - description
        - Name of the network being managed
    - required
        - True
    - type
        - str

#### net_template

???+ "Details"

    - default
        - Default_Network_Universal
    - description
        - Name of the config template to be used
    - type
        - str

#### netflow_enable

???+ "Details"

    - default
        - False
    - description
        - Enable Netflow 
        - Netflow is supported only if it is enabled on fabric 
        - Netflow configs are supported on NDFC only
    - required
        - False
    - type
        - bool

#### route_target_both

???+ "Details"

    - default
        - False
    - description
        - Enable both L2 VNI Route-Target
    - required
        - False
    - type
        - bool

#### routing_tag

???+ "Details"

    - default
        - 12345
    - description
        - Routing Tag for the network profile
    - required
        - False
    - type
        - int

#### secondary_ip_gw1

???+ "Details"

    - description
        - IP address with subnet for secondary gateway 1
    - required
        - False
    - type
        - str

#### secondary_ip_gw2

???+ "Details"

    - description
        - IP address with subnet for secondary gateway 2
    - required
        - False
    - type
        - str

#### secondary_ip_gw3

???+ "Details"

    - description
        - IP address with subnet for secondary gateway 3
    - required
        - False
    - type
        - str

#### secondary_ip_gw4

???+ "Details"

    - description
        - IP address with subnet for secondary gateway 4
    - required
        - False
    - type
        - str

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

#### vlan_id

???+ "Details"

    - description
        - VLAN ID for the network. 
        - If not specified in the playbook, DCNM will auto-select an available vlan_id
    - required
        - False
    - type
        - int

#### vlan_name

???+ "Details"

    - description
        - Name of the vlan configured 
        - if > 32 chars enable, system vlan long-name on switch
    - required
        - False
    - type
        - str

#### vlan_nf_monitor

???+ "Details"

    - description
        - Vlan Netflow Monitor 
        - Provide monitor name defined in fabric setting for Layer 3 Record 
        - Netflow configs are supported on NDFC only
    - required
        - False
    - type
        - str

#### vrf_name

???+ "Details"

    - description
        - Name of the VRF to which the network belongs to 
        - This field is required for L3 Networks. VRF name should not be specified or may be specified as "" for L2 networks
    - type
        - str
    - type
        - list

### fabric

???+ "Details"

    - description
        - Name of the target fabric for network operations
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
#   Networks defined in the playbook will be merged into the target fabric.
#     - If the network does not exist it will be added.
#     - If the network exists but properties managed by the playbook are different
#       they will be updated if possible.
#     - Networks that are not specified in the playbook will be untouched.
#
# Replaced:
#   Networks defined in the playbook will be replaced in the target fabric.
#     - If the Networks does not exist it will be added.
#     - If the Networks exists but properties managed by the playbook are different
#       they will be updated if possible.
#     - Properties that can be managed by the module but are not specified
#       in the playbook will be deleted or defaulted if possible.
#     - Networks that are not specified in the playbook will be untouched.
#
# Overridden:
#   Networks defined in the playbook will be overridden in the target fabric.
#     - If the Networks does not exist it will be added.
#     - If the Networks exists but properties managed by the playbook are different
#       they will be updated if possible.
#     - Properties that can be managed by the module but are not specified
#       in the playbook will be deleted or defaulted if possible.
#     - Networks that are not specified in the playbook will be deleted.
#
# Deleted:
#   Networks defined in the playbook will be deleted.
#   If no Networks are provided in the playbook, all Networks present on that DCNM fabric will be deleted.
#
# Query:
#   Returns the current DCNM state for the Networks listed in the playbook.

- name: Merge networks
  cisco.dcnm.dcnm_network:
    fabric: vxlan-fabric
    state: merged
    config:
    - net_name: ansible-net13
      vrf_name: Tenant-1
      net_id: 7005
      net_template: Default_Network_Universal
      net_extension_template: Default_Network_Extension_Universal
      vlan_id: 150
      gw_ip_subnet: '192.168.30.1/24'
      attach:
      - ip_address: 192.168.1.224
        ports: [Ethernet1/13, Ethernet1/14]
      - ip_address: 192.168.1.225
        ports: [Ethernet1/13, Ethernet1/14]
      deploy: true
    - net_name: ansible-net12
      vrf_name: Tenant-2
      net_id: 7002
      net_template: Default_Network_Universal
      net_extension_template: Default_Network_Extension_Universal
      vlan_id: 151
      gw_ip_subnet: '192.168.40.1/24'
      attach:
      - ip_address: 192.168.1.224
        ports: [Ethernet1/11, Ethernet1/12]
        tor_ports:
        - ip_address: 192.168.1.120
          ports: [Ethernet1/14, Ethernet1/15]
      - ip_address: 192.168.1.225
        ports: [Ethernet1/11, Ethernet1/12]
      deploy: false

- name: Replace networks
  cisco.dcnm.dcnm_network:
    fabric: vxlan-fabric
    state: replaced
    config:
      - net_name: ansible-net13
        vrf_name: Tenant-1
        net_id: 7005
        net_template: Default_Network_Universal
        net_extension_template: Default_Network_Extension_Universal
        vlan_id: 150
        gw_ip_subnet: '192.168.30.1/24'
        attach:
        - ip_address: 192.168.1.224
          # Replace the ports with new ports
          # ports: [Ethernet1/13, Ethernet1/14]
          ports: [Ethernet1/16, Ethernet1/17]
          # Delete this attachment
        # - ip_address: 192.168.1.225
        #   ports: [Ethernet1/13, Ethernet1/14]
        deploy: true
        # Dont touch this if its present on DCNM
        # - net_name: ansible-net12
        #   vrf_name: Tenant-2
        #   net_id: 7002
        #   net_template: Default_Network_Universal
        #   net_extension_template: Default_Network_Extension_Universal
        #   vlan_id: 151
        #   gw_ip_subnet: '192.168.40.1/24'
        #   attach:
        #     - ip_address: 192.168.1.224
        #       ports: [Ethernet1/11, Ethernet1/12]
        #     - ip_address: 192.168.1.225
        #       ports: [Ethernet1/11, Ethernet1/12]
        #   deploy: false

- name: Override networks
  cisco.dcnm.dcnm_network:
    fabric: vxlan-fabric
    state: overridden
    config:
    - net_name: ansible-net13
      vrf_name: Tenant-1
      net_id: 7005
      net_template: Default_Network_Universal
      net_extension_template: Default_Network_Extension_Universal
      vlan_id: 150
      gw_ip_subnet: '192.168.30.1/24'
      attach:
      - ip_address: 192.168.1.224
        # Replace the ports with new ports
        # ports: [Ethernet1/13, Ethernet1/14]
        ports: [Ethernet1/16, Ethernet1/17]
        # Delete this attachment
        # - ip_address: 192.168.1.225
        #   ports: [Ethernet1/13, Ethernet1/14]
      deploy: true
      # Delete this network
      # - net_name: ansible-net12
      #   vrf_name: Tenant-2
      #   net_id: 7002
      #   net_template: Default_Network_Universal
      #   net_extension_template: Default_Network_Extension_Universal
      #   vlan_id: 151
      #   gw_ip_subnet: '192.168.40.1/24'
      #   attach:
      #   - ip_address: 192.168.1.224
      #     ports: [Ethernet1/11, Ethernet1/12]
      #   - ip_address: 192.168.1.225
      #     ports: [Ethernet1/11, Ethernet1/12]
      #   deploy: false

- name: Delete selected networks
  cisco.dcnm.dcnm_network:
    fabric: vxlan-fabric
    state: deleted
    config:
    - net_name: ansible-net13
      vrf_name: Tenant-1
      net_id: 7005
      net_template: Default_Network_Universal
      net_extension_template: Default_Network_Extension_Universal
      vlan_id: 150
      gw_ip_subnet: '192.168.30.1/24'
    - net_name: ansible-net12
      vrf_name: Tenant-2
      net_id: 7002
      net_template: Default_Network_Universal
      net_extension_template: Default_Network_Extension_Universal
      vlan_id: 151
      gw_ip_subnet: '192.168.40.1/24'
      deploy: false

- name: Delete all the networkss
  cisco.dcnm.dcnm_network:
    fabric: vxlan-fabric
    state: deleted

- name: Query Networks
  cisco.dcnm.dcnm_network:
    fabric: vxlan-fabric
    state: query
    config:
    - net_name: ansible-net13
    - net_name: ansible-net12
```
