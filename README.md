# BitTorrent Protocol Explorer

An educational implementation of the BitTorrent protocol built from scratch in Python.

The goal of this project was to understand how BitTorrent works under the hood instead of simply using an existing library. While building it, I learned how torrent files are structured, how peers communicate, how binary protocols work, and how data is exchanged over TCP sockets.

This project focuses on understanding and implementing the core parts of the BitTorrent protocol. It is intended as a learning project rather than a production-ready BitTorrent client.

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
git clone <repository-url>
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

These would be natural next steps when the project is expanded in the future.

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

# Why I Built This

I wanted a project that would teach me more than just writing application code.

Building this helped me understand what actually happens behind the scenes when a torrent starts downloading and how peers communicate over a network.

More importantly, it gave me experience reading protocol specifications, debugging binary data, and organizing a project into reusable modules.