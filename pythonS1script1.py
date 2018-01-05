import getpass
import sys
import telnetlib

user = raw_input("Enter username")
password = getpass.getpass()

for index in range (72,77):
    Host = "192.168.122." + str(index)
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "n/")
    tn.write("conf t\n") #configuration mode

    #configure loopback address for router1
    for index in range (2,7):
        tn.write("vlan " + str(index) + "\n")
        tn.write("desc Python_VLAN_" + str(index) + "\n")
        tn.write("exit\n")

        th.write("end\n")
        th.write("wr\n")
        tn.write("exit\n")

        print tn.read_all()
