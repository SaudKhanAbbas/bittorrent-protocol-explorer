import hashlib
import urllib.parse
import urllib.request

TORRENT_FILE = "torrents/ubuntu.torrent"


def get_raw_info_hash(torrent_bytes):

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
        raise ValueError("Could not find end of info dictionary.")

    info_bytes = torrent_bytes[info_start:info_end]

    return hashlib.sha1(info_bytes).digest()


def main():

    with open(TORRENT_FILE, "rb") as file:
        torrent_bytes = file.read()

    info_hash = get_raw_info_hash(torrent_bytes)

    peer_id = b"-PC0001-123456789012"

    tracker_url = (
        "https://torrent.ubuntu.com/announce"
        f"?info_hash={urllib.parse.quote_from_bytes(info_hash)}"
        f"&peer_id={peer_id.decode()}"
        "&port=6881"
        "&uploaded=0"
        "&downloaded=0"
        "&left=0"
        "&compact=1"
    )

    print("\nConnecting to tracker...\n")

    response = urllib.request.urlopen(tracker_url)

    tracker_response = response.read()

    print("Response Length:")

    print(len(tracker_response))

    print("\nRaw Response:\n")

    print(tracker_response)


if __name__ == "__main__":
    main()