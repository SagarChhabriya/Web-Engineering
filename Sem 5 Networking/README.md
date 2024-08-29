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