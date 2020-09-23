from netmiko import ConnectHandler

iosv_12 = {
	'device type' : 'cisco_ios',
	'ip' : '172.16.16.20',
	'username' : 'rahul',
	'password' : 'cisco',
}

net_connect = ConnectHandler(**iosv_12)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')#aauto enable mode
print output

config_commands = {}
output = net_connect.send_config_set(config_commands)#auto config mode
print output

for n in range (2,21)
	print "Creating VLAN" + str(n)
	config_commands = ('VLAN') +str(n), 'name Python_Vlan' + str(n)]
	output = net_connect.send_config_set(config_commands)
	print output

	