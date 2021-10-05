
import socket
#socket project
print(socket.getfqdn())
name = input('Enter host name of your choise\n')
socket.sethostname(name)
# sadly it's only available on UNIX for the moment.

# default LAPTOP-N9O96HRM
