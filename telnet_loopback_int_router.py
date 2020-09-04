import getpass
import sys	
import telnetlib

HOST = raw_input("Enter Device IP:")
USER = raw_input("Enter Your Telnet Username:")
password = getpass.getpass()

tn = tellnetlib.Telnet(HOST)

tn.read_untill("Username: ")
tn.write(user + "\n")
if password:
	tn.read_until("Password: ")
	tn.write(password + "\n")

tn.write("enabling\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loop 0\1\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()