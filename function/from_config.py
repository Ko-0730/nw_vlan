class to_list():
    def __init__(self, config_string):
        self.config_lines = config_string.split('\n')

    def convert(self):
        return_list = []
        for line in self.config_lines:
            line = line.strip()
            if not line:  # 空行をスキップ
                continue

            current_vlans = set() # 重複を避けるためにセットを使用
            vlans_str = line.split(',')
            for vlan_part in vlans_str:
                vlan_part = vlan_part.strip()
                if not vlan_part: # 空文字列をスキップ
                    continue

                if '-' in vlan_part:
                    spl_vl = vlan_part.split('-')
                    if len(spl_vl) != 2:
                        raise ValueError(f"不正なVLAN範囲形式です: {vlan_part}")
                    try:
                        low_num, high_num = int(spl_vl[0]), int(spl_vl[1])
                    except ValueError:
                        raise ValueError(f"VLAN範囲の数値が不正です: {vlan_part}")

                    if low_num > high_num:
                        raise ValueError(f"VLAN範囲の開始が終了より大きいです: {vlan_part}")

                    for num in range(low_num, high_num + 1):
                        current_vlans.add(num)
                else:
                    try:
                        current_vlans.add(int(vlan_part))
                    except ValueError:
                        raise ValueError(f"不正なVLAN番号形式です: {vlan_part}")
            
            if current_vlans: # 空でない場合にのみ追加
                return_list.append(sorted(list(current_vlans)))
        return return_list
