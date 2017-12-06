from collections import Sequence


class Lz77(object):
    def __init__(self, sliding_window_length):
        self._sliding_window_length = sliding_window_length

    def compress(self, data):
        lz77buffer = Lz77Buffer(self._sliding_window_length, data)
        position = 0
        while position < len(data):
            codeword = lz77buffer.codeword_for_position(position)
            position += len(codeword)
            yield codeword


class Lz77Buffer(object):
    def __init__(self, sliding_window_length, data):
        self._sliding_window_length = sliding_window_length
        self._buffer = data
        self._buffer_len = len(data)

    def codeword_for_position(self, position):
        longest_match_len = 0
        longest_match_offset = 0
        pattern_start_offset = 1
        pattern_start_pos = position - pattern_start_offset

        while pattern_start_offset < self._sliding_window_length and pattern_start_pos >= 0:
            match_len = self._match(pattern_start_pos, position)
            if match_len > longest_match_len:
                longest_match_len = match_len
                longest_match_offset = pattern_start_offset
            pattern_start_offset += 1
            pattern_start_pos -= 1

        return Codeword(longest_match_offset, longest_match_len,
                        self._buffer[position + longest_match_len])

    def _match(self, pattern_pos, matchee_pos):
        match_len = 0

        # The longest match can be until the last character in the buffer, not including it
        while matchee_pos + match_len + 1 < self._buffer_len:
            if self._buffer[pattern_pos + match_len] != self._buffer[matchee_pos + match_len]:
                break
            match_len += 1

        return match_len


class Codeword(object):
    def __init__(self, prefix_start_offset, prefix_len, character):
        self.prefix_start_offset = prefix_start_offset
        self.prefix_len = prefix_len
        self.character = character

    def __len__(self):
        # Plus one for the character that is always present
        return self.prefix_len + 1

    def __eq__(self, other):
        if isinstance(other, Sequence):
            return (
                self.prefix_start_offset == other[0] and
                self.prefix_len == other[1] and
                self.character == other[2]
            )

        else:
            return (
                self.prefix_start_offset == other.prefix_start_offset and
                self.prefix_len == other.prefix_len and
                self.character == other.character
            )

    def __repr__(self):
        return str((self.prefix_start_offset, self.prefix_len, self.character))
