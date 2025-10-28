import unittest
from unittest.mock import Mock, patch
import sys
import os

# functionディレクトリをPythonのパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../function')))

from dup_check import duplicate_confirmation

class TestDuplicateConfirmation(unittest.TestCase):

    def test_config_and_config_file_duplicated(self):
        # arg.config と arg.config_file が両方指定された場合の重複エラー
        mock_arg = Mock(config="some_config", config_file="some_file.txt")
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = False
        mock_arg.yaml_file = False
        rc, message, data = duplicate_confirmation(mock_arg)
        self.assertEqual(rc, 1)
        self.assertEqual(message, 'オプションが重複しています: config, config_file')

    def test_back_to_options_duplicated(self):
        # arg.back_to_json, arg.back_to_yaml, arg.back_to_flow_yaml のうち2つ以上が True の場合の重複エラー
        mock_arg = Mock(config="some_config", config_file=False)
        mock_arg.back_to_json = True
        mock_arg.back_to_yaml = True
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = False
        mock_arg.yaml_file = False
        rc, message, data = duplicate_confirmation(mock_arg)
        self.assertEqual(rc, 1)
        self.assertEqual(message, 'オプションが重複しています: back_to_json, back_to_yaml')

    def test_file_options_duplicated(self):
        # arg.file, arg.json_file, arg.yaml_file のうち2つ以上が True の場合の重複エラー
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = "some_file.txt"
        mock_arg.json_file = "some_json.json"
        mock_arg.yaml_file = False
        rc, message, data = duplicate_confirmation(mock_arg)
        self.assertEqual(rc, 1)
        self.assertEqual(message, 'オプションが重複しています: file, json_file')

    def test_no_file_options_specified(self):
        # arg.file, arg.json_file, arg.yaml_file のいずれも指定されていない場合の「No options specified」エラー
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = False
        mock_arg.yaml_file = False
        rc, message, data = duplicate_confirmation(mock_arg)
        self.assertEqual(rc, 1)
        self.assertEqual(message, 'オプションが指定されていません。')

    @patch('builtins.open', unittest.mock.mock_open(read_data='[1,2,3]\n[4,5,6]\n'))
    def test_valid_file_option(self):
        # 正常なケース（ファイルオプションが1つだけ指定された場合）
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = "valid_file.txt"
        mock_arg.json_file = False
        mock_arg.yaml_file = False
        rc, message, data = duplicate_confirmation(mock_arg)
        self.assertEqual(rc, 0)
        self.assertEqual(message, 'OK')
        self.assertEqual(data['action'], 'list_to_config')
        self.assertEqual(data['config'], [[1,2,3], [4,5,6]])

    @patch('builtins.open', unittest.mock.mock_open(read_data='{"key": "value"}'))
    @patch('json.load', return_value={"key": "value"})
    def test_valid_json_file_option(self, mock_json_load):
        # 正常なケース（JSONファイルオプションが1つだけ指定された場合）
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = "valid.json"
        mock_arg.yaml_file = False
        rc, message, data = duplicate_confirmation(mock_arg)
        self.assertEqual(rc, 0)
        self.assertEqual(message, 'OK')
        self.assertEqual(data['action'], 'list_to_config')
        self.assertEqual(data['config'], {"key": "value"})

    @patch('builtins.open', unittest.mock.mock_open(read_data='key: value'))
    @patch('yaml.safe_load', return_value={'key': 'value'})
    def test_valid_yaml_file_option(self, mock_yaml_safe_load):
        # 正常なケース（YAMLファイルオプションが1つだけ指定された場合）
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = False
        mock_arg.yaml_file = "valid.yaml"
        rc, message, data = duplicate_confirmation(mock_arg)
        self.assertEqual(rc, 0)
        self.assertEqual(message, 'OK')
        self.assertEqual(data['action'], 'list_to_config')
        self.assertEqual(data['config'], {'key': 'value'})

    @patch('builtins.open', unittest.mock.mock_open(read_data='some config string'))
    def test_valid_config_option_back_to_list(self):
        # 正常なケース（configオプションとback_to_list）
        mock_arg = Mock(config="some config string", config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = False
        mock_arg.yaml_file = False
        rc, message, data = duplicate_confirmation(mock_arg)
        self.assertEqual(rc, 0)
        self.assertEqual(message, 'OK')
        self.assertEqual(data['action'], 'back_to_list')
        self.assertEqual(data['config'], "some config string")

    @patch('builtins.open', unittest.mock.mock_open(read_data='some config string'))
    def test_valid_config_file_option_back_to_json(self):
        # 正常なケース（config_fileオプションとback_to_json）
        mock_arg = Mock(config=False, config_file="config.txt")
        mock_arg.back_to_json = True
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = False
        mock_arg.yaml_file = False
        rc, message, data = duplicate_confirmation(mock_arg)
        self.assertEqual(rc, 0)
        self.assertEqual(message, 'OK')
        self.assertEqual(data['action'], 'back_to_json')
        self.assertEqual(data['config'], "some config string")

    def test_file_not_found_config_file(self):
        # config_fileが見つからない場合
        mock_arg = Mock(config=False, config_file="non_existent_file.txt")
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = False
        mock_arg.yaml_file = False
        with patch('builtins.open', side_effect=FileNotFoundError):
            rc, message, data = duplicate_confirmation(mock_arg)
            self.assertEqual(rc, 1)
            self.assertEqual(message, 'ファイルが見つかりません。')

    def test_file_not_found_json_file(self):
        # json_fileが見つからない場合
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = "non_existent.json"
        mock_arg.yaml_file = False
        with patch('builtins.open', side_effect=FileNotFoundError):
            rc, message, data = duplicate_confirmation(mock_arg)
            self.assertEqual(rc, 1)
            self.assertEqual(message, 'ファイルが見つかりません。')

    def test_incorrect_json_file_format(self):
        # json_fileの形式が不正な場合
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = "invalid.json"
        mock_arg.yaml_file = False
        with patch('builtins.open', unittest.mock.mock_open(read_data='{invalid json')) as mock_file:
            rc, message, data = duplicate_confirmation(mock_arg)
            self.assertEqual(rc, 1)
            self.assertEqual(message, 'ファイル形式が不正です。')

    def test_file_not_found_yaml_file(self):
        # yaml_fileが見つからない場合
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = False
        mock_arg.yaml_file = "non_existent.yaml"
        with patch('builtins.open', side_effect=FileNotFoundError):
            rc, message, data = duplicate_confirmation(mock_arg)
            self.assertEqual(rc, 1)
            self.assertEqual(message, 'ファイルが見つかりません。')

    def test_incorrect_yaml_file_format(self):
        # yaml_fileのデータ構造が不正な場合
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = False
        mock_arg.json_file = False
        mock_arg.yaml_file = "invalid.yaml"
        with patch('builtins.open', unittest.mock.mock_open(read_data='- invalid: [yaml')) as mock_file:
            rc, message, data = duplicate_confirmation(mock_arg)
            self.assertEqual(rc, 1)
            self.assertEqual(message, 'データ構造が不正です。')

    def test_file_not_found_list_file(self):
        # list_fileが見つからない場合
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = "non_existent_list.txt"
        mock_arg.json_file = False
        mock_arg.yaml_file = False
        with patch('builtins.open', side_effect=FileNotFoundError):
            rc, message, data = duplicate_confirmation(mock_arg)
            self.assertEqual(rc, 1)
            self.assertEqual(message, 'ファイルが見つかりません。')

    def test_incorrect_list_file_format(self):
        # list_fileのデータ構造が不正な場合
        mock_arg = Mock(config=False, config_file=False)
        mock_arg.back_to_json = False
        mock_arg.back_to_yaml = False
        mock_arg.back_to_flow_yaml = False
        mock_arg.file = "invalid_list.txt"
        mock_arg.json_file = False
        mock_arg.yaml_file = False
        with patch('builtins.open', unittest.mock.mock_open(read_data='invalid,list,format\n')) as mock_file:
            rc, message, data = duplicate_confirmation(mock_arg)
            self.assertEqual(rc, 1)
            self.assertEqual(message, 'データ構造が不正です。')

if __name__ == '__main__':
    unittest.main()
