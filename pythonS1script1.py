import getpass
import sys
import telnetlib

Host = "192.168.122.72"
user = raw_input("Enter username")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "n/")

#configure loopback address for router1
tn.write("enable\n") #enter privileged exec mode
tn.write("cisco\n") #password
tn.write("config t\n") #configuration mode
for index in range (2,6):
    tn.write("vlan "+ str(index)+"\n")
    tn.write("desc Python_VLAN_"+str(index)+"\n")
    tn.write("exit\n")

th.write("end\n")
tn.write("exit\n")

print tn.read_all()
