import socket

HOST = "127.0.0.1"
PORT = 6881


def main():

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.bind((HOST, PORT))

    server_socket.listen()

    print(f"Listening on {HOST}:{PORT}")

    client_socket, client_address = server_socket.accept()

    print(f"\nConnection from {client_address}")

    handshake = client_socket.recv(68)

    print("\nReceived Handshake:\n")

    print(handshake)

    client_socket.close()

    server_socket.close()


if __name__ == "__main__":
    main()