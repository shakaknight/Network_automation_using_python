from netmiko import ConnectHandler

iosv_12_s1 = {
	'device type' : 'cisco_ios',
	'ip' : '172.16.16.20',
	'username' : 'rahul',
	'password' : 'cisco',
}

iosv_12_s2 = {
	'device type' : 'cisco_ios',
	'ip' : '172.16.16.21',
	'username' : 'rahul',
	'password' : 'cisco',
}

iosv_12_s3 = {
	'device type' : 'cisco_ios',
	'ip' : '172.16.16.22',
	'username' : 'rahul',
	'password' : 'cisco',
}

with open('iosv_12_config.txt') as f;
	lines = f.read().splitline()
print lines

all_devices = {iosv_12_s1,iosv_12_s2,iosv_12_s3}

for devices in all_devices
	net_connect = ConnectHandler(**devices)
	#net_connect.find_prompt()
	output = net_connect.send_config_set(lines)
	#auto enable mode
	print output


	