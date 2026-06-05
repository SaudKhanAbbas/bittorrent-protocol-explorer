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

            self.skip()
            self.skip()

        self.index += 1


def get_info_hash(torrent_bytes):

    marker = b"4:info"

    marker_pos = torrent_bytes.find(marker)

    if marker_pos == -1:
        raise ValueError("Info dictionary not found")

    info_start = marker_pos + len(marker)

    tracker = BencodePositionTracker(torrent_bytes)

    tracker.index = info_start

    tracker.skip()

    info_end = tracker.index

    info_bytes = torrent_bytes[info_start:info_end]

    return hashlib.sha1(info_bytes).digest()


def build_handshake(info_hash, peer_id):

    protocol = b"BitTorrent protocol"

    protocol_length = len(protocol)

    reserved = b"\x00" * 8

    handshake = (
        bytes([protocol_length])
        + protocol
        + reserved
        + info_hash
        + peer_id
    )

    return handshake