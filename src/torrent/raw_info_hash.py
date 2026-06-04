TORRENT_FILE = "torrents/ubuntu.torrent"


def main():

    with open(TORRENT_FILE, "rb") as file:
        torrent_bytes = file.read()

    info_marker = b"4:info"

    marker_position = torrent_bytes.find(info_marker)

    if marker_position == -1:
        raise ValueError("Info dictionary not found.")

    info_start = marker_position + len(info_marker)

    print("Info Dictionary Starts At:")

    print(info_start)

    nesting_level = 0

    for i in range(info_start, len(torrent_bytes)):

        current_byte = bytes([torrent_bytes[i]])

        if current_byte in (b"d", b"l"):
            nesting_level += 1

        elif current_byte == b"e":
            nesting_level -= 1

            if nesting_level == 0:
                info_end = i + 1
                break

    print("\nInfo Dictionary Ends At:")

    print(info_end)

    print("\nInfo Dictionary Size:")

    print(info_end - info_start)


if __name__ == "__main__":
    main()