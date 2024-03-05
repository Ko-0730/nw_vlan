import json, yaml

def to_yaml(datas, frmt):
    return_list = []
    for data in datas:
        if frmt == 'back_to_flow_yaml':
            return_list.append(yaml.dump(data, allow_unicode=True, default_flow_style=True))
        else:
            return_list.append(yaml.dump(data, allow_unicode=True))
    return return_list

def to_json(datas):
    return_list = []
    for data in datas:
        return_list.append(json.dumps(data, ensure_ascii=False, indent=4))
    return return_list
