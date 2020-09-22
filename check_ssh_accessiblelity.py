#taking up data of the switches.
# you have the ip address in the text file.
import paramiko
import time 
import getpass

username = raw_input("Enter your username:")
password = getpass.getpass()

f = open ("myswitches.txt")


for line in f:
	try:
		ip_address = line.strip()
		ssh_client = paramiko.SSHCLIENT()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname=ip_address,username=username,password=password)


		remote_connection = ssh_client.invoke_shell()

		remote_connection.send("exit\n")
	except:
		remote_connection = ("socket.error")
		
	result = remote_connection

	if result == "socket.error":
		print ip_address,"Not Accessible"
	else
		print ip_address,"Accessible"
	raw_input("Connectivity check done,press enter to exit:")