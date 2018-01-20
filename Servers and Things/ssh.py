#!/usr/bin/python
from sshtunnel import SSHTunnelForwarder
from time import sleep

with SSHTunnelForwarder(
    ssh_address_or_host = ('35.185.84.51', 22),
    ssh_username="alabaster_snowball",
    ssh_password="stream_unhappy_buy_loss",
    local_bind_address = ('localhost',9050),
    remote_bind_address=('10.142.0.7', 445),
) as server:

    print(server.local_bind_port)
    while True:
    
        sleep(1)

print('FINISH!')
