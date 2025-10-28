#!/usr/bin/env python3
import traceback
from function.option import get_option
from function.dup_check import duplicate_confirmation
from function.from_config import to_list
from function.to_config import to_config
from function.format_change import to_yaml, to_json


def main():
    args = get_option()
    rc, message, data = duplicate_confirmation(args)
    if not rc == 0:
        print('エラーが発生しました。')
        print('エラー内容: %s' % message)
        if args.debug:
            traceback.print_exc()
        exit(1) # エラー時は非ゼロの終了コードを返す
    try:
        if data['flag'] == 1:
            change = to_list(data['config'])
        elif data['flag'] == 2:
            change = to_config(data['config'])
        convert_data = change.convert()
        if data['action'] == 'back_to_yaml' or data['action'] == 'back_to_flow_yaml':
            result = to_yaml(convert_data, data['action'])
        elif data['action'] == 'back_to_json':
            result = to_json(convert_data)
        else:
            result = convert_data
        for i in result:
            print(i)
    except Exception as e:
        print('処理中に予期せぬエラーが発生しました。')
        print('エラー内容: %s' % str(e))
        if args.debug:
            traceback.print_exc()
        exit(1)

if __name__ == '__main__':
    main()
