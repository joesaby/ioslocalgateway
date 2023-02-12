BASE_WXC_CONFIG = '''
voice service voip
 ip address trusted list
  ipv4 173.37.69.0
  ipv4 173.37.68.248
  ipv4 173.37.69.42
  ipv4 173.37.68.226
  ipv4 10.0.0.57
  ipv4 10.0.0.59
  ipv4 10.53.53.59
  ipv4 10.53.44.223
  ipv4 135.84.175.12
  ipv4 135.84.175.11
  ipv4 135.84.175.139
  ipv4 173.37.69.32
  ipv4 135.84.175.142
  ipv4 135.84.172.116
  ipv4 135.84.171.116
  ipv4 139.177.73.10
  ipv4 139.177.73.11
  ipv4 139.177.72.11
  ipv4 139.177.66.10
  ipv4 139.177.66.11
  ipv4 139.177.71.10
  ipv4 139.177.70.11
  ipv4 139.177.70.10
  ipv4 139.177.68.10
  ipv4 139.177.68.11
  ipv4 10.123.184.183
  ipv4 10.53.56.152
  ipv4 10.123.184.236
  ipv4 10.65.63.248
  ipv4 139.177.72.10
  ipv4 139.177.64.11
  ipv4 139.177.64.13
  ipv4 139.177.71.11
  ipv4 139.177.69.11
  ipv4 139.177.69.10
  ipv4 139.177.67.11
  ipv4 139.177.67.10
  ipv4 139.177.65.11
  ipv4 139.177.65.13
  ipv4 10.53.44.207
  ipv4 10.123.184.149
  ipv4 170.72.17.128 255.255.255.128
  ipv4 170.72.29.0 255.255.255.0
  ipv4 150.253.133.0 255.255.255.0
  ipv4 173.39.236.0 255.255.255.0
  ipv4 207.182.170.0 255.255.254.0
  ipv4 207.182.188.0 255.255.254.0
  ipv4 170.72.82.0 255.255.255.0
  ipv4 139.177.64.41
  ipv4 139.177.65.12
  ipv4 139.177.64.45
  ipv4 150.253.209.128 255.255.255.128
  ipv4 23.89.1.128 255.255.255.128
  ipv4 23.89.40.0 255.255.255.128
  ipv4 139.177.64.12
  ipv4 23.89.154.0 255.255.255.128
  ipv4 170.72.242.0 255.255.255.0
 no ip address trusted authenticate
 media statistics
 media bulk-stats
 allow-connections sip to sip
 no supplementary-service sip refer
 no supplementary-service sip handle-replaces
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none
 stun
  stun flowdata agent-id 1 boot-count 31
  stun flowdata shared-secret 7 01100F175804575D72184D000A0618
 sip
  early-offer forced
  g729 annexb-all
!
voice class codec 99
 codec preference 1 g711ulaw
 codec preference 2 g711alaw
!
voice class stun-usage 1
 stun usage firewall-traversal flowdata
!
!
crypto pki trustpoint ciscoCATrustpoint
 revocation-check crl
crypto pki trustpool import clean url http://www.cisco.com/security/pki/trs/ios.p7b
!
sip-ua 
 transport tcp tls v1.2
 xfer target dial-peer
 crypto signaling default trustpoint ciscoCATrustpoint 
!
!
line con 0
 stopbits 1
!
!
'''

VOICE_CLASS_VOIP = '''voice service voip
 no ip address trusted authenticate
 media statistics
 media bulk-stats
 media stats-disconnect
 allow-connections sip to sip
 no supplementary-service sip refer
 no supplementary-service sip handle-replaces
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none
 stun
  stun flowdata agent-id 1 boot-count 56
  stun flowdata shared-secret 7 01100F175804575D72184D000A0618
 sip
  early-offer forced
  g729 annexb-all'''

STUN_USAGE = '''!
voice class stun-usage {{stun_usage_id}}
 stun usage firewall-traversal flowdata'''

STUN_USAGE_ICE = '''!
 voice class stun-usage {{stun_usage_id}}
  stun usage firewall-traversal flowdata
  stun usage ice lite'''

URI_FILTER_PORT = '''voice class uri {{filter_id}} sip
 pattern :{{PORT}}'''

URI_FILTER_HOST = '''voice class uri {{filter_id}} sip
 pattern host={{IP_ADDRESS}}'''

URI_FILTER_OTG = '''voice class uri {{filter_id}} sip
 pattern otg={{TRUNK_GROUP}}'''

URI_FILTER_DTG = '''voice class uri {{filter_id}} sip
 pattern dtg={{TRUNK_GROUP}}'''

DIAL_PEER_GROUP = '''voice class dpg {{dpg_id}}
 dial-peer {{outbound_dpg_id}} preference 1'''

OUTBOUND_DIAL_PEER_TO_WXC = '''dial-peer voice {{dial_peer_id}} voip
 description Outgoing dial-peer to BroadCloud TO TG {{TRUNK_GROUP}}
 destination-pattern .T
 session protocol sipv2
 session target sip-server
 voice-class stun-usage {{stun_usage_id}}
 voice-class sip tenant {{sip_tenant_id}}
 dtmf-relay rtp-nte
 voice-class codec 99
 fax-relay ecm disable
 fax-relay sg3-to-g3
 fax rate 2400
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback pass-through g711ulaw
 srtp
 no vad'''

OUTBOUND_DIAL_PEER_TO_PBX = '''dial-peer voice {{dial_peer_id}} voip
 description Outgoing dial-peer to IP PSTN TO TG {{TRUNK_GROUP}}
 destination-pattern .T
 session protocol sipv2
 session target ipv4:{{cube_ip_address}}
 session transport udp
 voice-class stun-usage {{stun_usage_id}}
 voice-class sip tenant {{sip_tenant_id}}
 dtmf-relay rtp-nte
 codec transparent
 fax rate 2400
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none
 no vad'''

INBOUND_DIAL_PEER_FROM_WXC = '''dial-peer voice {{dial_peer_id}} voip
 description Incoming dial-peer from SBC for TG {{TRUNK_GROUP}}
 session protocol sipv2
 destination dpg {{destination_dpg_id}}
 incoming uri request {{incoming_uri_id}}
 voice-class stun-usage {{stun_usage_id}}
 voice-class sip tenant {{sip_tenant_id}}
 dtmf-relay rtp-nte
 voice-class codec 99
 srtp
 no vad'''


INBOUND_DIAL_PEER_FROM_SIP_SERVER = '''dial-peer voice {{dial_peer_id}} voip
 description Incoming dial-peer from PSTN FOR TG {{TRUNK_GROUP}}
 session protocol sipv2
 destination dpg {{destination_dpg_id}}
 incoming uri via {{incoming_uri_id}}
 voice-class stun-usage {{stun_usage_id}}
 voice-class sip tenant {{sip_tenant_id}}
 dtmf-relay rtp-nte
 voice-class codec 99
 fax-relay ecm disable
 fax-relay sg3-to-g3
 fax rate 2400
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback pass-through g711ulaw
 no vad'''

INBOUND_DIAL_PEER_FROM_PBX = '''dial-peer voice {{dial_peer_id}} voip
 description Incoming dial-peer from PSTN FOR TG {{TRUNK_GROUP}}
 session protocol sipv2
 destination dpg {{destination_dpg_id}}
 incoming uri from {{incoming_uri_id}}
 voice-class stun-usage {{stun_usage_id}}
 voice-class sip tenant {{sip_tenant_id}}
 dtmf-relay rtp-nte
 voice-class codec 99
 fax-relay ecm disable
 fax-relay sg3-to-g3
 fax rate 2400
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback pass-through g711ulaw
 no vad'''

SIP_PROFILE = '''voice class sip-profiles {{code}}
 rule 1 request ANY sip-header SIP-Req-URI modify "sips:" "sip:" 
 rule 10 request ANY sip-header To modify "<sips:" "<sip:" 
 rule 11 request ANY sip-header From modify "<sips:" "<sip:" 
 rule 12 request ANY sip-header Contact modify "<sips:(.*)>" "<sip:\\1;transport=tls>" 
 rule 13 response ANY sip-header To modify "<sips:" "<sip:" 
 rule 14 response ANY sip-header From modify "<sips:" "<sip:" 
 rule 15 response ANY sip-header Contact modify "<sips:" "<sip:" 
 rule 16 request ANY sip-header From modify ">" ";otg={{TRUNK_GROUP}}>" 
 rule 17 request ANY sip-header P-Asserted-Identity modify "<sips:" "<sip:" 
 rule 18 request INVITE sip-header Diversion remove '''

CUBE_TO_PBX_TENANT = '''voice class tenant {{tenant_id}}
  session transport tcp
  url sip
  error-passthru
  asserted-id pai
  bind control source-interface {{GigabitEthernet}}
  bind media source-interface {{GigabitEthernet}}
  no pass-thru headers
  no pass-thru content custom-sdp
  sip-profiles {{sip_profile_id}}'''

CUBE_TO_WXC_TLS_TENANT = '''voice class tenant {{tenant_id}}
  registrar dns:{{registrar_domain}} scheme sips expires 240 refresh-ratio 50 tcp tls
  credentials number {{user_lineport}} username {{username}} password 0 {{user_password}} realm BroadWorks
  authentication username {{username}} password 0 {{user_password}}  realm BroadWorks
  authentication username {{username}} password 0 {{user_password}}  realm {{registrar_domain}}
  sip-server dns:{{registrar_domain}}
  connection-reuse
  session transport tcp tls
  url sips
  error-passthru
  bind control source-interface {{GigabitEthernet}}
  bind media source-interface {{GigabitEthernet}}
  no pass-thru content custom-sdp
  sip-profiles {{sip_profile_id}}
  outbound-proxy dns:{{outbound_proxy}}'''

