# XXX hack - until I understand how to use `pytest` properly
import sys
from os.path import abspath, join, dirname

sys.path.insert(0, abspath(join(dirname(__file__), '../src')))

import pynflate
# XXX end of hack

from pynflate.huffman import Codec


def test_passes():
    assert 1


def test_codec_interface():
    codec = Codec()
    codec.update('a', '010')
    assert codec.encode('a') == '010'
    assert codec.decode('010') == 'a'


def test_many_letters():
    codec = Codec()

    codec.update('a', '0')
    codec.update('b', '10')
    codec.update('c', '11')

    assert codec.encode('b') == '10'
    assert codec.decode('0') == 'a'


def test_two_letter_encoding():
    codec = Codec()

    codec.update('a', '0')
    codec.update('b', '10')

    assert codec.encode('ab') == '010'


def test_two_letter_decoding():
    codec = Codec()

    codec.update('a', '0')
    codec.update('b', '10')

    assert codec.decode('010') == 'ab'
