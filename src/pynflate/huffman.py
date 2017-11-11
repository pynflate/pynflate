class Codec:
    def __init__(self):
        self.letters = {}
        self.codes = {}

    def update(self, letter, code):
        self.letters[code] = letter
        self.codes[letter] = code

    def encode(self, s):
        return ''.join(self.codes[letter] for letter in s)

    def _decode(self, s):
        code = ''
        for c in s:
            code += c

            if code in self.letters:
                yield self.letters[code]
                code = ''

        assert code == ''

    def decode(self, s):
        return ''.join(self._decode(s))
