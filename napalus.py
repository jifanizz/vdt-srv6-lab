from napalm import get_network_driver

driver = get_network_driver('iosxr_netconf')

device = driver('172.20.2.201', 'cisco', 'cisco123')

device.open()
# print device.get_facts() ## doesn't work

print(device.get_interfaces())
print(device.get_interfaces_counters())
print(device.get_users())

device.close()