import json, yaml

def to_yaml(datas, frmt):
    return_list = []
    for data in datas:
        if frmt == 'back_to_flow_yaml':
            return_list.append(yaml.dump(data, allow_unicode=True, default_flow_style=True))
        else:
            return_list.append(yaml.dump(data, allow_unicode=True))
    return return_list
