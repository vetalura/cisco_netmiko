import netmiko
from netmiko import ConnectHandler


cisco_router_1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101',
    'port': '22',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'class'
    }

    sshcli = ConnectHandler(**cisco_router_1)
    sshcli.enable()

output = sshcli.send_command("show ip interface brief")
print("show ip interface brief:\n{}\n".format(output))

config_command_1 = [
'int Gigabit Ethernet 0/1',
'ip address 192.168.1.1 255.255.255.0',
'description WHATEVER LAN to PC'
'no shutdown'
]
output = sshcli.send_config_set(config_command_1)
print("Configure int gi0/1:\n{}\n".format(output))


config_command_2 = [
'int Gigabit Ethernet 0/0',
'ip address 192.168.0.1 255.255.255.0',
'description WHATEVER LAN to PC-B'
'no shutdown'
]
output = sshcli.send_config_set(config_command_2)
print("Configure int gi0/0:\n{}\n".format(output))

output = sshcli.send_command("show ip int brief")
print("show ip interface brief:\n{}\n".format(output))

sshcli.exit_enable_mode()
sshcli.disconnect()