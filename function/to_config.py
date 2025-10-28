class to_config():
    def __init__(self, vlan_data):
        self.vlan_data = vlan_data

    def _convert_vlan_list_to_range_string(self, v_lst):
        """
        VLAN番号のリストを範囲形式の文字列に変換するヘルパーメソッド。
        例: [1, 2, 3, 5, 6, 8] -> "1-3,5-6,8"
        """
        if not v_lst:
            return ''

        # リストをソートし、重複を削除
        sorted_vlans = sorted(list(set(v_lst)))
        
        result_parts = []
        current_range_start = sorted_vlans[0]
        current_range_end = sorted_vlans[0]

        for i in range(1, len(sorted_vlans)):
            if sorted_vlans[i] == current_range_end + 1:
                current_range_end = sorted_vlans[i]
            else:
                if current_range_start == current_range_end:
                    result_parts.append(str(current_range_start))
                else:
                    result_parts.append(f"{current_range_start}-{current_range_end}")
                current_range_start = sorted_vlans[i]
                current_range_end = sorted_vlans[i]

        # 最後の範囲を追加
        if current_range_start == current_range_end:
            result_parts.append(str(current_range_start))
        else:
            result_parts.append(f"{current_range_start}-{current_range_end}")

        return ','.join(result_parts)

    def convert(self):
        return_list = []
        if not self.vlan_data:
            return []

        # vlan_dataがVLAN番号のリストのリストであるかチェック
        if isinstance(self.vlan_data, list) and all(isinstance(item, list) for item in self.vlan_data):
            # VLANリストのリストの場合
            for v_lst in self.vlan_data:
                return_list.append(self._convert_vlan_list_to_range_string(v_lst))
        elif isinstance(self.vlan_data, list) and all(isinstance(item, int) for item in self.vlan_data):
            # 単一のVLAN番号のリストの場合
            return_list.append(self._convert_vlan_list_to_range_string(self.vlan_data))
        else:
            # 不正な形式の場合
            raise TypeError(f"VLANデータ構造が不正です: {self.vlan_data} (VLAN番号のリストまたはVLAN番号のリストのリストを期待)")
        
        return return_list
