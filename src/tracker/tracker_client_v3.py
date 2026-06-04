import hashlib
import urllib.parse
import urllib.request

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

            self.skip()
            self.skip()

        self.index += 1


def get_correct_info_hash(torrent_bytes):

    marker = b"4:info"

    marker_pos = torrent_bytes.find(marker)

    info_start = marker_pos + len(marker)

    tracker = BencodePositionTracker(torrent_bytes)

    tracker.index = info_start

    tracker.skip()

    info_end = tracker.index

    info_bytes = torrent_bytes[info_start:info_end]

    return hashlib.sha1(info_bytes).digest()


def main():

    with open(TORRENT_FILE, "rb") as file:
        torrent_bytes = file.read()

    info_hash = get_correct_info_hash(torrent_bytes)

    peer_id = b"-PC0001-123456789012"

    tracker_url = (
        "https://torrent.ubuntu.com/announce"
        f"?info_hash={urllib.parse.quote_from_bytes(info_hash)}"
        f"&peer_id={peer_id.decode()}"
        "&port=6881"
        "&uploaded=0"
        "&downloaded=0"
        "&left=6345887744"
        "&compact=1"
    )

    print("Connecting to tracker...")

    response = urllib.request.urlopen(tracker_url)

    tracker_response = response.read()

    print("\nResponse Length:")

    print(len(tracker_response))

    print("\nRaw Response:\n")

    print(tracker_response)


if __name__ == "__main__":
    main()