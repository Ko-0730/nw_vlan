class to_config():
    def __init__(self, list):
        self.list = list

    def run_conv(self, v_lst):
        a = b = 0
        ran_vl = ''
        for v_num in v_lst:
            if a == 0:
                a = v_num
            elif a + 1 == v_num:
                b = v_num
            elif b + 1 == v_num:
                b += 1
            elif a == b and b + 1 < v_num:
                ran_vl = '%s,%s' % (ran_vl, str(a))
                a = b = v_num
            elif b + 1 < v_num:
                if ran_vl == '':
                    if a > b and b == 0:
                        ran_vl = '%s' % (str(a))
                        a = b = v_num
                    else:
                        ran_vl = '%s-%s' % (str(a), str(b))
                        a = b = v_num
                else:
                    ran_vl = '%s,%s-%s' % (ran_vl, str(a), str(b))
                    a = b = v_num
            else:
                pass
        if a == b:
            ran_vl = '%s,%s' % (ran_vl, str(a))
        elif a + 1 <= b:
            if ran_vl == '':
                ran_vl = '%s-%s' % (str(a), str(b))
            else:
                ran_vl = '%s,%s-%s' % (ran_vl, str(a), str(b))
        return ran_vl

    def convert(self):
        return_list = []
        for v_lst in self.list:

            if type(v_lst) is list:
                return_list.append(self.run_conv(v_lst))
            else:
                return_list.append(self.run_conv(self.list))
                break
        return return_list
