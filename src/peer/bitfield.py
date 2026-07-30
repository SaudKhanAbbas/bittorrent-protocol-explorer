MESSAGE_ID = 5


def build_bitfield(bitfield_bytes):

    length = len(bitfield_bytes) + 1

    message = (
        length.to_bytes(4, "big")
        + bytes([MESSAGE_ID])
        + bitfield_bytes
    )

    return message


def parse_bitfield(message):

    length = int.from_bytes(
        message[:4],
        "big"
    )

    message_id = message[4]

    bitfield = message[5:]

    return {
        "length": length,
        "message_id": message_id,
        "bitfield": bitfield
    }


def main():

    sample_bitfield = bytes([0b11010011])

    message = build_bitfield(
        sample_bitfield
    )

    parsed = parse_bitfield(
        message
    )

    print("Length:")

    print(parsed["length"])

    print("\nMessage ID:")

    print(parsed["message_id"])

    print("\nBitfield:")

    print(bin(parsed["bitfield"][0]))


if __name__ == "__main__":
    main()
