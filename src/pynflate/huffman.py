from heapq import heappush, heappop


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


def huffman(frequencies):
    if len(frequencies) == 1:
        letter, = frequencies
        return {letter: '0'}

    queue = []
    res = {letter: '' for letter in frequencies}

    for letter, frequency in frequencies.items():
        heappush(queue, (frequency, letter))

    while len(queue) > 1:
        first_freq, first_letters = heappop(queue)
        second_freq, second_letters = heappop(queue)

        for letter in first_letters:
            res[letter] = '0' + res[letter]

        for letter in second_letters:
            res[letter] = '1' + res[letter]

        heappush(
            queue,
            (
                first_freq + second_freq,
                ''.join(sorted(first_letters + second_letters))
            )
        )

    return res
