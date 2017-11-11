class Codec:
    def __init__(self):
        self.letters = {}
        self.codes = {}

    def update(self, letter, code):
        self.letters[code] = letter
        self.codes[letter] = code

    def encode(self, letter):
        return self.codes[letter]

    def decode(self, code):
        return self.letters[code]
