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


def _min_letter(frequencies):
    min_freq = min(frequencies.values())
    min_letters = [letter for letter in frequencies
                   if frequencies[letter] == min_freq]
    # Ensure stability
    return min(min_letters)


def huffman(frequencies):
    res = {letter: '' for letter in frequencies}

    while len(frequencies) > 1:
        min_letter = _min_letter(frequencies)
        total = frequencies[min_letter]
        del frequencies[min_letter]

        min_letter2 = _min_letter(frequencies)
        total += frequencies[min_letter2]
        del frequencies[min_letter2]

        for a in min_letter:
            res[a] = '0' + res[a]

        for b in min_letter2:
            res[b] = '1' + res[b]

        frequencies[min_letter + min_letter2] = total

    return res
