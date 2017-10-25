import unittest

from arrays import reorderArrayWithEvenFirst
from count_bits import count_bits
from parity import process_parity


class TestTypesBootcamp(unittest.TestCase):
    def test_count_bits(self):
        bit_nb = count_bits(12)
        self.assertEqual(bit_nb, 2)


class TestParityCheck(unittest.TestCase):
    def test_should_return_0_when_input_is_0b0(self):
        parity = process_parity(0b0)
        self.assertEqual(parity, 0)

    def test_should_return_1_when_input_is_0b1011(self):
        parity = process_parity(0b1011)
        self.assertEqual(parity, 1)


class TestArrays(unittest.TestCase):
    def test_reorderArrayWithEvenFirst(self):
        reordered_array = [1, 2, 3]
        reorderArrayWithEvenFirst(reordered_array)
        self.assertSequenceEqual(reordered_array, [2, 3, 1])


if __name__ == '__main__':
    unittest.main()
