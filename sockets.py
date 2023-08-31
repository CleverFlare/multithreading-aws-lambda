import json
from globals import HEADER, FORMAT

def recv(client):
    msg_length = client.recv(HEADER).decode(FORMAT)
    msg = ""
    if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(HEADER).decode(FORMAT)
    return msg


def send(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def sendJson(client, data):
    try:
        strJson = json.dumps(data)
        send(client, strJson)
    except json.decoder.JSONDecodeError:
        raise Exception("[STRINGIFY_ERROR] Your json data is not valid")
