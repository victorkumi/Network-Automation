# A network script that telnets into a router and configures
# two loopback interfaces and enables ospf.

# import two modules
import getpass
import telnetlib

HOST = "192.168.122.155"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")


tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")


tn.write(b"int lo0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")

tn.write(b"int lo1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")

tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
