from pynflate.lz77 import Lz77


class TestLz77(object):
    def test_empty(self):
        lz77 = Lz77(6)
        codewords = list(lz77.compress(''))
        assert codewords == []

    def test_one_char(self):
        lz77 = Lz77(6)
        codewords = list(lz77.compress('x'))
        assert codewords == [(0, 0, 'x')]

    def test_all_same(self):
        lz77 = Lz77(6)
        codewords = list(lz77.compress('xxxxxxxxxx'))
        assert codewords == [(0, 0, 'x'), (1, 8, 'x')]

    def test_nothing_special(self):
        lz77 = Lz77(6)
        codewords = list(lz77.compress('aacaacabcabaaac'))
        assert codewords == [(0, 0, 'a'), (1, 1, 'c'), (3, 4, 'b'), (3, 3, 'a'), (1, 2, 'c')]
