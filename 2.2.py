import netmiko
from netmiko import ConnectHandler

sshcli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.56.101',
    port = '22',
    username = 'cisco',
    password = 'cisco123!'
)

output = sshcli.send_command("show ip interface brief")
print("show ip interface brief:\n{}\n".format(output))

config_command_1 = [
'int loopback 1',
'ip address 2.2.2.2 255.255.255.0',
'description WHATEVER This int was configured with netmiko'
]
output = sshcli.send_config_set(config_command_1)
print("Configure int lo1:\n{}\n".format(output))

output = sshcli.send_command("show ip interface brief")
print("show ip interface brief:\n{}\n".format(output))

config_command_2 = [
'int loopback 2',
'ip address 1.1.1.1 255.255.255.0',
'description WHATEVER This int lo2 was configured with netmiko'
]
output = sshcli.send_config_set(config_command_2)
print("Configure int lo2:\n{}\n".format(output))

output = sshcli.send_command("show interface description")
print("show ip interface brief:\n{}\n".format(output))