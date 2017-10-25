import unittest

from arrays import reorderArrayWithEvenFirst
from count_bits import count_bits
from parity import process_parity


class TestTypesBootcamp(unittest.TestCase):
    # Chaque méthode dont le nom commence par 'test_'
    # est un test.
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
        reorderedArray = [1,2,3]
        reorderArrayWithEvenFirst(reorderedArray)
        self.assertSequenceEqual(reorderedArray, [2,1,3])


if __name__ == '__main__':
    unittest.main()
