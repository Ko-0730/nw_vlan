class to_config():
    def __init__(self, list):
        self.list = list.split('\n')

    def convert(self):
        return_list = []
        vl_list = []
        for line in self.list:
            if line != '':
                vlans = line.split(',')
                for vlan in vlans:
                    if '-' in vlan:
                        spl_vl = vlan.split('-')
                        low_num, high_num = int(spl_vl[0]), int(spl_vl[1])
                        vl_list.append(low_num)
                        while True:
                            if low_num == high_num:
                                break
                            else:
                                low_num += 1
                                vl_list.append(low_num)
                    elif '' in vlan:
                        pass
                    else:
                        vl_list.append(int(vlan))
                return_list.append(vl_list)
                vl_list = []
        return return_list
