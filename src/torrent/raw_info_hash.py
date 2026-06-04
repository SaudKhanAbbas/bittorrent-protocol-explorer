import hashlib

TORRENT_FILE = "torrents/ubuntu.torrent"


def main():

    with open(TORRENT_FILE, "rb") as file:
        torrent_bytes = file.read()

    info_marker = b"4:info"

    marker_position = torrent_bytes.find(info_marker)

    if marker_position == -1:
        raise ValueError("Info dictionary not found.")

    info_start = marker_position + len(info_marker)

    nesting_level = 0

    info_end = None

    for i in range(info_start, len(torrent_bytes)):

        current_byte = bytes([torrent_bytes[i]])

        if current_byte in (b"d", b"l"):
            nesting_level += 1

        elif current_byte == b"e":
            nesting_level -= 1

            if nesting_level == 0:
                info_end = i + 1
                break

    if info_end is None:
        raise ValueError("Could not determine end of info dictionary.")

    info_bytes = torrent_bytes[info_start:info_end]

    info_hash = hashlib.sha1(info_bytes).hexdigest()

    print("\n===== REAL INFO HASH =====\n")

    print(info_hash)

    print("\nInfo Dictionary Size:")

    print(len(info_bytes))


if __name__ == "__main__":
    main()