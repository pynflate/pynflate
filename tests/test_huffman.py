from pytest import fixture
from pynflate.huffman import Codec


@fixture
def codec():
    c = Codec()

    c.update('a', '0')
    c.update('b', '10')
    c.update('c', '11')

    return c


class TestCodec(object):
    def test_codec_interface(self):
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
