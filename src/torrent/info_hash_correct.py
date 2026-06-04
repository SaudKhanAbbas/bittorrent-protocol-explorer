import hashlib

TORRENT_FILE = "torrents/ubuntu.torrent"


class BencodePositionTracker:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def skip(self):

        current = chr(self.data[self.index])

        if current == "i":
            self.skip_integer()

        elif current.isdigit():
            self.skip_string()

        elif current == "l":
            self.skip_list()

        elif current == "d":
            self.skip_dictionary()

        else:
            raise ValueError(f"Unsupported type: {current}")

    def skip_integer(self):

        self.index += 1

        while chr(self.data[self.index]) != "e":
            self.index += 1

        self.index += 1

    def skip_string(self):

        colon = self.data.index(b":", self.index)

        length = int(self.data[self.index:colon])

        self.index = colon + 1 + length

    def skip_list(self):

        self.index += 1

        while chr(self.data[self.index]) != "e":
            self.skip()

        self.index += 1

    def skip_dictionary(self):

        self.index += 1

        while chr(self.data[self.index]) != "e":

            self.skip()  # key

            self.skip()  # value

        self.index += 1


def main():

    with open(TORRENT_FILE, "rb") as file:
        torrent_bytes = file.read()

    marker = b"4:info"

    marker_pos = torrent_bytes.find(marker)

    if marker_pos == -1:
        raise ValueError("info dictionary not found")

    info_start = marker_pos + len(marker)

    tracker = BencodePositionTracker(torrent_bytes)

    tracker.index = info_start

    tracker.skip()

    info_end = tracker.index

    info_bytes = torrent_bytes[info_start:info_end]

    info_hash = hashlib.sha1(info_bytes).hexdigest()

    print("\n===== CORRECT INFO HASH =====\n")

    print(info_hash)

    print("\nInfo Dictionary Size:")

    print(len(info_bytes))


if __name__ == "__main__":
    main()