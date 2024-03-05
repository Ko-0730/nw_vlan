#!/usr/bin/env python3
from function.option import get_option
from function.dup_check import duplicate_confirmation
from function.from_config import to_list
from function.to_config import to_config
from function.format_change import to_yaml, to_json


if __name__ == '__main__':
    args = get_option()
    rc, message, data = duplicate_confirmation(args)
    if not rc == 0:
        print('error\nerror contents: %s' % message)
        exit()
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
