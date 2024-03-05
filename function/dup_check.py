import json, yaml

def duplicate_confirmation(arg):
    rc, message, data = 0, 'OK', {}
    if arg.config and arg.config_file:
        rc, message = 1, 'Cannot execute because the options are duplicated.'
        return rc, message, data
    elif arg.config or arg.config_file:
        data['flag'] = 1
        if arg.config_file:
            try:
                with open(arg.config_file) as f:
                    conf_str = f.read()
            except:
                rc, message = 1, 'File not found.'
                return rc, message, data
        else:
            conf_str = arg.config
        if [arg.back_to_json, arg.back_to_yaml, arg.back_to_flow_yaml].count(False) < 2:
            rc, message = 1, 'Cannot execute because the options are duplicated.'
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
        if [arg.json, arg.yaml, arg.file, arg.json_file, arg.yaml_file].count(False) < 4:
            rc, message = 1, 'Cannot execute because the options are duplicated.'
            return rc, message, data
        elif [arg.json, arg.yaml, arg.file, arg.json_file, arg.yaml_file].count(False) == 5:
            rc, message = 1, 'No options specified.'
            return rc, message, data
        elif arg.json or arg.json_file:
            if arg.json_file:
                try:
                    with open(arg.json_file) as f:
                        try:
                            conf_str = json.load(f)
                        except:
                            rc, message = 1, 'Incorrect file format.'
                            return rc, message, data
                except:
                    rc, message = 1, 'File not found.'
                    return rc, message, data
            else:
                conf_str = arg.json
            data['config'], data['action'] = conf_str, 'list_to_config'
        elif arg.yaml or arg.yaml_file:
            if arg.yaml_file:
                try:
                    with open(arg.yaml_file) as f:
                        try:
                            conf_str = yaml.safe_load(f)
                        except:
                            rc, message = 1, 'The data structure is incorrect.'
                            return rc, message, data
                except:
                    rc, message = 1, 'File not found.'
                    return rc, message, data
            else:
                conf_str = arg.yaml
            data['config'], data['action'] = conf_str, 'list_to_config'
        else:
            try:
                with open(arg.file) as f:
                    try:
                        tmplist = f.readlines()
                    except:
                        rc, message = 1, 'The data structure is incorrect.'
                        return rc, message, data
                    else:
                        conf_str = []
                        for tmp_str in tmplist:
                            conv_str = tmp_str.replace('[', '').replace(']', '')
                            conf_str.append([int(a) for a in conv_str.split(',')])
            except:
                rc, message = 1, 'File not found.'
                return rc, message, data
            else:
                data['config'], data['action'] = conf_str, 'list_to_config'
    return rc, message, data
