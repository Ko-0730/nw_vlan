import json, yaml

def _check_duplicate_options(options):
    """
    指定されたオプションの辞書から、Trueになっているオプションが複数ある場合に
    重複しているオプション名のリストを返すヘルパー関数。
    """
    active_options = [name for name, value in options.items() if value]
    if len(active_options) > 1:
        return active_options
    return []

def duplicate_confirmation(arg):
    rc, message, data = 0, 'OK', {}

    # config と config_file の重複チェック
    if arg.config and arg.config_file:
        rc, message = 1, 'オプションが重複しています: config, config_file'
        return rc, message, data
    elif arg.config or arg.config_file:
        data['flag'] = 1
        if arg.config_file:
            try:
                with open(arg.config_file) as f:
                    conf_str = f.read()
            except FileNotFoundError:
                rc, message = 1, 'ファイルが見つかりません。'
                return rc, message, data
            except Exception:
                rc, message = 1, 'ファイルの処理中に予期せぬエラーが発生しました。'
                return rc, message, data
        else:
            conf_str = arg.config

        # back_to_json, back_to_yaml, back_to_flow_yaml の重複チェック
        back_to_options = {
            'back_to_json': arg.back_to_json,
            'back_to_yaml': arg.back_to_yaml,
            'back_to_flow_yaml': arg.back_to_flow_yaml
        }
        duplicated_back_to_options = _check_duplicate_options(back_to_options)
        if duplicated_back_to_options:
            rc, message = 1, f'オプションが重複しています: {", ".join(duplicated_back_to_options)}'
            return rc, message, data
        elif arg.back_to_json:
            data['config'], data['action'] = conf_str, 'back_to_json'
        elif arg.back_to_yaml:
            data['config'], data['action'] = conf_str, 'back_to_yaml'
        elif arg.back_to_flow_yaml:
            data['config'], data['action'] = conf_str, 'back_to_flow_yaml'
        else:
            data['config'], data['action'] = conf_str, 'back_to_list'
    else:
        data['flag'] = 2
        # file, json_file, yaml_file の重複チェック
        file_options = {
            'file': arg.file,
            'json_file': arg.json_file,
            'yaml_file': arg.yaml_file
        }
        duplicated_file_options = _check_duplicate_options(file_options)
        if duplicated_file_options:
            rc, message = 1, f'オプションが重複しています: {", ".join(duplicated_file_options)}'
            return rc, message, data
        elif not any(file_options.values()): # どのファイルオプションも指定されていない場合
            rc, message = 1, 'オプションが指定されていません。'
            return rc, message, data
        elif arg.json_file:
            try:
                with open(arg.json_file) as f:
                    conf_str = json.load(f)
            except json.JSONDecodeError:
                rc, message = 1, 'ファイル形式が不正です。'
                return rc, message, data
            except FileNotFoundError:
                rc, message = 1, 'ファイルが見つかりません。'
                return rc, message, data
            except Exception:
                rc, message = 1, 'ファイルの処理中に予期せぬエラーが発生しました。'
                return rc, message, data
            data['config'], data['action'] = conf_str, 'list_to_config'
        elif arg.yaml_file:
            try:
                with open(arg.yaml_file) as f:
                    conf_str = yaml.safe_load(f)
            except yaml.YAMLError:
                rc, message = 1, 'データ構造が不正です。'
                return rc, message, data
            except FileNotFoundError:
                rc, message = 1, 'ファイルが見つかりません。'
                return rc, message, data
            except Exception:
                rc, message = 1, 'ファイルの処理中に予期せぬエラーが発生しました。'
                return rc, message, data
            data['config'], data['action'] = conf_str, 'list_to_config'
        else: # arg.file の場合
            try:
                with open(arg.file) as f:
                    tmplist = f.readlines()
                    conf_str = []
                    for tmp_str in tmplist:
                        conv_str = tmp_str.replace('[', '').replace(']', '')
                        conf_str.append([int(a) for a in conv_str.split(',')])
            except ValueError:
                rc, message = 1, 'データ構造が不正です。'
                return rc, message, data
            except FileNotFoundError:
                rc, message = 1, 'ファイルが見つかりません。'
                return rc, message, data
            except Exception:
                rc, message = 1, 'ファイルの処理中に予期せぬエラーが発生しました。'
                return rc, message, data
            else:
                data['config'], data['action'] = conf_str, 'list_to_config'
    return rc, message, data
