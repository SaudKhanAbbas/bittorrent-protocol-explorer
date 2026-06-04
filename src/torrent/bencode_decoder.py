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

        if current_char == "l":
            return self.decode_list()

        if current_char == "d":
            return self.decode_dictionary()

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

    def decode_list(self):
        self.index += 1

        result = []

        while self.data[self.index] != "e":
            result.append(self.decode())

        self.index += 1

        return result

    def decode_dictionary(self):
        self.index += 1

        result = {}

        while self.data[self.index] != "e":
            key = self.decode()
            value = self.decode()

            result[key] = value

        self.index += 1

        return result


decoder = BencodeDecoder("d4:name5:Saude")

print(decoder.decode())