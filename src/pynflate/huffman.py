class Codec:
    def update(self, letter, code):
        self.letter = letter
        self.code = code

    def encode(self, letter):
        return self.code

    def decode(self, code):
        return self.letter
