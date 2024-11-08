# dcnm_links

???+ "Details"

    - short_description
        - DCNM ansible module for managing Links.
    - version_added
        - 2.1.0
    - description
        - DCNM ansible module for creating, modifying, deleting and querying Links
    - author
        - Mallik Mudigonda (@mmudigon)


## options

???+ "Details"


### src_fabric

???+ "Details"

    - description
        - Name of the source fabric for links operations.
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
        - deleted
        - query
    - default
        - merged

### deploy

???+ "Details"

    - description
        - Flag to control deployment of links. If set to 'true' then the links included will be deployed to specified switches. If set to 'false', the links will be created but not deployed. 
        - Setting this flag to 'true' will result in all pending configurations on the source and destination devices to be deployed.
    - type
        - bool
    - required
        - False
    - default
        - True

### config

???+ "Details"

    - description
        - A list of dictionaries containing Links information.
    - type
        - list
    - elements
        - dict
    - default
        - []

#### dst_fabric

???+ "Details"

    - description
        - Name of the destination fabric. If this is same as 'src_fabric' then the link is considered intra-fabric link. If this parameter is different from 'src_fabric', then the link is considered inter-fabric link.
    - type
        - str
    - required
        - True

#### src_device

???+ "Details"

    - description
        - IP address or DNS name of the source switch which is part of the link being configured.
    - type
        - str
    - required
        - True

#### dst_device

???+ "Details"

    - description
        - IP address or DNS name of the destination switch which is part of the link being configured.
    - type
        - str
    - required
        - True

#### src_interface

???+ "Details"

    - description
        - Interface on the source device which is part of the link being configured.
    - type
        - str
    - required
        - True

#### dst_interface

???+ "Details"

    - description
        - Interface on the destination device which is part of the link being configured.
    - type
        - str
    - required
        - True

#### template

???+ "Details"

    - description
        - Name of the template that is applied on the link being configured. 
        - The last 3 template choices are applicable for inter-fabric links and the others are applicable for intra-fabric links. 
        - This parameter is required only for 'merged' and 'replaced' states. It is optional for other states.
    - type
        - str
    - required
        - True
    - choices
        - int_intra_fabric_ipv6_link_local(intra-fabric)
        - int_intra_fabric_num_link (intra-fabric)
        - int_intra_fabric_unnum_link (intra-fabric)
        - int_intra_vpc_peer_keep_alive_link (intra-fabric)
        - int_pre_provision_intra_fabric_link (intra-fabric)
        - ios_xe_int_intra_fabric_num_link (intra-fabric)
        - ext_fabric_setup (inter-fabric)
        - ext_multisite_underlay_setup (inter-fabric)
        - ext_evpn_multisite_overlay_setup (inter-fabric)

#### profile

???+ "Details"

    - description
        - Additional link related parameters that must be included while creating links.

##### peer1_ipv4_address

???+ "Details"

    - description
        - IPV4 address of the source interface. 
        - This parameter is optional if the underlying fabric is ipv6 enabled. 
        - This parameter is required only if template is 'int_intra_fabric_num_link' or 'ios_xe_int_intra_fabric_num_link' or 'int_intra_vpc_peer_keep_alive_link'.
    - type
        - str
    - required
        - True

##### peer2_ipv4_address

???+ "Details"

    - description
        - IPV4 address of the destination interface. 
        - This parameter is optional if the underlying fabric is ipv6 enabled. 
        - This parameter is required only if template is 'int_intra_fabric_num_link' or 'ios_xe_int_intra_fabric_num_link' or 'int_intra_vpc_peer_keep_alive_link'.
    - type
        - str
    - required
        - True

##### peer1_ipv6_address

???+ "Details"

    - description
        - IPV6 address of the source interface. 
        - This parameter is required only if the underlying fabric is ipv6 enabled. 
        - This parameter is required only if template is 'int_intra_fabric_num_link' or 'ios_xe_int_intra_fabric_num_link' or 'int_intra_vpc_peer_keep_alive_link'.
    - type
        - str
    - required
        - False
    - default
        - 

##### peer2_ipv6_address

???+ "Details"

    - description
        - IPV6 address of the destination interface. 
        - This parameter is required only if the underlying fabric is ipv6 enabled. 
        - This parameter is required only if template is 'int_intra_fabric_num_link' or 'ios_xe_int_intra_fabric_num_link' or 'int_intra_vpc_peer_keep_alive_link'.
    - type
        - str
    - required
        - False
    - default
        - 

##### ipv4_subnet

???+ "Details"

    - description
        - IPV4 address of the source interface with mask. 
        - Required for below templates 
        - ext_fabric_setup 
        - ext_multisite_underlay_setup
    - type
        - str
    - required
        - True

##### ipv4_address

???+ "Details"

    - description
        - IPV4 address of the source interface without mask. 
        - This parameter is required only if template is 'ext_evpn_multisite_overlay_setup'.
    - type
        - str
    - required
        - True

##### neighbor_ip

???+ "Details"

    - description
        - IPV4 address of the neighbor switch on the destination fabric. 
        - Required for below templates 
        - ext_fabric_setup 
        - ext_multisite_underlay_setup 
        - ext_evpn_multisite_overlay_setup 
        - ext_vxlan_mpls_underlay_setup 
        - ext_vxlan_mpls_overlay_setup
    - type
        - str
    - required
        - True

##### src_asn

???+ "Details"

    - description
        - BGP ASN number on the source fabric. 
        - Required for below templates 
        - ext_fabric_setup 
        - ext_multisite_underlay_setup 
        - ext_evpn_multisite_overlay_setup 
        - ext_vxlan_mpls_overlay_setup
    - type
        - str
    - required
        - True

##### dst_asn

???+ "Details"

    - description
        - BGP ASN number on the destination fabric. 
        - Required for below templates 
        - ext_fabric_setup 
        - ext_multisite_underlay_setup 
        - ext_evpn_multisite_overlay_setup 
        - ext_vxlan_mpls_overlay_setup
    - type
        - str
    - required
        - True

##### auto_deploy

???+ "Details"

    - description
        - Flag that controls auto generation of neighbor VRF Lite configuration for managed neighbor devices. 
        - This parameter is required only if template is 'ext_fabric_setup'.
    - type
        - str
    - required
        - True

##### max_paths

???+ "Details"

    - description
        - Maximum number of iBGP/eBGP paths. 
        - This parameter is required only if template is 'ext_multisite_underlay_setup'.
    - type
        - int
    - required
        - False
    - default
        - 1

##### ebgp_password_enable

???+ "Details"

    - description
        - Flag to enable eBGP password. 
        - This parameter is required only if template is 'ext_multisite_underlay_setup' or 'ext_evpn_multisite_overlay_setup'.
    - type
        - bool
    - required
        - False
    - default
        - True

##### inherit_from_msd

???+ "Details"

    - description
        - Flag indicating whether to inherit BGP password from MSD information. 
        - Applicable only when source and destination fabric are in the same MSD fabric. 
        - This parameter is required only if template is 'ext_multisite_underlay_setup' or 'ext_evpn_multisite_overlay_setup'
    - type
        - bool
    - required
        - False
    - default
        - True

##### ebgp_password

???+ "Details"

    - description
        - Encrypted eBGP Password Hex String. 
        - This parameter is required only if template is 'ext_multisite_underlay_setup' or 'ext_evpn_multisite_overlay_setup'. 
        - This parameter is required only if inherit_from_msd is false.
    - type
        - str
    - required
        - True

##### ebgp_auth_key_type

???+ "Details"

    - description
        - BGP Key Encryption Type. 
        - This parameter is required only if template is 'ext_multisite_underlay_setup' or 'ext_evpn_multisite_overlay_setup'. 
        - This parameter is required only if inherit_from_msd is false. 
        - Choices are 3 (3DES) or 7 (Cisco)
    - type
        - int
    - required
        - True
    - choices
        - 3
        - 7

##### route_tag

???+ "Details"

    - description
        - Routing tag associated with interface IP. 
        - This parameter is required only if template is 'ext_multisite_underlay_setup'
    - type
        - str
    - default
        - 

##### deploy_dci_tracking

???+ "Details"

    - description
        - Flag to enable deploy DCI tracking. 
        - This parameter is required only if template is 'ext_multisite_underlay_setup'. 
        - This parameter MUST be included only if the fabrics are part of multisite.
    - type
        - bool
    - required
        - False
    - default
        - False

##### trm_enabled

???+ "Details"

    - description
        - Flag to enable Tenant Routed Multicast. 
        - This parameter is required only if template is 'ext_evpn_multisite_overlay_setup'.
    - type
        - bool
    - required
        - False
    - default
        - False

##### bgp_multihop

???+ "Details"

    - description
        - eBGP Time-To-Live Value for Remote Peer. 
        - This parameter is required only if template is 'ext_evpn_multisite_overlay_setup'.
    - type
        - int
    - required
        - False
    - default
        - 5

##### admin_state

???+ "Details"

    - description
        - Admin state of the link. 
        - This parameter is not required if template is 'ext_evpn_multisite_overlay_setup', 'ext_multisite_underlay_setup', and 'ext_fabric_setup'.
    - type
        - bool
    - required
        - True

##### mtu

???+ "Details"

    - description
        - MTU of the link. 
        - This parameter is optional if template is 'ios_xe_int_intra_fabric_num_link'. The default value in this case will be 1500. 
        - This parameter is not required if template is 'ext_evpn_multisite_overlay_setup'.
    - type
        - int
    - required
        - True

##### peer1_description

???+ "Details"

    - description
        - Description of the source interface. 
        - This parameter is not required if template is 'ext_evpn_multisite_overlay_setup'.
    - type
        - str
    - required
        - False
    - default
        - 

##### peer2_description

???+ "Details"

    - description
        - Description of the destination interface. 
        - This parameter is not required if template is 'ext_evpn_multisite_overlay_setup'.
    - type
        - str
    - required
        - False
    - default
        - 

##### peer1_cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under the source interface. 
        - This parameter is not required if template is  'ext_evpn_multisite_overlay_setup'.
    - type
        - list
    - elements
        - str
    - required
        - False
    - default
        - []

##### peer2_cmds

???+ "Details"

    - description
        - Commands to be included in the configuration under the destination interface. 
        - This parameter is not required if template is 'ext_evpn_multisite_overlay_setup'.
    - type
        - list
    - elements
        - str
    - required
        - False
    - default
        - []

##### enable_macsec

???+ "Details"

    - description
        - Enable MACsec on the link. 
        - This parameter is applicable only if MACsec feature is enabled on the fabric. 
        - This parameter is applicable only if template is 'int_intra_fabric_ipv6_link_local' or 'int_intra_fabric_num_link' or 'int_intra_fabric_unnum_link'.
    - type
        - bool
    - required
        - False
    - default
        - False

##### peer1_bfd_echo_disable

???+ "Details"

    - description
        - Enable BFD echo on the source interface. Only applicable if BFD is enabled on the fabric. 
        - This parameter is applicable only if template is 'int_intra_fabric_num_link'.
    - type
        - bool
    - required
        - False
    - default
        - False

##### peer2_bfd_echo_disable

???+ "Details"

    - description
        - Enable BFD echo on the destination interface. Only applicable if BFD is enabled on the fabric. 
        - This parameter is applicable only if template is 'int_intra_fabric_num_link'.
    - type
        - bool
    - required
        - False
    - default
        - False

##### intf_vrf

???+ "Details"

    - description
        - Name of the non-default VRF for the link. 
        - Make sure to configure the VRF before using it here. 
        - This parameter is applicable only if template is 'int_intra_vpc_peer_keep_alive_link'.
    - type
        - str
    - required
        - False
    - default
        - 

##### mpls_fabric

???+ "Details"

    - description
        - MPLS LDP or Segment-Routing 
        - This parameter is applicable only if template is `ext_vxlan_mpls_underlay_setup`.
    - type
        - str
    - default
        - SR
    - choices
        - SR
        - LDP

##### peer1_sr_mpls_index

???+ "Details"

    - description
        - Unique SR SID index for the source border 
        - This parameter is applicable only if template is `ext_vxlan_mpls_underlay_setup` and `mpls_fabric` is `SR`
    - type
        - int
    - default
        - 0

##### peer2_sr_mpls_index

???+ "Details"

    - description
        - Unique SR SID index for the destination border 
        - This parameter is applicable only if template is `ext_vxlan_mpls_underlay_setup` and `mpls_fabric` is `SR`
    - type
        - int
    - default
        - 0

##### global_block_range

???+ "Details"

    - description
        - For Segment Routing binding 
        - This parameter is applicable only if template is `ext_vxlan_mpls_underlay_setup` and `mpls_fabric` is `SR`
    - type
        - str
    - default
        - 16000-23999

##### dci_routing_proto

???+ "Details"

    - description
        - Routing protocol used on the DCI MPLS link 
        - This parameter is applicable only if template is `ext_vxlan_mpls_underlay_setup` and `mpls_fabric` is `SR`
    - type
        - str
    - default
        - is-is
    - choices
        - is-is
        - ospf

##### ospf_area_id

???+ "Details"

    - description
        - OSPF Area ID in IP address format 
        - This parameter is applicable only if template is `ext_vxlan_mpls_underlay_setup` and `dci_routing_proto` is `ospf`
    - type
        - str
    - default
        - 0.0.0.0

##### dci_routing_tag

???+ "Details"

    - description
        - Routing Process Tag of DCI Underlay 
        - This parameter is applicable only if template is `ext_vxlan_mpls_underlay_setup`
    - type
        - str
    - default
        - MPLS_UNDERLAY
