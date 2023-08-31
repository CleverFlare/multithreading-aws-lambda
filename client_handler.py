import json
from globals import DISCONNECT_MESSAGE
import sockets
import requests
import concurrent.futures
import queue

def handle_thread(json_data):
    res = requests.post("https://ewbpmfu54b.execute-api.eu-north-1.amazonaws.com/test/multithreadEventsHandler", data=json_data)
    print(res.json())


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    q = queue.Queue()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

    connected = True
    while connected:
        msg = sockets.recv(conn)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        try:
            recv_json = json.loads(msg)
            q.put(recv_json)
        except json.decoder.JSONDecodeError:
            sockets.send(conn,"You haven't sent a valid JSON object")

        while not q.empty():
            queued_msg = q.get()
            executor.submit(handle_thread, queued_msg)
            
    conn.close()




