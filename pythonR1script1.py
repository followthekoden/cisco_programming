import getpass
import sys
import telnetlib

Host = "192.168.122.71"
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
tn.write("int loop 0\n") #select interface loopback 0
tn.write("ip add 1.1.1.1 255.255.255.255\n") #assign ip address
tn.write("int loop 1\n") #select interface loopback 1
tn.write("ip add 2.2.2.2 255.255.255.255\n") #assign ip address
tn.write("router ospf 1\n") #assign routing protocol (open shortest path first)
tn.write("network 0.0.0.0 255.255.255.255 area 0\n") #assign area
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()