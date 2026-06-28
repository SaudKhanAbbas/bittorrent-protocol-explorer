import urllib.parse
import urllib.request

from src.torrent.torrent import Torrent


class Tracker:

    def __init__(self, torrent: Torrent):

        self.torrent = torrent

        self.peer_id = b"-PC0001-123456789012"

        self.port = 6881

        self.uploaded = 0

        self.downloaded = 0

        self.left = torrent.file_size

    def build_tracker_url(self):

        return (
            f"{self.torrent.announce_url}"
            f"?info_hash={urllib.parse.quote_from_bytes(self.torrent.info_hash)}"
            f"&peer_id={self.peer_id.decode()}"
            f"&port={self.port}"
            f"&uploaded={self.uploaded}"
            f"&downloaded={self.downloaded}"
            f"&left={self.left}"
            f"&compact=1"
        )

    def announce(self):

        tracker_url = self.build_tracker_url()

        response = urllib.request.urlopen(tracker_url)

        return response.read()


def main():

    torrent = Torrent("torrents/ubuntu.torrent")

    tracker = Tracker(torrent)

    print("Tracker URL:\n")

    print(tracker.build_tracker_url())

    print("\nContacting tracker...\n")

    response = tracker.announce()

    print("Tracker Response Length:")

    print(len(response))

    print("\nTracker Response:\n")

    print(response)


if __name__ == "__main__":
    main()