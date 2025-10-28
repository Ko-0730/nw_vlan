import unittest
import sys
import os

# functionディレクトリをPythonのパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../function')))

from to_config import to_config

class TestToConfigRunConv(unittest.TestCase):

    def test_empty_list(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([]), '')

    def test_single_vlan(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([10]), '10')

    def test_consecutive_vlans(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 2, 3]), '1-3')
        self.assertEqual(tc._convert_vlan_list_to_range_string([10, 11, 12, 13]), '10-13')

    def test_non_consecutive_vlans(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 3, 5]), '1,3,5')
        self.assertEqual(tc._convert_vlan_list_to_range_string([10, 12, 14, 16]), '10,12,14,16')

    def test_mixed_vlans(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 2, 4, 5, 7]), '1-2,4-5,7')
        self.assertEqual(tc._convert_vlan_list_to_range_string([10, 11, 13, 15, 16, 17]), '10-11,13,15-17')

    def test_vlans_with_gaps_at_start_and_end(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 3, 4, 6]), '1,3-4,6')

    def test_large_numbers(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([100, 101, 103, 104, 105, 107]), '100-101,103-105,107')

    def test_already_sorted_unique_vlans(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 2, 3, 5, 6, 8, 9, 10]), '1-3,5-6,8-10')

    def test_single_vlan_at_end_of_range(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 2, 3, 5]), '1-3,5')

    def test_single_vlan_at_start_of_range(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 3, 4, 5]), '1,3-5')

    def test_two_consecutive_vlans(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 2]), '1-2')

    def test_two_non_consecutive_vlans(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 3]), '1,3')

    def test_unsorted_vlans(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([3, 1, 2]), '1-3')
        self.assertEqual(tc._convert_vlan_list_to_range_string([12, 10, 13, 11]), '10-13')

    def test_vlans_with_duplicates(self):
        tc = to_config(None)
        self.assertEqual(tc._convert_vlan_list_to_range_string([1, 2, 2, 3]), '1-3')
        self.assertEqual(tc._convert_vlan_list_to_range_string([10, 10, 11, 12, 12]), '10-12')


class TestToConfigConvert(unittest.TestCase):

    def test_list_of_lists(self):
        tc = to_config([[1, 2, 3], [5, 7], [10, 11, 12]])
        self.assertEqual(tc.convert(), ['1-3', '5,7', '10-12'])

    def test_single_list(self):
        tc = to_config([1, 2, 3, 5, 6])
        self.assertEqual(tc.convert(), ['1-3,5-6'])

    def test_empty_outer_list(self):
        tc = to_config([])
        self.assertEqual(tc.convert(), [])

    def test_list_with_empty_inner_list(self):
        tc = to_config([[]])
        self.assertEqual(tc.convert(), [''])

    def test_list_with_mixed_types_in_outer_list_raises_type_error(self):
        tc = to_config([1, [2, 3], 4])
        with self.assertRaisesRegex(TypeError, "VLANデータ構造が不正です: \[1, \[2, 3\], 4\] \(VLAN番号のリストまたはVLAN番号のリストのリストを期待\)"):
            tc.convert()

    def test_single_list_of_ints(self):
        tc = to_config([1])
        self.assertEqual(tc.convert(), ['1'])

if __name__ == '__main__':
    unittest.main()
