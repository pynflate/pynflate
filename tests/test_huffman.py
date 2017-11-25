from pytest import fixture
from pynflate.huffman import Codec, huffman


@fixture
def codec():
    c = Codec()

    c.update('a', '0')
    c.update('b', '10')
    c.update('c', '11')

    return c


class TestCodec:
    def test_interface(self):
        codec = Codec()
        codec.update('a', '010')
        assert codec.encode('a') == '010'
        assert codec.decode('010') == 'a'

    def test_many_letters(self, codec):
        assert codec.encode('b') == '10'
        assert codec.decode('0') == 'a'

    def test_two_letter_encoding(self, codec):
        assert codec.encode('ab') == '010'

    def test_two_letter_decoding(self, codec):
        assert codec.decode('010') == 'ab'

    def test_complex_coding(self, codec):
        assert codec.encode('cca') == '11110'
        assert codec.decode('1110010') == 'cbab'


class TestHuffman:
    def test_interface(self):
        codes = huffman({'a': 1, 'b': 2})
        assert codes == {'a': '0', 'b': '1'}

    def test_two_letters(self):
        codes = huffman({'c': 3, 'd': 4})
        assert codes == {'c': '0', 'd': '1'}

    def test_three_letters(self):
        codes = huffman({'a': 1, 'b': 2, 'c': 5})
        assert codes == {'a': '00', 'b': '01', 'c': '1'}

    def test_equal_frequencies(self):
        codes = huffman({'a': 1, 'b': 1})
        assert codes == {'a': '0', 'b': '1'}
