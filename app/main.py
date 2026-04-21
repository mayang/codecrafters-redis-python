import socket  # noqa: F401
import threading
from app.store import Store

store = Store()

def parse_response(data):
    if not data or data[0] != ord(b"*"):
        return None

    parts = data.split(b"\r\n")

    try:
        num_elements = int(parts[0][1:])
        elems = parts[2::2]
    except:
        return None

    # if nothing or len(rest of parts) does not match num_elements
    # return None
    if len(elems) != num_elements:
        return None

    return elems 

def handle_response(cmd):
    if cmd == None:
        return b"-ERR invalid command\r\n"
    elif cmd[0].upper() == b"PING":
        return b"+PONG\r\n"
    elif cmd[0].upper() == b"ECHO":
        return b"$" + str(len(cmd[1])).encode() + b"\r\n" + cmd[1] + b"\r\n"
    elif cmd[0].upper() == b"SET":
        if len(cmd) == 3:
            return store.set(cmd[1], cmd[2])
        elif len(cmd) == 5:
            return store.set(cmd[1], cmd[2], cmd[3], cmd[4])
        else:
            return b"-ERR invalid arguments\r\n"
    elif cmd[0].upper() == b"GET":
        return store.get(cmd[1]) 

def handle_connection(conn: socket.socket):
    while True:
        data = conn.recv(1024)
        conn.sendall(handle_response(parse_response(data)))

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    try:
        while True:
            conn, _ = server_socket.accept()
            threading.Thread(target=handle_connection, args=(conn,)).start()
    except:
        conn.close()

if __name__ == "__main__":
    main()
