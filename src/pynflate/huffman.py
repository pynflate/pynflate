class Codec:
    def __init__(self):
        self.letters = {}
        self.codes = {}

    def update(self, letter, code):
        self.letters[code] = letter
        self.codes[letter] = code

    def encode(self, s):
        return ''.join(self.codes[letter] for letter in s)

    def decode(self, code):
        return self.letters[code]
