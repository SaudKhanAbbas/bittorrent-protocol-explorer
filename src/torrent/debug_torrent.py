TORRENT_FILE = "torrents/ubuntu.torrent"


def main():

    with open(TORRENT_FILE, "rb") as file:
        data = file.read()

    print("Torrent Size:")

    print(len(data))

    print("\nFirst 500 Bytes:\n")

    print(data[:500])


if __name__ == "__main__":
    main()