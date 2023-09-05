import socket
import json
import time
from globals import ADDR
import sockets

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

event = {
    "name": "Muhammad"
}

while True:
    sockets.send(client, json.dumps(event))
    time.sleep(1)


