import unittest

from arrays import reorderArrayWithEvenFirst, transform_string_to_list_using_for, \
    transform_string_to_list_using_listcomp, generate_cartesian_product_list_from_two_lists
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
        # reordered_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        reorderArrayWithEvenFirst(reordered_array)
        self.assertSequenceEqual(reordered_array, [2, 3, 1])

    def test_should_build_a_unicode_codepoints_when_parsing_a_string(self):
        symbols = '$ç£€'
        codesequence = transform_string_to_list_using_for(symbols)
        self.assertSequenceEqual([36, 231, 163, 8364], codesequence)

    def test_should_build_a_unicode_codepoints_when_parsing_a_string_using_a_listcomp(self):
        symbols = '$ç£€'
        codesequence = transform_string_to_list_using_listcomp(symbols)
        self.assertSequenceEqual([36, 231, 163, 8364], codesequence)

    def test_should_generate_cartesian_product_list_from_two_lists(self):
        color_list = ['black', 'white']
        size_list = ['S', 'M', 'L']
        generatedCartesianProductSequence = generate_cartesian_product_list_from_two_lists(color_list, size_list)
        self.assertSequenceEqual(
            [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')],
            generatedCartesianProductSequence)


if __name__ == '__main__':
    unittest.main()
