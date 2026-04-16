import socket  # noqa: F401
import threading

def handle_connection(conn: socket.socket):
    _ = conn.recv(1024)
    conn.sendall(b"+PONG\r\n")

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment the code below to pass the first stage
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    try:
        while True:
            conn, _ = server_socket.accept()
            threading.Thread(target=handle_connection, args=(conn))
    except:
        conn.close()

if __name__ == "__main__":
    main()
