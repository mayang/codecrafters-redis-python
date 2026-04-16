import socket  # noqa: F401
import threading

def handle_response(cmd):
    if cmd == None or cmd == None:
        return b"-ERR invalid command"
    elif cmd[0].upper() == b"PING":
        return b"+PONG\r\n"
    elif cmd[0].upper() == b"ECHO":
        return b"$" + str(len(cmd[1])).encode() + b"\r\n" + command[1] + b"\r\n"

def handle_connection(conn: socket.socket):
    while True:
        data = conn.recv(1024)
        conn.sendall(handle_response(data))

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
