import socket

from src.peer.handshake import parse_handshake

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

    parsed = parse_handshake(handshake)

    print("\n===== HANDSHAKE VALIDATION =====\n")

    print("Protocol Length:")

    print(parsed["protocol_length"])

    print("\nProtocol:")

    print(parsed["protocol"])

    print("\nPeer ID:")

    print(parsed["peer_id"])

    print("\nInfo Hash:")

    print(parsed["info_hash"].hex())

    if parsed["protocol"] == b"BitTorrent protocol":
        print("\nVALID BITTORRENT PEER")
    else:
        print("\nINVALID PROTOCOL")

    client_socket.close()

    server_socket.close()


if __name__ == "__main__":
    main()