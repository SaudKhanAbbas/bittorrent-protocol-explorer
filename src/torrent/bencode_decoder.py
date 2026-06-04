class BencodeDecoder:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def decode_integer(self):
        self.index += 1

        end_index = self.data.index("e", self.index)

        number = int(self.data[self.index:end_index])

        self.index = end_index + 1

        return number


decoder = BencodeDecoder("i42e")

result = decoder.decode_integer()

print(result)