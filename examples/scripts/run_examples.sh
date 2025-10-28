#!/bin/bash

# スクリプトの実行ディレクトリをnw_vlanのルートに設定
SCRIPT_DIR=$(dirname "$0")
NW_VLAN_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)
PYTHON_CMD="python3 $NW_VLAN_ROOT/nw_vlan.py"
DATA_DIR="$NW_VLAN_ROOT/examples/data"

echo "nw_vlan.pyの機能確認スクリプトを開始します。"
echo "--------------------------------------------------"

# ヘルパー関数: テストケースを実行し、結果を表示
run_test() {
    local description="$1"
    local command="$2"
    echo "テストケース: $description"
    echo "コマンド: $command"
    echo "--- 実行結果 ---"
    eval "$command"
    echo "--------------------------------------------------"
}

# 1. listfile.txt を -f オプションで読み込み、Pythonリスト形式で出力
run_test "listfile.txt を -f オプションで読み込み、Pythonリスト形式で出力" \
    "$PYTHON_CMD -f $DATA_DIR/listfile.txt"

# 2. config_vlan.txt を -cf オプションで読み込み、Pythonリスト形式で出力
run_test "config_vlan.txt を -cf オプションで読み込み、Pythonリスト形式で出力" \
    "$PYTHON_CMD -cf $DATA_DIR/config_vlan.txt"

# 3. json_list を -jf オプションで読み込み、Pythonリスト形式で出力
run_test "json_list を -jf オプションで読み込み、Pythonリスト形式で出力" \
    "$PYTHON_CMD -jf $DATA_DIR/json_list"

# 4. yaml_list を -yf オプションで読み込み、Pythonリスト形式で出力
run_test "yaml_list を -yf オプションで読み込み、Pythonリスト形式で出力" \
    "$PYTHON_CMD -yf $DATA_DIR/yaml_list"

# 5. config_vlan.txt を -cf と -bj オプションで読み込み、JSON形式で出力
run_test "config_vlan.txt を -cf と -bj オプションで読み込み、JSON形式で出力" \
    "$PYTHON_CMD -cf $DATA_DIR/config_vlan.txt -bj"

# 6. config_vlan.txt を -cf と -by オプションで読み込み、YAML形式で出力
run_test "config_vlan.txt を -cf と -by オプションで読み込み、YAML形式で出力" \
    "$PYTHON_CMD -cf $DATA_DIR/config_vlan.txt -by"

# 7. config_vlan.txt を -cf と -bfy オプションで読み込み、フロー形式のYAMLで出力
run_test "config_vlan.txt を -cf と -bfy オプションで読み込み、フロー形式のYAMLで出力" \
    "$PYTHON_CMD -cf $DATA_DIR/config_vlan.txt -bfy"

# 8. 直接 -c オプションでVLAN文字列を渡し、Pythonリスト形式で出力
run_test "直接 -c オプションでVLAN文字列を渡し、Pythonリスト形式で出力" \
    "$PYTHON_CMD -c '10,20-22,30'"

# 9. 直接 -c オプションでVLAN文字列を渡し、-bj オプションでJSON形式で出力
run_test "直接 -c オプションでVLAN文字列を渡し、-bj オプションでJSON形式で出力" \
    "$PYTHON_CMD -c '10,20-22,30' -bj"

echo "--------------------------------------------------"
echo "nw_vlan.pyの機能確認スクリプトが完了しました。"
