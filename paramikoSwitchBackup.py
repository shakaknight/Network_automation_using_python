#taking up data of the switches.
# you have the ip address in the text file.
import paramiko
import time 
import getpass

username = raw_input("Enter your username:")
password = getpass.getpass()

f = open ("myswitches.txt")


for line in f:

	ip_address = line.strip()
	ssh_client = paramiko.SSHCLIENT()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip_address,username=username,password=password)

	print "Successful connection:",ip_address

	remote_connection = ssh_client.invoke_shell()

	print "Getting Running-config of " + ip_address

	remote_connection.send("terminal length 0\n")
	remote_connection.send("show run")
	remote_connection.send("exit\n")

	time.sleep(20)
	readoutput = remote_connection.recv(655350)
	saveoutput = open("Backup_Switch_" + ip_address,"w")
	print "Saving configuration in Backup_Switch_ "+ip_address
	saveoutput.write(readoutput)
	saveoutput.write("\n")

	saveoutput.close