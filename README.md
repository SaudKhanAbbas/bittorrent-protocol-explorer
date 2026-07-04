BitTorrent Protocol Explorer

An educational implementation of the BitTorrent protocol built from scratch in Python to understand how BitTorrent works under the hood. This project focuses on implementing the protocol's core components for learning purposes rather than building a production-ready client.

---

# Features

Currently implemented:

* Parse `.torrent` files
* Decode bencoded data
* Extract torrent metadata
* Generate the correct SHA-1 info hash
* Build tracker announce requests
* Contact a BitTorrent tracker
* Decode tracker responses
* Build BitTorrent handshake packets
* Parse and validate incoming handshakes
* Simulate peer-to-peer communication locally using TCP sockets

---

# Project Structure

```
bittorrent-protocol-explorer/
│
├── torrents/
│   └── ubuntu.torrent
│
├── src/
│   ├── main.py
│   │
│   ├── torrent/
│   │   ├── bencode_decoder.py
│   │   ├── bencode_encoder.py
│   │   └── torrent.py
│   │
│   ├── tracker/
│   │   └── tracker.py
│   │
│   └── peer/
│       ├── handshake.py
│       ├── peer.py
│       ├── peer_client.py
│       └── peer_server.py
│
└── README.md
```

---

# What I Learned

This project helped me understand topics that I had only read about before.

Some of the main things I learned were:

* TCP socket programming
* Client-server communication
* Binary data handling
* The BitTorrent protocol
* Bencoding
* SHA-1 hashing
* Network protocols
* Organizing a larger Python project

One of the most interesting bugs I encountered was generating an incorrect info hash because I was hashing reconstructed data instead of the original raw bytes from the torrent file. Fixing that gave me a much better understanding of how protocol implementations need to be exact.

---

# Running the Project

Clone the repository:

```bash
git clone https://github.com/SaudKhanAbbas/bittorrent-protocol-explorer
```

Go into the project:

```bash
cd bittorrent-protocol-explorer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m src.main
```

---

# Example Output

```
==================================================
        MINI BITTORRENT CLIENT v1.0
==================================================

Loading torrent...

✓ Torrent loaded

Torrent Information

File Name:
ubuntu-24.04.3-desktop-amd64.iso

Tracker:
https://torrent.ubuntu.com/announce

File Size:
6345887744

Pieces:
24208

Info Hash:
...

Contacting tracker...

Tracker Response:
...
```

---

# Current Limitations

This project focuses on understanding the protocol rather than implementing every BitTorrent feature.

It does not currently support:

* Downloading pieces from real peers
* File assembly
* Multi-peer downloading
* Resume downloads
* Seeding
* Magnet links
* DHT

---

# Future Improvements

Some features I'd like to add later:

* Peer discovery from tracker responses
* Bitfield messages
* Interested / Unchoke messages
* Piece requests
* Piece downloading
* SHA-1 verification of downloaded pieces
* Writing the final file to disk
* Multi-peer downloading
* Resume interrupted downloads

---

Why I Built This

I built this project to better understand how BitTorrent works internally. Along the way, I learned how to read protocol specifications, debug binary data, and organize a networking project into reusable modules.
