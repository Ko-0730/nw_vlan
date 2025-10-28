import unittest
import sys
import os

# functionディレクトリをPythonのパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../function')))

from from_config import to_list

class TestToListConvert(unittest.TestCase):

    def test_empty_input(self):
        tl = to_list('')
        self.assertEqual(tl.convert(), [])

    def test_single_vlan(self):
        tl = to_list('10')
        self.assertEqual(tl.convert(), [[10]])

    def test_multiple_single_vlans_on_one_line(self):
        tl = to_list('10,20,30')
        self.assertEqual(tl.convert(), [[10, 20, 30]])

    def test_vlan_range(self):
        tl = to_list('1-3')
        self.assertEqual(tl.convert(), [[1, 2, 3]])

    def test_multiple_vlan_ranges_on_one_line(self):
        tl = to_list('1-3,5-7')
        self.assertEqual(tl.convert(), [[1, 2, 3, 5, 6, 7]])

    def test_mixed_vlans_and_ranges_on_one_line(self):
        tl = to_list('1,3-5,7')
        self.assertEqual(tl.convert(), [[1, 3, 4, 5, 7]])

    def test_multiple_lines(self):
        input_str = "10,20\n30-32\n40"
        tl = to_list(input_str)
        self.assertEqual(tl.convert(), [[10, 20], [30, 31, 32], [40]])

    def test_input_with_empty_lines(self):
        input_str = "10\n\n20-21\n"
        tl = to_list(input_str)
        self.assertEqual(tl.convert(), [[10], [20, 21]])

    def test_input_with_spaces_around_commas(self):
        tl = to_list('10 , 20-21 , 30')
        self.assertEqual(tl.convert(), [[10, 20, 21, 30]])

    def test_invalid_vlan_format_non_integer(self):
        tl = to_list('10,abc')
        with self.assertRaisesRegex(ValueError, "不正なVLAN番号形式です: abc"):
            tl.convert()

    def test_invalid_vlan_range_format(self):
        tl = to_list('1-a')
        with self.assertRaisesRegex(ValueError, "VLAN範囲の数値が不正です: 1-a"):
            tl.convert()

    def test_invalid_vlan_range_order(self):
        tl = to_list('5-3')
        with self.assertRaisesRegex(ValueError, "VLAN範囲の開始が終了より大きいです: 5-3"):
            tl.convert()

    def test_vlan_with_leading_trailing_spaces(self):
        tl = to_list(' 10 , 20 ')
        self.assertEqual(tl.convert(), [[10, 20]])

    def test_vlan_with_duplicates(self):
        tl = to_list('10,10,20-21,21')
        self.assertEqual(tl.convert(), [[10, 20, 21]])

    def test_vlan_with_zero(self):
        tl = to_list('0,1,2')
        self.assertEqual(tl.convert(), [[0, 1, 2]])

    def test_vlan_with_large_numbers(self):
        tl = to_list('4000-4002,4005')
        self.assertEqual(tl.convert(), [[4000, 4001, 4002, 4005]])

if __name__ == '__main__':
    unittest.main()
