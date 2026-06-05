import socket

from src.peer.handshake import (
    get_info_hash,
    build_handshake
)

TORRENT_FILE = "torrents/ubuntu.torrent"

HOST = "127.0.0.1"
PORT = 6881


def main():

    with open(TORRENT_FILE, "rb") as file:
        torrent_bytes = file.read()

    info_hash = get_info_hash(torrent_bytes)

    peer_id = b"-PC0001-123456789012"

    handshake = build_handshake(
        info_hash,
        peer_id
    )

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client_socket.connect((HOST, PORT))

    print("Connected!")

    client_socket.send(handshake)

    print("Handshake sent!")

    client_socket.close()


if __name__ == "__main__":
    main()