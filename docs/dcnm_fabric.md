# dcnm_fabric

???+ "Details"

    - short_description
        - Manage creation and configuration of NDFC fabrics.
    - version_added
        - 3.5.0
    - author
        - Allen Robel (@quantumonion)
    - description
        - Create, delete, update NDFC fabrics.


## options

???+ "Details"


### state

???+ "Details"

    - choices
        - deleted
        - merged
        - query
        - replaced
    - default
        - merged
    - description
        - The state of the feature or object after module completion
    - type
        - str

### skip_validation

???+ "Details"

    - default
        - False
    - description
        - Skip playbook parameter validation.  Useful for debugging.
    - type
        - bool

### config

???+ "Details"

    - description
        - A list of fabric configuration dictionaries
    - type
        - list
    - elements
        - dict

#### DEPLOY

???+ "Details"

    - default
        - False
    - description
        - Save and deploy the fabric configuration.
    - required
        - False
    - type
        - bool

#### FABRIC_NAME

???+ "Details"

    - description
        - The name of the fabric.
    - required
        - True
    - type
        - str

#### FABRIC_TYPE

???+ "Details"

    - choices
        - IPFM
        - ISN
        - LAN_CLASSIC
        - VXLAN_EVPN
        - VXLAN_EVPN_MSD
    - description
        - The type of fabric.
    - required
        - True
    - type
        - str

#### VXLAN_EVPN_FABRIC_PARAMETERS

???+ "Details"

    - description
        - Data Center VXLAN EVPN fabric specific parameters. 
        - Fabric for a VXLAN EVPN deployment with Nexus 9000 and 3000 switches. 
        - The following parameters are specific to VXLAN EVPN fabrics. 
        - The indentation of these parameters is meant only to logically group them. 
        - They should be at the same YAML level as FABRIC_TYPE and FABRIC_NAME.

##### AAA_REMOTE_IP_ENABLED

???+ "Details"

    - default
        - False
    - description
        - Enable only, when IP Authorization is enabled in the AAA Server
    - required
        - False
    - type
        - bool

##### AAA_SERVER_CONF

???+ "Details"

    - default
        - 
    - description
        - AAA Configurations
    - required
        - False
    - type
        - str

##### ADVERTISE_PIP_BGP

???+ "Details"

    - default
        - False
    - description
        - For Primary VTEP IP Advertisement As Next-Hop Of Prefix Routes
    - required
        - False
    - type
        - bool

##### ADVERTISE_PIP_ON_BORDER

???+ "Details"

    - default
        - True
    - description
        - Enable advertise-pip on vPC borders and border gateways only. Applicable only when vPC advertise-pip is not enabled
    - required
        - False
    - type
        - bool

##### ANYCAST_BGW_ADVERTISE_PIP

???+ "Details"

    - default
        - False
    - description
        - To advertise Anycast Border Gateway PIP as VTEP. Effective on MSD fabric Recalculate Config
    - required
        - False
    - type
        - bool

##### ANYCAST_GW_MAC

???+ "Details"

    - default
        - 2020.0000.00aa
    - description
        - Shared MAC address for all leafs (xxxx.xxxx.xxxx)
    - required
        - False
    - type
        - str

##### ANYCAST_LB_ID

???+ "Details"

    - default
        - 10
    - description
        - 'Used for vPC Peering in VXLANv6 Fabrics '
    - required
        - False
    - type
        - int

##### ANYCAST_RP_IP_RANGE

???+ "Details"

    - default
        - 10.254.254.0/24
    - description
        - Anycast or Phantom RP IP Address Range
    - required
        - False
    - type
        - str

##### AUTO_SYMMETRIC_DEFAULT_VRF

???+ "Details"

    - default
        - False
    - description
        - Whether to auto generate Default VRF interface and BGP peering configuration on managed neighbor devices. If set, auto created VRF Lite IFC links will have Auto Deploy Default VRF for Peer enabled.
    - required
        - False
    - type
        - bool

##### AUTO_SYMMETRIC_VRF_LITE

???+ "Details"

    - default
        - False
    - description
        - Whether to auto generate VRF LITE sub-interface and BGP peering configuration on managed neighbor devices. If set, auto created VRF Lite IFC links will have Auto Deploy for Peer enabled.
    - required
        - False
    - type
        - bool

##### AUTO_UNIQUE_VRF_LITE_IP_PREFIX

???+ "Details"

    - default
        - False
    - description
        - When enabled, IP prefix allocated to the VRF LITE IFC is not reused on VRF extension over VRF LITE IFC. Instead, unique IP Subnet is allocated for each VRF extension over VRF LITE IFC.
    - required
        - False
    - type
        - bool

##### AUTO_VRFLITE_IFC_DEFAULT_VRF

???+ "Details"

    - default
        - False
    - description
        - Whether to auto generate Default VRF interface and BGP peering configuration on VRF LITE IFC auto deployment. If set, auto created VRF Lite IFC links will have Auto Deploy Default VRF enabled.
    - required
        - False
    - type
        - bool

##### BANNER

???+ "Details"

    - default
        - 
    - description
        - Message of the Day (motd) banner. Delimiter char (very first char is delimiter char) followed by message ending with delimiter
    - required
        - False
    - type
        - str

##### BFD_AUTH_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Valid for P2P Interfaces only
    - required
        - False
    - type
        - bool

##### BFD_AUTH_KEY

???+ "Details"

    - default
        - 
    - description
        - Encrypted SHA1 secret value
    - required
        - False
    - type
        - str

##### BFD_AUTH_KEY_ID

???+ "Details"

    - default
        - 100
    - description
        - No description available
    - required
        - False
    - type
        - int

##### BFD_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Valid for IPv4 Underlay only
    - required
        - False
    - type
        - bool

##### BFD_IBGP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### BFD_ISIS_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### BFD_OSPF_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### BFD_PIM_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### BGP_AS

???+ "Details"

    - default
        - 
    - description
        - 1-4294967295 | 1-65535.0-65535 It is a good practice to have a unique ASN for each Fabric.
    - required
        - False
    - type
        - str

##### BGP_AUTH_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### BGP_AUTH_KEY

???+ "Details"

    - default
        - 
    - description
        - Encrypted BGP Authentication Key based on type
    - required
        - False
    - type
        - str

##### BGP_AUTH_KEY_TYPE

???+ "Details"

    - choices
        - 3
        - 7
    - default
        - 3
    - description
        - BGP Key Encryption Type: 3 - 3DES, 7 - Cisco
    - required
        - False
    - type
        - int

##### BGP_LB_ID

???+ "Details"

    - default
        - 0
    - description
        - No description available
    - required
        - False
    - type
        - int

##### BOOTSTRAP_CONF

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs required during device bootup/login e.g. AAA/Radius
    - required
        - False
    - type
        - str

##### BOOTSTRAP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Automatic IP Assignment For POAP
    - required
        - False
    - type
        - bool

##### BOOTSTRAP_MULTISUBNET

???+ "Details"

    - default
        - #Scope_Start_IP, Scope_End_IP, Scope_Default_Gateway, Scope_Subnet_Prefix
    - description
        - 'lines with
    - required
        - False
    - type
        - str

##### BROWNFIELD_NETWORK_NAME_FORMAT

???+ "Details"

    - default
        - Auto_Net_VNI$$VNI$$_VLAN$$VLAN_ID$$
    - description
        - Generated network name should be &lt; 64 characters
    - required
        - False
    - type
        - str

##### BROWNFIELD_SKIP_OVERLAY_NETWORK_ATTACHMENTS

???+ "Details"

    - default
        - False
    - description
        - Enable to skip overlay network interface attachments for Brownfield and Host Port Resync cases
    - required
        - False
    - type
        - bool

##### CDP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Enable CDP on management interface
    - required
        - False
    - type
        - bool

##### COPP_POLICY

???+ "Details"

    - choices
        - dense
        - lenient
        - moderate
        - strict
        - manual
    - default
        - strict
    - description
        - Fabric Wide CoPP Policy. Customized CoPP policy should be provided when manual is selected
    - required
        - False
    - type
        - str

##### DCI_SUBNET_RANGE

???+ "Details"

    - default
        - 10.33.0.0/16
    - description
        - Address range to assign P2P Interfabric Connections
    - required
        - False
    - type
        - str

##### DCI_SUBNET_TARGET_MASK

???+ "Details"

    - default
        - 30
    - description
        - No description available
    - required
        - False
    - type
        - int

##### DEFAULT_QUEUING_POLICY_CLOUDSCALE

???+ "Details"

    - choices
        - queuing_policy_default_4q_cloudscale
        - queuing_policy_default_8q_cloudscale
    - default
        - queuing_policy_default_8q_cloudscale
    - description
        - Queuing Policy for all 92xx, -EX, -FX, -FX2, -FX3, -GX series switches in the fabric
    - required
        - False
    - type
        - str

##### DEFAULT_QUEUING_POLICY_OTHER

???+ "Details"

    - choices
        - queuing_policy_default_other
    - default
        - queuing_policy_default_other
    - description
        - Queuing Policy for all other switches in the fabric
    - required
        - False
    - type
        - str

##### DEFAULT_QUEUING_POLICY_R_SERIES

???+ "Details"

    - choices
        - queuing_policy_default_r_series
    - default
        - queuing_policy_default_r_series
    - description
        - Queuing Policy for all R-Series switches in the fabric
    - required
        - False
    - type
        - str

##### DEFAULT_VRF_REDIS_BGP_RMAP

???+ "Details"

    - default
        - extcon-rmap-filter
    - description
        - Route Map used to redistribute BGP routes to IGP in default vrf in auto created VRF Lite IFC links
    - required
        - False
    - type
        - str

##### DHCP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Automatic IP Assignment For POAP From Local DHCP Server
    - required
        - False
    - type
        - bool

##### DHCP_END

???+ "Details"

    - default
        - 
    - description
        - End Address For Switch POAP
    - required
        - False
    - type
        - str

##### DHCP_IPV6_ENABLE

???+ "Details"

    - choices
        - DHCPv4
        - DHCPv6
    - default
        - DHCPv4
    - description
        - No description available
    - required
        - False
    - type
        - str

##### DHCP_START

???+ "Details"

    - default
        - 
    - description
        - Start Address For Switch POAP
    - required
        - False
    - type
        - str

##### DNS_SERVER_IP_LIST

???+ "Details"

    - default
        - 
    - description
        - Comma separated list of IP Addresses(v4/v6)
    - required
        - False
    - type
        - str

##### DNS_SERVER_VRF

???+ "Details"

    - default
        - 
    - description
        - One VRF for all DNS servers or a comma separated list of VRFs, one per DNS server
    - required
        - False
    - type
        - str

##### ENABLE_AAA

???+ "Details"

    - default
        - False
    - description
        - Include AAA configs from Manageability tab during device bootup
    - required
        - False
    - type
        - bool

##### ENABLE_DEFAULT_QUEUING_POLICY

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### ENABLE_FABRIC_VPC_DOMAIN_ID

???+ "Details"

    - default
        - False
    - description
        - (Not Recommended)
    - required
        - False
    - type
        - bool

##### ENABLE_MACSEC

???+ "Details"

    - default
        - False
    - description
        - Enable MACsec in the fabric
    - required
        - False
    - type
        - bool

##### ENABLE_NETFLOW

???+ "Details"

    - default
        - False
    - description
        - Enable Netflow on VTEPs
    - required
        - False
    - type
        - bool

##### ENABLE_NGOAM

???+ "Details"

    - default
        - True
    - description
        - Enable the Next Generation (NG) OAM feature for all switches in the fabric to aid in trouble-shooting VXLAN EVPN fabrics
    - required
        - False
    - type
        - bool

##### ENABLE_NXAPI

???+ "Details"

    - default
        - True
    - description
        - Enable HTTPS NX-API
    - required
        - False
    - type
        - bool

##### ENABLE_NXAPI_HTTP

???+ "Details"

    - default
        - True
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### ENABLE_PBR

???+ "Details"

    - default
        - False
    - description
        - When ESR option is ePBR, enable ePBR will enable pbr, sla sender and epbr features on the switch
    - required
        - False
    - type
        - bool

##### ENABLE_PVLAN

???+ "Details"

    - default
        - False
    - description
        - Enable PVLAN on switches except spines and super spines
    - required
        - False
    - type
        - bool

##### ENABLE_TENANT_DHCP

???+ "Details"

    - default
        - True
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### ENABLE_TRM

???+ "Details"

    - default
        - False
    - description
        - For Overlay Multicast Support In VXLAN Fabrics
    - required
        - False
    - type
        - bool

##### ENABLE_VPC_PEER_LINK_NATIVE_VLAN

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### ESR_OPTION

???+ "Details"

    - default
        - PBR
    - description
        - Policy-Based Routing (PBR) or Enhanced PBR (ePBR)
    - required
        - False
    - type
        - str

##### EXTRA_CONF_INTRA_LINKS

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs For All Intra-Fabric Links
    - required
        - False
    - type
        - str

##### EXTRA_CONF_LEAF

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs For All Leafs As Captured From Show Running Configuration
    - required
        - False
    - type
        - str

##### EXTRA_CONF_SPINE

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs For All Spines As Captured From Show Running Configuration
    - required
        - False
    - type
        - str

##### EXTRA_CONF_TOR

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs For All ToRs As Captured From Show Running Configuration
    - required
        - False
    - type
        - str

##### FABRIC_INTERFACE_TYPE

???+ "Details"

    - choices
        - p2p
        - unnumbered
    - default
        - p2p
    - description
        - Numbered(Point-to-Point) or Unnumbered
    - required
        - False
    - type
        - str

##### FABRIC_MTU

???+ "Details"

    - default
        - 9216
    - description
        - . Must be an even number
    - required
        - False
    - type
        - int

##### FABRIC_NAME

???+ "Details"

    - default
        - 
    - description
        - Please provide the fabric name to create it (Max Size 32)
    - required
        - False
    - type
        - str

##### FABRIC_VPC_DOMAIN_ID

???+ "Details"

    - default
        - 1
    - description
        - vPC Domain Id to be used on all vPC pairs
    - required
        - False
    - type
        - int

##### FABRIC_VPC_QOS

???+ "Details"

    - default
        - False
    - description
        - Qos on spines for guaranteed delivery of vPC Fabric Peering communication
    - required
        - False
    - type
        - bool

##### FABRIC_VPC_QOS_POLICY_NAME

???+ "Details"

    - default
        - spine_qos_for_fabric_vpc_peering
    - description
        - Qos Policy name should be same on all spines
    - required
        - False
    - type
        - str

##### FEATURE_PTP

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### GRFIELD_DEBUG_FLAG

???+ "Details"

    - choices
        - Enable
        - Disable
    - default
        - Disable
    - description
        - Enable to clean switch configuration without reload when PreserveConfig=no
    - required
        - False
    - type
        - str

##### HD_TIME

???+ "Details"

    - default
        - 180
    - description
        - NVE Source Inteface HoldDown Time  in seconds
    - required
        - False
    - type
        - int

##### HOST_INTF_ADMIN_STATE

???+ "Details"

    - default
        - True
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### IBGP_PEER_TEMPLATE

???+ "Details"

    - default
        - 
    - description
        - Speficies the iBGP Peer-Template config used for RR and spines with border role.
    - required
        - False
    - type
        - str

##### IBGP_PEER_TEMPLATE_LEAF

???+ "Details"

    - default
        - 
    - description
        - Specifies the config used for leaf, border or border gateway. If this field is empty, the peer template defined in iBGP Peer-Template Config is used on all BGP enabled devices (RRs,leafs, border or border gateway roles.
    - required
        - False
    - type
        - str

##### INBAND_DHCP_SERVERS

???+ "Details"

    - default
        - 
    - description
        - Comma separated list of IPv4 Addresses (Max 3)
    - required
        - False
    - type
        - str

##### INBAND_MGMT

???+ "Details"

    - default
        - False
    - description
        - Manage switches with only Inband connectivity
    - required
        - False
    - type
        - bool

##### ISIS_AUTH_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### ISIS_AUTH_KEY

???+ "Details"

    - default
        - 
    - description
        - Cisco Type 7 Encrypted
    - required
        - False
    - type
        - str

##### ISIS_AUTH_KEYCHAIN_KEY_ID

???+ "Details"

    - default
        - 127
    - description
        - No description available
    - required
        - False
    - type
        - int

##### ISIS_AUTH_KEYCHAIN_NAME

???+ "Details"

    - default
        - 
    - description
        - No description available
    - required
        - False
    - type
        - str

##### ISIS_LEVEL

???+ "Details"

    - choices
        - level-1
        - level-2
    - default
        - level-2
    - description
        - Supported IS types: level-1, level-2
    - required
        - False
    - type
        - str

##### ISIS_OVERLOAD_ELAPSE_TIME

???+ "Details"

    - default
        - 60
    - description
        - Clear the overload bit after an elapsed time in seconds
    - required
        - False
    - type
        - int

##### ISIS_OVERLOAD_ENABLE

???+ "Details"

    - default
        - True
    - description
        - When enabled, set the overload bit for an elapsed time after a reload
    - required
        - False
    - type
        - bool

##### ISIS_P2P_ENABLE

???+ "Details"

    - default
        - True
    - description
        - This will enable network point-to-point on fabric interfaces which are numbered
    - required
        - False
    - type
        - bool

##### L2_HOST_INTF_MTU

???+ "Details"

    - default
        - 9216
    - description
        - . Must be an even number
    - required
        - False
    - type
        - int

##### L2_SEGMENT_ID_RANGE

???+ "Details"

    - default
        - 30000-49000
    - description
        - 'Overlay Network Identifier Range '
    - required
        - False
    - type
        - str

##### L3VNI_MCAST_GROUP

???+ "Details"

    - default
        - 239.1.1.0
    - description
        - Default Underlay Multicast group IP assigned for every overlay VRF.
    - required
        - False
    - type
        - str

##### L3_PARTITION_ID_RANGE

???+ "Details"

    - default
        - 50000-59000
    - description
        - 'Overlay VRF Identifier Range '
    - required
        - False
    - type
        - str

##### LINK_STATE_ROUTING

???+ "Details"

    - choices
        - ospf
        - is-is
    - default
        - ospf
    - description
        - Used for Spine-Leaf Connectivity
    - required
        - False
    - type
        - str

##### LINK_STATE_ROUTING_TAG

???+ "Details"

    - default
        - UNDERLAY
    - description
        - Underlay Routing Process Tag
    - required
        - False
    - type
        - str

##### LOOPBACK0_IPV6_RANGE

???+ "Details"

    - default
        - fd00::a02:0/119
    - description
        - Typically Loopback0 IPv6 Address Range
    - required
        - False
    - type
        - str

##### LOOPBACK0_IP_RANGE

???+ "Details"

    - default
        - 10.2.0.0/22
    - description
        - Typically Loopback0 IP Address Range
    - required
        - False
    - type
        - str

##### LOOPBACK1_IPV6_RANGE

???+ "Details"

    - default
        - fd00::a03:0/118
    - description
        - Typically Loopback1 and Anycast Loopback IPv6 Address Range
    - required
        - False
    - type
        - str

##### LOOPBACK1_IP_RANGE

???+ "Details"

    - default
        - 10.3.0.0/22
    - description
        - Typically Loopback1 IP Address Range
    - required
        - False
    - type
        - str

##### MACSEC_ALGORITHM

???+ "Details"

    - default
        - AES_128_CMAC
    - description
        - AES_128_CMAC or AES_256_CMAC
    - required
        - False
    - type
        - str

##### MACSEC_CIPHER_SUITE

???+ "Details"

    - default
        - GCM-AES-XPN-256
    - description
        - Configure Cipher Suite
    - required
        - False
    - type
        - str

##### MACSEC_FALLBACK_ALGORITHM

???+ "Details"

    - default
        - AES_128_CMAC
    - description
        - AES_128_CMAC or AES_256_CMAC
    - required
        - False
    - type
        - str

##### MACSEC_FALLBACK_KEY_STRING

???+ "Details"

    - default
        - 
    - description
        - Cisco Type 7 Encrypted Octet String
    - required
        - False
    - type
        - str

##### MACSEC_KEY_STRING

???+ "Details"

    - default
        - 
    - description
        - Cisco Type 7 Encrypted Octet String
    - required
        - False
    - type
        - str

##### MACSEC_REPORT_TIMER

???+ "Details"

    - default
        - 5
    - description
        - MACsec Operational Status periodic report timer in minutes
    - required
        - False
    - type
        - int

##### MGMT_GW

???+ "Details"

    - default
        - 
    - description
        - Default Gateway For Management VRF On The Switch
    - required
        - False
    - type
        - str

##### MGMT_PREFIX

???+ "Details"

    - default
        - 24
    - description
        - No description available
    - required
        - False
    - type
        - int

##### MGMT_V6PREFIX

???+ "Details"

    - default
        - 64
    - description
        - No description available
    - required
        - False
    - type
        - int

##### MPLS_HANDOFF

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### MPLS_LB_ID

???+ "Details"

    - default
        - 101
    - description
        - 'Used for VXLAN to MPLS SR/LDP Handoff '
    - required
        - False
    - type
        - int

##### MPLS_LOOPBACK_IP_RANGE

???+ "Details"

    - default
        - 10.101.0.0/25
    - description
        - Used for VXLAN to MPLS SR/LDP Handoff
    - required
        - False
    - type
        - str

##### MST_INSTANCE_RANGE

???+ "Details"

    - default
        - 0
    - description
        - MST instance range, Example: 0-3,5,7-9, Default is 0
    - required
        - False
    - type
        - str

##### MULTICAST_GROUP_SUBNET

???+ "Details"

    - default
        - 239.1.1.0/25
    - description
        - Multicast pool prefix between 8 to 30. A multicast group IP from this pool is used for BUM traffic for each overlay network.
    - required
        - False
    - type
        - str

##### NETFLOW_EXPORTER_LIST

???+ "Details"

    - default
        - 
    - description
        - One or Multiple Netflow Exporters
    - required
        - False
    - type
        - list
    - elements
        - str

##### NETFLOW_MONITOR_LIST

???+ "Details"

    - default
        - 
    - description
        - One or Multiple Netflow Monitors
    - required
        - False
    - type
        - list
    - elements
        - str

##### NETFLOW_RECORD_LIST

???+ "Details"

    - default
        - 
    - description
        - One or Multiple Netflow Records
    - required
        - False
    - type
        - list
    - elements
        - str

##### NETWORK_VLAN_RANGE

???+ "Details"

    - default
        - 2300-2999
    - description
        - 'Per Switch Overlay Network VLAN Range '
    - required
        - False
    - type
        - str

##### NTP_SERVER_IP_LIST

???+ "Details"

    - default
        - 
    - description
        - Comma separated list of IP Addresses(v4/v6)
    - required
        - False
    - type
        - str

##### NTP_SERVER_VRF

???+ "Details"

    - default
        - 
    - description
        - One VRF for all NTP servers or a comma separated list of VRFs, one per NTP server
    - required
        - False
    - type
        - str

##### NVE_LB_ID

???+ "Details"

    - default
        - 1
    - description
        - No description available
    - required
        - False
    - type
        - int

##### NXAPI_HTTPS_PORT

???+ "Details"

    - default
        - 443
    - description
        - No description available
    - required
        - False
    - type
        - int

##### NXAPI_HTTP_PORT

???+ "Details"

    - default
        - 80
    - description
        - No description available
    - required
        - False
    - type
        - int

##### OBJECT_TRACKING_NUMBER_RANGE

???+ "Details"

    - default
        - 100-299
    - description
        - 'Per switch tracked object ID Range '
    - required
        - False
    - type
        - str

##### OSPF_AREA_ID

???+ "Details"

    - default
        - 0.0.0.0
    - description
        - OSPF Area Id in IP address format
    - required
        - False
    - type
        - str

##### OSPF_AUTH_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### OSPF_AUTH_KEY

???+ "Details"

    - default
        - 
    - description
        - 3DES Encrypted
    - required
        - False
    - type
        - str

##### OSPF_AUTH_KEY_ID

???+ "Details"

    - default
        - 127
    - description
        - No description available
    - required
        - False
    - type
        - int

##### OVERLAY_MODE

???+ "Details"

    - default
        - cli
    - description
        - VRF/Network configuration using config-profile or CLI
    - required
        - False
    - type
        - str

##### PER_VRF_LOOPBACK_AUTO_PROVISION

???+ "Details"

    - default
        - False
    - description
        - Auto provision a loopback on a VTEP on VRF attachment
    - required
        - False
    - type
        - bool

##### PER_VRF_LOOPBACK_IP_RANGE

???+ "Details"

    - default
        - 10.5.0.0/22
    - description
        - Prefix pool to assign IP addresses to loopbacks on VTEPs on a per VRF basis
    - required
        - False
    - type
        - str

##### PHANTOM_RP_LB_ID1

???+ "Details"

    - default
        - 2
    - description
        - 'Used for Bidir-PIM Phantom RP '
    - required
        - False
    - type
        - int

##### PHANTOM_RP_LB_ID2

???+ "Details"

    - default
        - 3
    - description
        - 'Used for Fallback Bidir-PIM Phantom RP '
    - required
        - False
    - type
        - int

##### PHANTOM_RP_LB_ID3

???+ "Details"

    - default
        - 4
    - description
        - 'Used for second Fallback Bidir-PIM Phantom RP '
    - required
        - False
    - type
        - int

##### PHANTOM_RP_LB_ID4

???+ "Details"

    - default
        - 5
    - description
        - 'Used for third Fallback Bidir-PIM Phantom RP '
    - required
        - False
    - type
        - int

##### PIM_HELLO_AUTH_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Valid for IPv4 Underlay only
    - required
        - False
    - type
        - bool

##### PIM_HELLO_AUTH_KEY

???+ "Details"

    - default
        - 
    - description
        - 3DES Encrypted
    - required
        - False
    - type
        - str

##### PM_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### POWER_REDUNDANCY_MODE

???+ "Details"

    - choices
        - ps-redundant
        - combined
        - insrc-redundant
    - default
        - ps-redundant
    - description
        - Default Power Supply Mode For The Fabric
    - required
        - False
    - type
        - str

##### PTP_DOMAIN_ID

???+ "Details"

    - default
        - 0
    - description
        - 'Multiple Independent PTP Clocking Subdomains on a Single Network '
    - required
        - False
    - type
        - int

##### PTP_LB_ID

???+ "Details"

    - default
        - 0
    - description
        - No description available
    - required
        - False
    - type
        - int

##### REPLICATION_MODE

???+ "Details"

    - choices
        - Multicast
        - Ingress
    - default
        - Multicast
    - description
        - Replication Mode for BUM Traffic
    - required
        - False
    - type
        - str

##### ROUTER_ID_RANGE

???+ "Details"

    - default
        - 10.2.0.0/23
    - description
        - No description available
    - required
        - False
    - type
        - str

##### ROUTE_MAP_SEQUENCE_NUMBER_RANGE

???+ "Details"

    - default
        - 1-65534
    - description
        - No description available
    - required
        - False
    - type
        - str

##### RP_COUNT

???+ "Details"

    - choices
        - 2
        - 4
    - default
        - 2
    - description
        - Number of spines acting as Rendezvous-Point (RP)
    - required
        - False
    - type
        - int

##### RP_LB_ID

???+ "Details"

    - default
        - 254
    - description
        - No description available
    - required
        - False
    - type
        - int

##### RP_MODE

???+ "Details"

    - choices
        - asm
        - bidir
    - default
        - asm
    - description
        - Multicast RP Mode
    - required
        - False
    - type
        - str

##### RR_COUNT

???+ "Details"

    - choices
        - 2
        - 4
    - default
        - 2
    - description
        - Number of spines acting as Route-Reflectors
    - required
        - False
    - type
        - int

##### SEED_SWITCH_CORE_INTERFACES

???+ "Details"

    - default
        - 
    - description
        - Core-facing Interface list on Seed Switch (e.g. e1/1-30,e1/32)
    - required
        - False
    - type
        - str

##### SERVICE_NETWORK_VLAN_RANGE

???+ "Details"

    - default
        - 3000-3199
    - description
        - 'Per Switch Overlay Service Network VLAN Range '
    - required
        - False
    - type
        - str

##### SITE_ID

???+ "Details"

    - default
        - 
    - description
        - For EVPN Multi-Site Support . Defaults to Fabric ASN
    - required
        - False
    - type
        - str

##### SLA_ID_RANGE

???+ "Details"

    - default
        - 10000-19999
    - description
        - 'Per switch SLA ID Range '
    - required
        - False
    - type
        - str

##### SNMP_SERVER_HOST_TRAP

???+ "Details"

    - default
        - True
    - description
        - Configure NDFC as a receiver for SNMP traps
    - required
        - False
    - type
        - bool

##### SPINE_SWITCH_CORE_INTERFACES

???+ "Details"

    - default
        - 
    - description
        - Core-facing Interface list on all Spines (e.g. e1/1-30,e1/32)
    - required
        - False
    - type
        - str

##### STATIC_UNDERLAY_IP_ALLOC

???+ "Details"

    - default
        - False
    - description
        - Checking this will disable Dynamic Underlay IP Address Allocations
    - required
        - False
    - type
        - bool

##### STP_BRIDGE_PRIORITY

???+ "Details"

    - default
        - 0
    - description
        - Bridge priority for the spanning tree in increments of 4096
    - required
        - False
    - type
        - int

##### STP_ROOT_OPTION

???+ "Details"

    - choices
        - rpvst+
        - mst
        - unmanaged
    - default
        - unmanaged
    - description
        - Which protocol to use for configuring root bridge? rpvst+: Rapid Per-VLAN Spanning Tree, mst: Multiple Spanning Tree, unmanaged (default): STP Root not managed by NDFC
    - required
        - False
    - type
        - str

##### STP_VLAN_RANGE

???+ "Details"

    - default
        - 1-3967
    - description
        - Vlan range, Example: 1,3-5,7,9-11, Default is 1-3967
    - required
        - False
    - type
        - str

##### STRICT_CC_MODE

???+ "Details"

    - default
        - False
    - description
        - Enable bi-directional compliance checks to flag additional configs in the running config that are not in the intent/expected config
    - required
        - False
    - type
        - bool

##### SUBINTERFACE_RANGE

???+ "Details"

    - default
        - 2-511
    - description
        - 'Per Border Dot1q Range For VRF Lite Connectivity '
    - required
        - False
    - type
        - str

##### SUBNET_RANGE

???+ "Details"

    - default
        - 10.4.0.0/16
    - description
        - Address range to assign Numbered and Peer Link SVI IPs
    - required
        - False
    - type
        - str

##### SUBNET_TARGET_MASK

???+ "Details"

    - choices
        - 30
        - 31
    - default
        - 30
    - description
        - Mask for Underlay Subnet IP Range
    - required
        - False
    - type
        - int

##### SYSLOG_SERVER_IP_LIST

???+ "Details"

    - default
        - 
    - description
        - Comma separated list of IP Addresses(v4/v6)
    - required
        - False
    - type
        - str

##### SYSLOG_SERVER_VRF

???+ "Details"

    - default
        - 
    - description
        - One VRF for all Syslog servers or a comma separated list of VRFs, one per Syslog server
    - required
        - False
    - type
        - str

##### SYSLOG_SEV

???+ "Details"

    - default
        - 
    - description
        - 'Comma separated list of Syslog severity values, one per Syslog server '
    - required
        - False
    - type
        - str

##### TCAM_ALLOCATION

???+ "Details"

    - default
        - True
    - description
        - TCAM commands are automatically generated for VxLAN and vPC Fabric Peering when Enabled
    - required
        - False
    - type
        - bool

##### UNDERLAY_IS_V6

???+ "Details"

    - default
        - False
    - description
        - If not enabled, IPv4 underlay is used
    - required
        - False
    - type
        - bool

##### UNNUM_BOOTSTRAP_LB_ID

???+ "Details"

    - default
        - 253
    - description
        - No description available
    - required
        - False
    - type
        - int

##### UNNUM_DHCP_END

???+ "Details"

    - default
        - 
    - description
        - Must be a subset of IGP/BGP Loopback Prefix Pool
    - required
        - False
    - type
        - str

##### UNNUM_DHCP_START

???+ "Details"

    - default
        - 
    - description
        - Must be a subset of IGP/BGP Loopback Prefix Pool
    - required
        - False
    - type
        - str

##### USE_LINK_LOCAL

???+ "Details"

    - default
        - True
    - description
        - If not enabled, Spine-Leaf interfaces will use global IPv6 addresses
    - required
        - False
    - type
        - bool

##### V6_SUBNET_RANGE

???+ "Details"

    - default
        - fd00::a04:0/112
    - description
        - IPv6 Address range to assign Numbered and Peer Link SVI IPs
    - required
        - False
    - type
        - str

##### V6_SUBNET_TARGET_MASK

???+ "Details"

    - choices
        - 126
        - 127
    - default
        - 126
    - description
        - Mask for Underlay Subnet IPv6 Range
    - required
        - False
    - type
        - int

##### VPC_AUTO_RECOVERY_TIME

???+ "Details"

    - default
        - 360
    - description
        - No description available
    - required
        - False
    - type
        - int

##### VPC_DELAY_RESTORE

???+ "Details"

    - default
        - 150
    - description
        - No description available
    - required
        - False
    - type
        - int

##### VPC_DOMAIN_ID_RANGE

???+ "Details"

    - default
        - 1-1000
    - description
        - vPC Domain id range to use for new pairings
    - required
        - False
    - type
        - str

##### VPC_ENABLE_IPv6_ND_SYNC

???+ "Details"

    - default
        - True
    - description
        - Enable IPv6 ND synchronization between vPC peers
    - required
        - False
    - type
        - bool

##### VPC_PEER_KEEP_ALIVE_OPTION

???+ "Details"

    - choices
        - loopback
        - management
    - default
        - management
    - description
        - Use vPC Peer Keep Alive with Loopback or Management
    - required
        - False
    - type
        - str

##### VPC_PEER_LINK_PO

???+ "Details"

    - default
        - 500
    - description
        - No description available
    - required
        - False
    - type
        - int

##### VPC_PEER_LINK_VLAN

???+ "Details"

    - default
        - 3600
    - description
        - 'VLAN range for vPC Peer Link SVI '
    - required
        - False
    - type
        - int

##### VRF_LITE_AUTOCONFIG

???+ "Details"

    - choices
        - Manual
        - Back2Back&ToExternal
    - default
        - Manual
    - description
        - VRF Lite Inter-Fabric Connection Deployment Options. If Back2Back&ToExternal is selected, VRF Lite IFCs are auto created between border devices of two Easy Fabrics, and between border devices in Easy Fabric and edge routers in External Fabric. The IP address is taken from the VRF Lite Subnet IP Range pool.
    - required
        - False
    - type
        - str

##### VRF_VLAN_RANGE

???+ "Details"

    - default
        - 2000-2299
    - description
        - 'Per Switch Overlay VRF VLAN Range '
    - required
        - False
    - type
        - str

##### default_network

???+ "Details"

    - choices
        - Default_Network_Universal
        - Service_Network_Universal
    - default
        - Default_Network_Universal
    - description
        - Default Overlay Network Template For Leafs
    - required
        - False
    - type
        - str

##### default_pvlan_sec_network

???+ "Details"

    - choices
        - Pvlan_Secondary_Network
    - default
        - Pvlan_Secondary_Network
    - description
        - Default PVLAN Secondary Network Template
    - required
        - False
    - type
        - str

##### default_vrf

???+ "Details"

    - choices
        - Default_VRF_Universal
    - default
        - Default_VRF_Universal
    - description
        - Default Overlay VRF Template For Leafs
    - required
        - False
    - type
        - str

##### enableRealTimeBackup

???+ "Details"

    - default
        - 
    - description
        - Backup hourly only if there is any config deployment since last backup
    - required
        - False
    - type
        - bool

##### enableScheduledBackup

???+ "Details"

    - default
        - 
    - description
        - Backup at the specified time
    - required
        - False
    - type
        - bool

##### network_extension_template

???+ "Details"

    - choices
        - Default_Network_Extension_Universal
    - default
        - Default_Network_Extension_Universal
    - description
        - Default Overlay Network Template For Borders
    - required
        - False
    - type
        - str

##### scheduledTime

???+ "Details"

    - default
        - 
    - description
        - Time (UTC) in 24hr format. (00:00 to 23:59)
    - required
        - False
    - type
        - str

##### vrf_extension_template

???+ "Details"

    - choices
        - Default_VRF_Extension_Universal
    - default
        - Default_VRF_Extension_Universal
    - description
        - Default Overlay VRF Template For Borders
    - required
        - False
    - type
        - str

#### VXLAN_EVPN_FABRIC_MSD_PARAMETERS

???+ "Details"

    - description
        - VXLAN EVPN Multi-Site fabric specific parameters. 
        - Domain that can contain multiple VXLAN EVPN Fabrics with Layer-2/Layer-3 Overlay Extensions and other Fabric Types. 
        - The indentation of these parameters is meant only to logically group them. 
        - They should be at the same YAML level as FABRIC_TYPE and FABRIC_NAME.

##### ANYCAST_GW_MAC

???+ "Details"

    - default
        - 2020.0000.00aa
    - description
        - Shared MAC address for all leaves
    - required
        - False
    - type
        - str

##### BGP_RP_ASN

???+ "Details"

    - default
        - 
    - description
        - 1-4294967295 | 1-65535.0-65535, e.g. 65000, 65001
    - required
        - False
    - type
        - str

##### BGW_ROUTING_TAG

???+ "Details"

    - default
        - 54321
    - description
        - Routing tag associated with IP address of loopback and DCI interfaces
    - required
        - False
    - type
        - int

##### BORDER_GWY_CONNECTIONS

???+ "Details"

    - choices
        - Manual
        - Centralized_To_Route_Server
        - Direct_To_BGWS
    - default
        - Manual
    - description
        - Manual, Auto Overlay EVPN Peering to Route Servers, Auto Overlay EVPN Direct Peering to Border Gateways
    - required
        - False
    - type
        - str

##### CLOUDSEC_ALGORITHM

???+ "Details"

    - default
        - AES_128_CMAC
    - description
        - AES_128_CMAC or AES_256_CMAC
    - required
        - False
    - type
        - str

##### CLOUDSEC_AUTOCONFIG

???+ "Details"

    - default
        - False
    - description
        - Auto Config CloudSec on Border Gateways
    - required
        - False
    - type
        - bool

##### CLOUDSEC_ENFORCEMENT

???+ "Details"

    - default
        - 
    - description
        - If set to strict, data across site must be encrypted.
    - required
        - False
    - type
        - str

##### CLOUDSEC_KEY_STRING

???+ "Details"

    - default
        - 
    - description
        - Cisco Type 7 Encrypted Octet String
    - required
        - False
    - type
        - str

##### CLOUDSEC_REPORT_TIMER

???+ "Details"

    - default
        - 5
    - description
        - CloudSec Operational Status periodic report timer in minutes
    - required
        - False
    - type
        - int

##### DCI_SUBNET_RANGE

???+ "Details"

    - default
        - 10.10.1.0/24
    - description
        - Address range to assign P2P DCI Links
    - required
        - False
    - type
        - str

##### DCI_SUBNET_TARGET_MASK

???+ "Details"

    - default
        - 30
    - description
        - 'Target Mask for Subnet Range '
    - required
        - False
    - type
        - int

##### DELAY_RESTORE

???+ "Details"

    - default
        - 300
    - description
        - Multi-Site underlay and overlay control plane convergence time  in seconds
    - required
        - False
    - type
        - int

##### ENABLE_BGP_BFD

???+ "Details"

    - default
        - False
    - description
        - For auto-created Multi-Site Underlay IFCs
    - required
        - False
    - type
        - bool

##### ENABLE_BGP_LOG_NEIGHBOR_CHANGE

???+ "Details"

    - default
        - False
    - description
        - For auto-created Multi-Site Underlay IFCs
    - required
        - False
    - type
        - bool

##### ENABLE_BGP_SEND_COMM

???+ "Details"

    - default
        - False
    - description
        - For auto-created Multi-Site Underlay IFCs
    - required
        - False
    - type
        - bool

##### ENABLE_PVLAN

???+ "Details"

    - default
        - False
    - description
        - Enable PVLAN on MSD and its child fabrics
    - required
        - False
    - type
        - bool

##### ENABLE_RS_REDIST_DIRECT

???+ "Details"

    - default
        - False
    - description
        - For auto-created Multi-Site overlay IFCs in Route Servers. Applicable only when Multi-Site Overlay IFC Deployment Method is Centralized_To_Route_Server.
    - required
        - False
    - type
        - bool

##### FABRIC_NAME

???+ "Details"

    - default
        - 
    - description
        - Please provide the fabric name to create it (Max Size 64)
    - required
        - False
    - type
        - str

##### L2_SEGMENT_ID_RANGE

???+ "Details"

    - default
        - 30000-49000
    - description
        - 'Overlay Network Identifier Range '
    - required
        - False
    - type
        - str

##### L3_PARTITION_ID_RANGE

???+ "Details"

    - default
        - 50000-59000
    - description
        - 'Overlay VRF Identifier Range '
    - required
        - False
    - type
        - str

##### LOOPBACK100_IP_RANGE

???+ "Details"

    - default
        - 10.10.0.0/24
    - description
        - Typically Loopback100 IP Address Range
    - required
        - False
    - type
        - str

##### MS_IFC_BGP_AUTH_KEY_TYPE

???+ "Details"

    - choices
        - 3
        - 7
    - default
        - 3
    - description
        - BGP Key Encryption Type: 3 - 3DES, 7 - Cisco
    - required
        - False
    - type
        - int

##### MS_IFC_BGP_PASSWORD

???+ "Details"

    - default
        - 
    - description
        - Encrypted eBGP Password Hex String
    - required
        - False
    - type
        - str

##### MS_IFC_BGP_PASSWORD_ENABLE

???+ "Details"

    - default
        - False
    - description
        - eBGP password for Multi-Site underlay/overlay IFCs
    - required
        - False
    - type
        - bool

##### MS_LOOPBACK_ID

???+ "Details"

    - default
        - 100
    - description
        - No description available
    - required
        - False
    - type
        - int

##### MS_UNDERLAY_AUTOCONFIG

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### RP_SERVER_IP

???+ "Details"

    - default
        - 
    - description
        - Multi-Site Route-Server peer list (typically loopback IP address on Route-Server for Multi-Site EVPN peering with BGWs), e.g. 128.89.0.1, 128.89.0.2
    - required
        - False
    - type
        - str

##### RS_ROUTING_TAG

???+ "Details"

    - default
        - 54321
    - description
        - Routing tag associated with Route Server IP for redistribute direct. This is the IP used in eBGP EVPN peering.
    - required
        - False
    - type
        - int

##### TOR_AUTO_DEPLOY

???+ "Details"

    - default
        - False
    - description
        - Enables Overlay VLANs on uplink between ToRs and Leafs
    - required
        - False
    - type
        - bool

##### default_network

???+ "Details"

    - choices
        - Default_Network_Universal
        - Service_Network_Universal
    - default
        - Default_Network_Universal
    - description
        - Default Overlay Network Template For Leafs
    - required
        - False
    - type
        - str

##### default_pvlan_sec_network

???+ "Details"

    - choices
        - Pvlan_Secondary_Network
    - default
        - Pvlan_Secondary_Network
    - description
        - Default PVLAN Secondary Network Template
    - required
        - False
    - type
        - str

##### default_vrf

???+ "Details"

    - choices
        - Default_VRF_Universal
    - default
        - Default_VRF_Universal
    - description
        - Default Overlay VRF Template For Leafs
    - required
        - False
    - type
        - str

##### enableScheduledBackup

???+ "Details"

    - default
        - 
    - description
        - Backup at the specified time. Note: Fabric Backup/Restore functionality is being deprecated for MSD fabrics. Recommendation is to use NDFC Backup & Restore
    - required
        - False
    - type
        - bool

##### network_extension_template

???+ "Details"

    - choices
        - Default_Network_Extension_Universal
    - default
        - Default_Network_Extension_Universal
    - description
        - Default Overlay Network Template For Borders
    - required
        - False
    - type
        - str

##### scheduledTime

???+ "Details"

    - default
        - 
    - description
        - Time (UTC) in 24hr format. (00:00 to 23:59)
    - required
        - False
    - type
        - str

##### vrf_extension_template

???+ "Details"

    - choices
        - Default_VRF_Extension_Universal
    - default
        - Default_VRF_Extension_Universal
    - description
        - Default Overlay VRF Template For Borders
    - required
        - False
    - type
        - str

#### ISN_FABRIC_PARAMETERS

???+ "Details"

    - description
        - ISN (Inter-site Network) fabric specific parameters. 
        - Also known as Multi-Site External Network. 
        - The following parameters are specific to ISN fabrics. 
        - Network infrastructure attached to Border Gateways to interconnect VXLAN EVPN fabrics for Multi-Site and Multi-Cloud deployments. 
        - The indentation of these parameters is meant only to logically group them. 
        - They should be at the same YAML level as FABRIC_TYPE and FABRIC_NAME.

##### AAA_REMOTE_IP_ENABLED

???+ "Details"

    - default
        - False
    - description
        - Enable only, when IP Authorization is enabled in the AAA Server
    - required
        - False
    - type
        - bool

##### AAA_SERVER_CONF

???+ "Details"

    - default
        - 
    - description
        - AAA Configurations
    - required
        - False
    - type
        - str

##### BGP_AS

???+ "Details"

    - default
        - 
    - description
        - 1-4294967295 | 1-65535.0-65535 It is a good practice to have a unique ASN for each Fabric.
    - required
        - False
    - type
        - str

##### BOOTSTRAP_CONF

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs required during device bootup/login e.g. AAA/Radius
    - required
        - False
    - type
        - str

##### BOOTSTRAP_CONF_XE

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs required during device bootup/login e.g. AAA/Radius
    - required
        - False
    - type
        - str

##### BOOTSTRAP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Automatic IP Assignment For POAP
    - required
        - False
    - type
        - bool

##### BOOTSTRAP_MULTISUBNET

???+ "Details"

    - default
        - #Scope_Start_IP, Scope_End_IP, Scope_Default_Gateway, Scope_Subnet_Prefix
    - description
        - 'lines with
    - required
        - False
    - type
        - str

##### CDP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Enable CDP on management interface
    - required
        - False
    - type
        - bool

##### DHCP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Automatic IP Assignment For POAP From Local DHCP Server
    - required
        - False
    - type
        - bool

##### DHCP_END

???+ "Details"

    - default
        - 
    - description
        - End Address For Switch POAP
    - required
        - False
    - type
        - str

##### DHCP_IPV6_ENABLE

???+ "Details"

    - choices
        - DHCPv4
        - DHCPv6
    - default
        - DHCPv4
    - description
        - No description available
    - required
        - False
    - type
        - str

##### DHCP_START

???+ "Details"

    - default
        - 
    - description
        - Start Address For Switch POAP
    - required
        - False
    - type
        - str

##### DOMAIN_NAME

???+ "Details"

    - default
        - 
    - description
        - Domain name for DHCP server PnP block
    - required
        - False
    - type
        - str

##### ENABLE_AAA

???+ "Details"

    - default
        - False
    - description
        - Include AAA configs from Advanced tab during device bootup
    - required
        - False
    - type
        - bool

##### ENABLE_NETFLOW

???+ "Details"

    - default
        - False
    - description
        - Enable Netflow on VTEPs
    - required
        - False
    - type
        - bool

##### ENABLE_NXAPI

???+ "Details"

    - default
        - False
    - description
        - Enable HTTPS NX-API
    - required
        - False
    - type
        - bool

##### ENABLE_NXAPI_HTTP

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### ENABLE_RT_INTF_STATS

???+ "Details"

    - default
        - False
    - description
        - Valid for NX-OS only
    - required
        - False
    - type
        - bool

##### FABRIC_FREEFORM

???+ "Details"

    - default
        - 
    - description
        - Additional supported CLIs for all same OS (e.g. all NxOS or IOS-XE, etc) switches
    - required
        - False
    - type
        - str

##### FABRIC_NAME

???+ "Details"

    - default
        - 
    - description
        - Please provide the fabric name to create it (Max Size 64)
    - required
        - False
    - type
        - str

##### FEATURE_PTP

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### INBAND_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Enable POAP over Inband Interface (Pre-req: Inband Mgmt Knob should be Enabled)
    - required
        - False
    - type
        - bool

##### INBAND_MGMT

???+ "Details"

    - default
        - False
    - description
        - Import switches with inband connectivity
    - required
        - False
    - type
        - bool

##### INTF_STAT_LOAD_INTERVAL

???+ "Details"

    - default
        - 10
    - description
        - 'Time in seconds '
    - required
        - False
    - type
        - int

##### IS_READ_ONLY

???+ "Details"

    - default
        - True
    - description
        - If enabled, fabric is only monitored. No configuration will be deployed
    - required
        - False
    - type
        - bool

##### MGMT_GW

???+ "Details"

    - default
        - 
    - description
        - Default Gateway For Management VRF On The Switch
    - required
        - False
    - type
        - str

##### MGMT_PREFIX

???+ "Details"

    - default
        - 24
    - description
        - No description available
    - required
        - False
    - type
        - int

##### MGMT_V6PREFIX

???+ "Details"

    - default
        - 64
    - description
        - No description available
    - required
        - False
    - type
        - int

##### MPLS_HANDOFF

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### MPLS_LB_ID

???+ "Details"

    - default
        - 101
    - description
        - No description available
    - required
        - False
    - type
        - int

##### MPLS_LOOPBACK_IP_RANGE

???+ "Details"

    - default
        - 10.102.0.0/25
    - description
        - MPLS Loopback IP Address Range
    - required
        - False
    - type
        - str

##### NETFLOW_EXPORTER_LIST

???+ "Details"

    - default
        - 
    - description
        - One or Multiple Netflow Exporters
    - required
        - False
    - type
        - list
    - elements
        - str

##### NETFLOW_MONITOR_LIST

???+ "Details"

    - default
        - 
    - description
        - One or Multiple Netflow Monitors
    - required
        - False
    - type
        - list
    - elements
        - str

##### NETFLOW_RECORD_LIST

???+ "Details"

    - default
        - 
    - description
        - One or Multiple Netflow Records
    - required
        - False
    - type
        - list
    - elements
        - str

##### NETFLOW_SAMPLER_LIST

???+ "Details"

    - default
        - 
    - description
        - One or multiple netflow samplers. Applicable to N7K only
    - required
        - False
    - type
        - list
    - elements
        - str

##### NXAPI_HTTPS_PORT

???+ "Details"

    - default
        - 443
    - description
        - No description available
    - required
        - False
    - type
        - int

##### NXAPI_HTTP_PORT

???+ "Details"

    - default
        - 80
    - description
        - No description available
    - required
        - False
    - type
        - int

##### PM_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### PNP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Enable Plug n Play (Automatic IP Assignment) for Cat9K switches
    - required
        - False
    - type
        - bool

##### POWER_REDUNDANCY_MODE

???+ "Details"

    - choices
        - ps-redundant
        - combined
        - insrc-redundant
    - default
        - ps-redundant
    - description
        - Default Power Supply Mode For Bootstrapped NX-OS Switches
    - required
        - False
    - type
        - str

##### PTP_DOMAIN_ID

???+ "Details"

    - default
        - 0
    - description
        - 'Multiple Independent PTP Clocking Subdomains on a Single Network '
    - required
        - False
    - type
        - int

##### PTP_LB_ID

???+ "Details"

    - default
        - 0
    - description
        - No description available
    - required
        - False
    - type
        - int

##### SNMP_SERVER_HOST_TRAP

???+ "Details"

    - default
        - True
    - description
        - Configure NDFC as a receiver for SNMP traps
    - required
        - False
    - type
        - bool

##### SUBINTERFACE_RANGE

???+ "Details"

    - default
        - 2-511
    - description
        - 'Per Border Dot1q Range For VRF Lite Connectivity '
    - required
        - False
    - type
        - str

##### enableRealTimeBackup

???+ "Details"

    - default
        - 
    - description
        - Backup hourly only if there is any config deployment since last backup
    - required
        - False
    - type
        - bool

##### enableScheduledBackup

???+ "Details"

    - default
        - 
    - description
        - Backup at the specified time
    - required
        - False
    - type
        - bool

##### scheduledTime

???+ "Details"

    - default
        - 
    - description
        - Time (UTC) in 24hr format. (00:00 to 23:59)
    - required
        - False
    - type
        - str

#### IPFM_FABRIC_PARAMETERS

???+ "Details"

    - description
        - IPFM (IP Fabric for Media) fabric specific parameters. 
        - The following parameters are specific to IPFM fabrics. 
        - Fabric for a fully automated deployment of IP Fabric for Media Network with Nexus 9000 switches. 
        - The indentation of these parameters is meant only to logically group them. 
        - They should be at the same YAML level as FABRIC_TYPE and FABRIC_NAME.

##### AAA_REMOTE_IP_ENABLED

???+ "Details"

    - default
        - False
    - description
        - Enable only, when IP Authorization is enabled in the AAA Server
    - required
        - False
    - type
        - bool

##### AAA_SERVER_CONF

???+ "Details"

    - default
        - 
    - description
        - AAA Configurations
    - required
        - False
    - type
        - str

##### ASM_GROUP_RANGES

???+ "Details"

    - default
        - 
    - description
        - ASM group ranges with prefixes (len:4-32) example: 239.1.1.0/25, max 20 ranges. Enabling SPT-Threshold Infinity to prevent switchover to source-tree.
    - required
        - False
    - type
        - list
    - elements
        - str

##### BOOTSTRAP_CONF

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs required during device bootup/login e.g. AAA/Radius
    - required
        - False
    - type
        - str

##### BOOTSTRAP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Automatic IP Assignment For POAP
    - required
        - False
    - type
        - bool

##### BOOTSTRAP_MULTISUBNET

???+ "Details"

    - default
        - #Scope_Start_IP, Scope_End_IP, Scope_Default_Gateway, Scope_Subnet_Prefix
    - description
        - 'lines with
    - required
        - False
    - type
        - str

##### CDP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Enable CDP on management interface
    - required
        - False
    - type
        - bool

##### DHCP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Automatic IP Assignment For POAP From Local DHCP Server
    - required
        - False
    - type
        - bool

##### DHCP_END

???+ "Details"

    - default
        - 
    - description
        - End Address For Switch Out-of-Band POAP
    - required
        - False
    - type
        - str

##### DHCP_IPV6_ENABLE

???+ "Details"

    - choices
        - DHCPv4
    - default
        - DHCPv4
    - description
        - No description available
    - required
        - False
    - type
        - str

##### DHCP_START

???+ "Details"

    - default
        - 
    - description
        - Start Address For Switch Out-of-Band POAP
    - required
        - False
    - type
        - str

##### DNS_SERVER_IP_LIST

???+ "Details"

    - default
        - 
    - description
        - Comma separated list of IP Addresses (v4/v6)
    - required
        - False
    - type
        - str

##### DNS_SERVER_VRF

???+ "Details"

    - default
        - 
    - description
        - One VRF for all DNS servers or a comma separated list of VRFs, one per DNS server
    - required
        - False
    - type
        - str

##### ENABLE_AAA

???+ "Details"

    - default
        - False
    - description
        - Include AAA configs from Manageability tab during device bootup
    - required
        - False
    - type
        - bool

##### ENABLE_ASM

???+ "Details"

    - default
        - False
    - description
        - Enable groups with receivers sending (*,G) joins
    - required
        - False
    - type
        - bool

##### ENABLE_NBM_PASSIVE

???+ "Details"

    - default
        - False
    - description
        - Enable NBM mode to pim-passive for default VRF
    - required
        - False
    - type
        - bool

##### EXTRA_CONF_INTRA_LINKS

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs For All Intra-Fabric Links
    - required
        - False
    - type
        - str

##### EXTRA_CONF_LEAF

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs For All Leafs and Tier2 Leafs As Captured From Show Running Configuration
    - required
        - False
    - type
        - str

##### EXTRA_CONF_SPINE

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs For All Spines As Captured From Show Running Configuration
    - required
        - False
    - type
        - str

##### FABRIC_INTERFACE_TYPE

???+ "Details"

    - choices
        - p2p
    - default
        - p2p
    - description
        - Only Numbered(Point-to-Point) is supported
    - required
        - False
    - type
        - str

##### FABRIC_MTU

???+ "Details"

    - default
        - 9216
    - description
        - . Must be an even number
    - required
        - False
    - type
        - int

##### FABRIC_NAME

???+ "Details"

    - default
        - 
    - description
        - Name of the fabric (Max Size 64)
    - required
        - False
    - type
        - str

##### FEATURE_PTP

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### ISIS_AUTH_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### ISIS_AUTH_KEY

???+ "Details"

    - default
        - 
    - description
        - Cisco Type 7 Encrypted
    - required
        - False
    - type
        - str

##### ISIS_AUTH_KEYCHAIN_KEY_ID

???+ "Details"

    - default
        - 127
    - description
        - No description available
    - required
        - False
    - type
        - int

##### ISIS_AUTH_KEYCHAIN_NAME

???+ "Details"

    - default
        - 
    - description
        - No description available
    - required
        - False
    - type
        - str

##### ISIS_LEVEL

???+ "Details"

    - choices
        - level-1
        - level-2
    - default
        - level-2
    - description
        - Supported IS types: level-1, level-2
    - required
        - False
    - type
        - str

##### ISIS_P2P_ENABLE

???+ "Details"

    - default
        - True
    - description
        - This will enable network point-to-point on fabric interfaces which are numbered
    - required
        - False
    - type
        - bool

##### L2_HOST_INTF_MTU

???+ "Details"

    - default
        - 9216
    - description
        - . Must be an even number
    - required
        - False
    - type
        - int

##### LINK_STATE_ROUTING

???+ "Details"

    - choices
        - ospf
        - is-is
    - default
        - ospf
    - description
        - Used for Spine-Leaf Connectivity
    - required
        - False
    - type
        - str

##### LINK_STATE_ROUTING_TAG

???+ "Details"

    - default
        - 1
    - description
        - Routing process tag for the fabric
    - required
        - False
    - type
        - str

##### LOOPBACK0_IP_RANGE

???+ "Details"

    - default
        - 10.2.0.0/22
    - description
        - Routing Loopback IP Address Range
    - required
        - False
    - type
        - str

##### MGMT_GW

???+ "Details"

    - default
        - 
    - description
        - Default Gateway For Management VRF On The Switch
    - required
        - False
    - type
        - str

##### MGMT_PREFIX

???+ "Details"

    - default
        - 24
    - description
        - No description available
    - required
        - False
    - type
        - int

##### NTP_SERVER_IP_LIST

???+ "Details"

    - default
        - 
    - description
        - Comma separated list of IP Addresses (v4/v6)
    - required
        - False
    - type
        - str

##### NTP_SERVER_VRF

???+ "Details"

    - default
        - 
    - description
        - One VRF for all NTP servers or a comma separated list of VRFs, one per NTP server
    - required
        - False
    - type
        - str

##### NXAPI_VRF

???+ "Details"

    - choices
        - management
        - default
    - default
        - management
    - description
        - VRF used for NX-API communication
    - required
        - False
    - type
        - str

##### OSPF_AREA_ID

???+ "Details"

    - default
        - 0.0.0.0
    - description
        - OSPF Area Id in IP address format
    - required
        - False
    - type
        - str

##### OSPF_AUTH_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### OSPF_AUTH_KEY

???+ "Details"

    - default
        - 
    - description
        - 3DES Encrypted
    - required
        - False
    - type
        - str

##### OSPF_AUTH_KEY_ID

???+ "Details"

    - default
        - 127
    - description
        - No description available
    - required
        - False
    - type
        - int

##### PIM_HELLO_AUTH_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### PIM_HELLO_AUTH_KEY

???+ "Details"

    - default
        - 
    - description
        - 3DES Encrypted
    - required
        - False
    - type
        - str

##### PM_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### POWER_REDUNDANCY_MODE

???+ "Details"

    - choices
        - ps-redundant
        - combined
        - insrc-redundant
    - default
        - ps-redundant
    - description
        - Default power supply mode for the fabric
    - required
        - False
    - type
        - str

##### PTP_DOMAIN_ID

???+ "Details"

    - default
        - 0
    - description
        - 'Multiple Independent PTP Clocking Subdomains on a Single Network '
    - required
        - False
    - type
        - int

##### PTP_LB_ID

???+ "Details"

    - default
        - 0
    - description
        - No description available
    - required
        - False
    - type
        - int

##### PTP_PROFILE

???+ "Details"

    - choices
        - IEEE-1588v2
        - SMPTE-2059-2
        - AES67-2015
    - default
        - SMPTE-2059-2
    - description
        - Enabled on ISL links only
    - required
        - False
    - type
        - str

##### ROUTING_LB_ID

???+ "Details"

    - default
        - 0
    - description
        - No description available
    - required
        - False
    - type
        - int

##### RP_IP_RANGE

???+ "Details"

    - default
        - 10.254.254.0/24
    - description
        - RP Loopback IP Address Range
    - required
        - False
    - type
        - str

##### RP_LB_ID

???+ "Details"

    - default
        - 254
    - description
        - No description available
    - required
        - False
    - type
        - int

##### SNMP_SERVER_HOST_TRAP

???+ "Details"

    - default
        - True
    - description
        - Configure NDFC as a receiver for SNMP traps
    - required
        - False
    - type
        - bool

##### STATIC_UNDERLAY_IP_ALLOC

???+ "Details"

    - default
        - False
    - description
        - Checking this will disable Dynamic Fabric IP Address Allocations
    - required
        - False
    - type
        - bool

##### SUBNET_RANGE

???+ "Details"

    - default
        - 10.4.0.0/16
    - description
        - Address range to assign Numbered IPs
    - required
        - False
    - type
        - str

##### SUBNET_TARGET_MASK

???+ "Details"

    - choices
        - 30
        - 31
    - default
        - 30
    - description
        - Mask for Fabric Subnet IP Range
    - required
        - False
    - type
        - int

##### SYSLOG_SERVER_IP_LIST

???+ "Details"

    - default
        - 
    - description
        - Comma separated list of IP Addresses (v4/v6)
    - required
        - False
    - type
        - str

##### SYSLOG_SERVER_VRF

???+ "Details"

    - default
        - 
    - description
        - One VRF for all Syslog servers or a comma separated list of VRFs, one per Syslog server
    - required
        - False
    - type
        - str

##### SYSLOG_SEV

???+ "Details"

    - default
        - 
    - description
        - 'Comma separated list of Syslog severity values, one per Syslog server '
    - required
        - False
    - type
        - str

#### LAN_CLASSIC_FABRIC_PARAMETERS

???+ "Details"

    - description
        - LAN Classic fabric specific parameters. 
        - The following parameters are specific to Classic LAN fabrics. 
        - Fabric to manage a legacy Classic LAN deployment with Nexus switches. 
        - The indentation of these parameters is meant only to logically group them. 
        - They should be at the same YAML level as FABRIC_TYPE and FABRIC_NAME.

##### AAA_REMOTE_IP_ENABLED

???+ "Details"

    - default
        - False
    - description
        - Enable only, when IP Authorization is enabled in the AAA Server
    - required
        - False
    - type
        - bool

##### AAA_SERVER_CONF

???+ "Details"

    - default
        - 
    - description
        - AAA Configurations
    - required
        - False
    - type
        - str

##### BOOTSTRAP_CONF

???+ "Details"

    - default
        - 
    - description
        - Additional CLIs required during device bootup/login e.g. AAA/Radius
    - required
        - False
    - type
        - str

##### BOOTSTRAP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Automatic IP Assignment For POAP
    - required
        - False
    - type
        - bool

##### BOOTSTRAP_MULTISUBNET

???+ "Details"

    - default
        - #Scope_Start_IP, Scope_End_IP, Scope_Default_Gateway, Scope_Subnet_Prefix
    - description
        - 'lines with
    - required
        - False
    - type
        - str

##### CDP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Enable CDP on management interface
    - required
        - False
    - type
        - bool

##### DHCP_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Automatic IP Assignment For POAP From Local DHCP Server
    - required
        - False
    - type
        - bool

##### DHCP_END

???+ "Details"

    - default
        - 
    - description
        - End Address For Switch POAP
    - required
        - False
    - type
        - str

##### DHCP_IPV6_ENABLE

???+ "Details"

    - choices
        - DHCPv4
        - DHCPv6
    - default
        - DHCPv4
    - description
        - No description available
    - required
        - False
    - type
        - str

##### DHCP_START

???+ "Details"

    - default
        - 
    - description
        - Start Address For Switch POAP
    - required
        - False
    - type
        - str

##### ENABLE_AAA

???+ "Details"

    - default
        - False
    - description
        - Include AAA configs from Advanced tab during device bootup
    - required
        - False
    - type
        - bool

##### ENABLE_NETFLOW

???+ "Details"

    - default
        - False
    - description
        - Enable Netflow on VTEPs
    - required
        - False
    - type
        - bool

##### ENABLE_NXAPI

???+ "Details"

    - default
        - False
    - description
        - Enable HTTPS NX-API
    - required
        - False
    - type
        - bool

##### ENABLE_NXAPI_HTTP

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### FABRIC_FREEFORM

???+ "Details"

    - default
        - 
    - description
        - Additional supported CLIs for all same OS (e.g. all NxOS etc) switches
    - required
        - False
    - type
        - str

##### FABRIC_NAME

???+ "Details"

    - default
        - 
    - description
        - Please provide the fabric name to create it (Max Size 64)
    - required
        - False
    - type
        - str

##### FEATURE_PTP

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### INBAND_ENABLE

???+ "Details"

    - default
        - False
    - description
        - Enable POAP over Inband Interface (Pre-req: Inband Mgmt Knob should be Enabled)
    - required
        - False
    - type
        - bool

##### INBAND_MGMT

???+ "Details"

    - default
        - False
    - description
        - Import switches with inband connectivity
    - required
        - False
    - type
        - bool

##### IS_READ_ONLY

???+ "Details"

    - default
        - True
    - description
        - If enabled, fabric is only monitored. No configuration will be deployed
    - required
        - False
    - type
        - bool

##### MGMT_GW

???+ "Details"

    - default
        - 
    - description
        - Default Gateway For Management VRF On The Switch
    - required
        - False
    - type
        - str

##### MGMT_PREFIX

???+ "Details"

    - default
        - 24
    - description
        - No description available
    - required
        - False
    - type
        - int

##### MGMT_V6PREFIX

???+ "Details"

    - default
        - 64
    - description
        - No description available
    - required
        - False
    - type
        - int

##### MPLS_HANDOFF

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### MPLS_LB_ID

???+ "Details"

    - default
        - 101
    - description
        - No description available
    - required
        - False
    - type
        - int

##### MPLS_LOOPBACK_IP_RANGE

???+ "Details"

    - default
        - 10.102.0.0/25
    - description
        - MPLS Loopback IP Address Range
    - required
        - False
    - type
        - str

##### NETFLOW_EXPORTER_LIST

???+ "Details"

    - default
        - 
    - description
        - One or Multiple Netflow Exporters
    - required
        - False
    - type
        - list
    - elements
        - str

##### NETFLOW_MONITOR_LIST

???+ "Details"

    - default
        - 
    - description
        - One or Multiple Netflow Monitors
    - required
        - False
    - type
        - list
    - elements
        - str

##### NETFLOW_RECORD_LIST

???+ "Details"

    - default
        - 
    - description
        - One or Multiple Netflow Records
    - required
        - False
    - type
        - list
    - elements
        - str

##### NETFLOW_SAMPLER_LIST

???+ "Details"

    - default
        - 
    - description
        - One or multiple netflow Samplers. Applicable to N7K only
    - required
        - False
    - type
        - list
    - elements
        - str

##### NXAPI_HTTPS_PORT

???+ "Details"

    - default
        - 443
    - description
        - No description available
    - required
        - False
    - type
        - int

##### NXAPI_HTTP_PORT

???+ "Details"

    - default
        - 80
    - description
        - No description available
    - required
        - False
    - type
        - int

##### PM_ENABLE

???+ "Details"

    - default
        - False
    - description
        - No description available
    - required
        - False
    - type
        - bool

##### POWER_REDUNDANCY_MODE

???+ "Details"

    - choices
        - ps-redundant
        - combined
        - insrc-redundant
    - default
        - ps-redundant
    - description
        - Default Power Supply Mode For Bootstrapped NX-OS Switches
    - required
        - False
    - type
        - str

##### PTP_DOMAIN_ID

???+ "Details"

    - default
        - 0
    - description
        - 'Multiple Independent PTP Clocking Subdomains on a Single Network '
    - required
        - False
    - type
        - int

##### PTP_LB_ID

???+ "Details"

    - default
        - 0
    - description
        - No description available
    - required
        - False
    - type
        - int

##### SNMP_SERVER_HOST_TRAP

???+ "Details"

    - default
        - True
    - description
        - Configure NDFC as a receiver for SNMP traps
    - required
        - False
    - type
        - bool

##### SUBINTERFACE_RANGE

???+ "Details"

    - default
        - 2-511
    - description
        - 'Per Border Dot1q Range For VRF Lite Connectivity '
    - required
        - False
    - type
        - str

##### enableRealTimeBackup

???+ "Details"

    - default
        - False
    - description
        - Backup hourly only if there is any config deployment since last backup
    - required
        - False
    - type
        - bool

##### enableScheduledBackup

???+ "Details"

    - default
        - False
    - description
        - Backup at the specified time
    - required
        - False
    - type
        - bool

##### scheduledTime

???+ "Details"

    - default
        - 
    - description
        - Time (UTC) in 24hr format. (00:00 to 23:59)
    - required
        - False
    - type
        - str
