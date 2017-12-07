from pynflate.lz77 import Lz77


class TestLz77(object):
    def test_empty(self):
        lz77 = Lz77(6)
        codewords = list(lz77.compress(''))
        assert codewords == []

    def test_one_char(self):
        lz77 = Lz77(6)
        original = 'x'

        codewords = list(lz77.compress(original))
        assert codewords == [(0, 0, 'x')]

        decompressed = lz77.decompress(codewords)
        assert decompressed == original

    def test_all_same(self):
        lz77 = Lz77(6)
        original = 'xxxxxxxxxx'

        codewords = list(lz77.compress(original))
        assert codewords == [(0, 0, 'x'), (1, 8, 'x')]

        decompressed = lz77.decompress(codewords)
        assert decompressed == original

    def test_nothing_special(self):
        lz77 = Lz77(6)
        original = 'aacaacabcabaaac'

        codewords = list(lz77.compress(original))
        assert codewords == [(0, 0, 'a'), (1, 1, 'c'), (3, 4, 'b'), (3, 3, 'a'), (1, 2, 'c')]

        decompressed = lz77.decompress(codewords)
        assert decompressed == original
