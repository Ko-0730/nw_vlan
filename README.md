# nw_vlan

NW機器のVLAN設定を効率的に管理するためのPythonスクリプトです。
このツールは、NW機器のコンフィグ形式のVLANリストを様々な形式（Pythonリスト、JSON、YAML）に変換したり、
逆にこれらのリスト形式からNW機器のコンフィグ形式のVLAN設定を生成したりする機能を提供します。
ネットワークエンジニアがVLAN設定の確認、変更、自動化を行う際に役立ちます。

## 動作確認環境
Python 3.12.2

## インストール

1.  リポジトリをクローンします。
    ```bash
    git clone https://github.com/Ko-0730/nw_vlan.git
    ```
2.  クローンしたディレクトリに移動します。
    ```bash
    cd nw_vlan
    ```
3.  必要なパッケージをインストールします。（初回のみ）
    ```bash
    python3 -m pip install -r requirements.txt
    ```
    `requirements.txt`には、`PyYAML`が含まれています。

## 使い方

`nw_vlan.py`スクリプトは、コマンドライン引数を使用して様々な操作を実行します。

### 1. NW機器のコンフィグ形式VLANをリストに変換する

NW機器のコンフィグ形式（例: "1-3,5,7-9"）のVLANを、Pythonリスト、JSON、またはYAML形式に変換します。

*   **コマンドラインから直接指定する場合**: `-c` オプションを使用します。
    *   Pythonリスト形式:
        ```bash
        python3 nw_vlan.py -c "1-3,5-7"
        ```
    *   JSONリスト形式:
        ```bash
        python3 nw_vlan.py -c "1-3,5-7" -bj
        ```
    *   YAMLリスト形式:
        ```bash
        python3 nw_vlan.py -c "1-3,5-7" -by
        ```
    *   FlowスタイルのYAMLリスト形式:
        ```bash
        python3 nw_vlan.py -c "1-3,5-7" -bfy
        ```

*   **ファイルから読み込む場合**: `-cf` オプションを使用します。
    *   Pythonリスト形式:
        ```bash
        python3 nw_vlan.py -cf {filename}
        ```
    *   JSONリスト形式:
        ```bash
        python3 nw_vlan.py -cf {filename} -bj
        ```
    *   YAMLリスト形式:
        ```bash
        python3 nw_vlan.py -cf {filename} -by
        ```
    *   FlowスタイルのYAMLリスト形式:
        ```bash
        python3 nw_vlan.py -cf {filename} -bfy
        ```

### 2. リスト形式のVLANをNW機器のコンフィグ形式に変換する

Pythonリスト、YAML、またはJSON形式のVLANリストを、NW機器のコンフィグ形式に変換します。

*   **Pythonリストファイルから読み込む場合**: `-f` オプションを使用します。
    ```bash
    python3 nw_vlan.py -f {filename}
    ```
*   **YAMLリストファイルから読み込む場合**: `-yf` オプションを使用します。
    ```bash
    python3 nw_vlan.py -yf {filename}
    ```
*   **JSONリストファイルから読み込む場合**: `-jf` オプションを使用します。
    ```bash
    python3 nw_vlan.py -jf {filename}
    ```

## オプション一覧

*   `-c "VLAN_STRING"`: NW機器のコンフィグ形式VLAN文字列を直接指定します。
*   `-cf {filename}`: NW機器のコンフィグ形式VLANが記載されたファイルを読み込みます。
*   `-f {filename}`: Pythonリスト形式のVLANが記載されたファイルを読み込みます。
*   `-yf {filename}`: YAMLリスト形式のVLANが記載されたファイルを読み込みます。
*   `-jf {filename}`: JSONリスト形式のVLANが記載されたファイルを読み込みます。
*   `-bj`: 出力形式をJSONリストにします。
*   `-by`: 出力形式をYAMLリストにします。
*   `-bfy`: 出力形式をFlowスタイルのYAMLリストにします。

## 実行例

### 例1: コンフィグファイルからYAMLリストへの変換

`testfile/config_vlan.txt` の内容:
```
1-3,5-9,11
2-4,6-11,13-29
```

コマンド:
```bash
% python3 nw_vlan.py -by -cf testfile/config_vlan.txt
```

出力:
```
- 1
- 2
- 3
- 5
- 6
- 7
- 8
- 9

- 2
- 3
- 4
- 6
- 7
- 8
- 9
- 10
- 11
- 13
- 14
- 15
- 16
- 17
- 18
- 19
- 20
- 21
- 22
- 23
- 24
- 25
- 26
- 27
- 28
- 29
```

### 例2: YAMLリストファイルからコンフィグ形式への変換

`testfile/yaml_list` の内容:
```yaml
- 1
- 2
- 3
- 4
- 6
```

コマンド:
```bash
% python3 nw_vlan.py -yf testfile/yaml_list
```

出力:
```
1-4,6
```

### 例3: Pythonリストファイルからコンフィグ形式への変換 (新規追加)

`testfile/pylist.py` の内容:
```python
[10, 20, 21, 22, 30]
```

コマンド:
```bash
% python3 nw_vlan.py -f testfile/pylist.py
```

出力:
```
10,20-22,30
```

### 例4: JSONリストファイルからコンフィグ形式への変換 (新規追加)

`testfile/json_list` の内容:
```json
[100, 101, 102, 105]
```

コマンド:
```bash
% python3 nw_vlan.py -jf testfile/json_list
```

出力:
```
100-102,105
