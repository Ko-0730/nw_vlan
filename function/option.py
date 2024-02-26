from argparse import ArgumentParser

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-c', '--config', type=str,
                           default=False, help='Specify this when you want to return the NW device config to list format. If bj/by is not specified, it will be converted to Python list format.')
    argparser.add_argument('-j', '--json', type=str,
                           default=False, help='Specify when converting a json list.')
    argparser.add_argument('-y', '--yaml', type=str,
                           default=False, help='Specify when converting a yaml list.')
    argparser.add_argument('-f', '--file', type=str,
                           default=False, help='Specify the path if you want to load and execute a file containing Vlans separated by line breaks.')
    argparser.add_argument('-cf', '--config_file', type=str,
                           default=False, help='When you want to convert the NW device config back to list format, specify the file that contains the config you want to convert. If bj/by is not specified, it will be converted to Python list format.')
    argparser.add_argument('-jf', '--json_file', type=str,
                           default=False, help='Specify the path if you want to read and execute a file with Vlan written in json list format.')
    argparser.add_argument('-yf', '--yaml_file', type=str,
                           default=False, help='Specify the path if you want to read and execute a file with Vlan written in yaml list format.')
    argparser.add_argument('-bj', '--back_to_json',
                           action='store_true', help='Convert vlan in config format back to json.')
    argparser.add_argument('-by', '--back_to_yaml',
                           action='store_true', help='Convert vlan in config format back to yaml.')
    argparser.add_argument('-bfy', '--back_to_flow_yaml',
                           action='store_true', help='Convert vlan in config format back to flow style yaml.')
    return argparser.parse_args()
