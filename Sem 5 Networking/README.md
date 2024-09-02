# Interchange IP Addresses on Cisco Router

To resolve the overlapping IP address issue and interchange the IP addresses between `FastEthernet0/0` and `FastEthernet0/1`, follow these steps:

## Current Configuration:
- **FastEthernet0/0** has IP `192.168.1.100`.
- **FastEthernet0/1** has IP `16.0.0.100`.

## Steps to Interchange IP Addresses:

1. **Enter Global Configuration Mode:**
   Access global configuration mode on your router.

```bash
Router# configure terminal
Router(config)# interface FastEthernet0/0
Router(config-if)# no ip address
Router(config-if)# exit

Router(config)# interface FastEthernet0/1
Router(config-if)# no ip address
Router(config-if)# exit


Router(config)# interface FastEthernet0/0
Router(config-if)# ip address 16.0.0.100 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit

Router(config)# interface FastEthernet0/1
Router(config-if)# ip address 192.168.1.100 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit


Router# show ip interface brief

Router# show ip interface brief

Router# show ip interface brief
```



Only 24 Hours For Networking (With Consistency)

1. https://www.youtube.com/playlist?list=PLVFyjfF2Drdt9hXs37KTPTIqtNVCXFfOG <br>
   https://github.com/alihaghshenas/cisco-packet-tracer-cource

2. https://www.youtube.com/playlist?list=PLB57s6OrG8LjS4rXfvYZd95H5oHPabDcF

3. https://www.youtube.com/playlist?list=PLXP9Twz5n6qrPsZ8eJCc2TiSWMEEUi1O8

4. https://www.youtube.com/playlist?list=PLZURQ_XyXLwDBCD6BtfRP-Bc9DM4_U1Om

5. https://www.youtube.com/playlist?list=PLhEyzxBNToCroL2HjrsoLAOtcS88fwc9M

6. https://www.youtube.com/playlist?list=PL71kSR7neg7KpyPqlq3jgw0RMKU3XHljL



---
Cisco Packet tracer Shortcut keys

https://mahi130.wordpress.com/2011/06/21/packet-tracer-shortcuts/

---
Cisco Packet Tracer Github repos
