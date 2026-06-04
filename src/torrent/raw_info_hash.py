import hashlib

TORRENT_FILE = "torrents/ubuntu.torrent"


def main():

    with open(TORRENT_FILE, "rb") as file:
        torrent_bytes = file.read()

    info_start = torrent_bytes.find(b"4:info")

    if info_start == -1:
        raise ValueError("Could not find info dictionary.")

    print("Found info dictionary at byte:")

    print(info_start)

    print("\nNOTE:")

    print(
        "This is only the first step. "
        "We still need the exact end of the info dictionary."
    )


if __name__ == "__main__":
    main()