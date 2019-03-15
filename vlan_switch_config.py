#!/usr/bin/env python3
#A script that logs into switches and configures vlan on each switch

import getpass
import telnetlib


user = input("Enter your telnet username: ")
password = getpass.getpass()


for n in range(150,155):
        HOST = "192.168.122." + str(n)
        tn = telnetlib.Telnet(HOST)

        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")

        tn.write(b"conf t\n")

        for n in range(2,15):
                tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
                tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
                tn.write(b"exit\n")

        tn.write(b"end\n")

        print(tn.read_all().decode('ascii'))