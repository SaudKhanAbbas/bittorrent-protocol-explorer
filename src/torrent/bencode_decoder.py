class BencodeDecoder:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def decode(self):
        current_char = self.data[self.index]

        if current_char == "i":
            return self.decode_integer()

        if current_char.isdigit():
            return self.decode_string()

        raise ValueError(f"Unsupported type: {current_char}")

    def decode_integer(self):
        self.index += 1

        end_index = self.data.index("e", self.index)

        number = int(self.data[self.index:end_index])

        self.index = end_index + 1

        return number

    def decode_string(self):
        colon_index = self.data.index(":", self.index)

        length = int(self.data[self.index:colon_index])

        self.index = colon_index + 1

        result = self.data[self.index:self.index + length]

        self.index += length

        return result


decoder1 = BencodeDecoder("i42e")
print(decoder1.decode())

decoder2 = BencodeDecoder("5:hello")
print(decoder2.decode())