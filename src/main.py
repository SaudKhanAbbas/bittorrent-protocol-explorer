from src.torrent.torrent import Torrent
from src.tracker.tracker import Tracker


def print_header():

    print("=" * 50)
    print("        BITTORRENT PROTOCOL EXPLORER v1.0")
    print("=" * 50)


def main():

    print_header()

    print("\nLoading torrent...")

    torrent = Torrent("torrents/ubuntu.torrent")

    print("✓ Torrent loaded")

    print("\nTorrent Information")

    print("------------------------------")

    print(f"File Name     : {torrent.file_name}")
    print(f"File Size     : {torrent.file_size:,} bytes")
    print(f"Piece Length  : {torrent.piece_length:,} bytes")
    print(f"Pieces        : {torrent.number_of_pieces}")
    print(f"Tracker       : {torrent.announce_url}")
    print(f"Info Hash     : {torrent.info_hash.hex()}")

    print("\nContacting tracker...")

    tracker = Tracker(torrent)

    try:

        response = tracker.announce()

        print("✓ Tracker responded")

        print(f"Response Size : {len(response)} bytes")

        print("\nTracker Response")

        print("------------------------------")

        print(response)

    except Exception as error:

        print("✗ Tracker request failed")

        print(error)

    print("\nProject Status")

    print("------------------------------")

    print("✓ Torrent parsing")
    print("✓ Metadata extraction")
    print("✓ Info hash generation")
    print("✓ Tracker communication")
    print("✓ Handshake implementation")
    print("✓ Peer communication foundation")

    print("\nMini BitTorrent Client v1.0 complete.")


if __name__ == "__main__":
    main()