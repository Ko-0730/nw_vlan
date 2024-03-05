# nw_vlan

NW機器のVlanの並びをlistにしたい時や、listをNW機器のconfigのVlanっぽく変換したいときに多分使えます。

## 動作確認している環境
Python 3.12.2

## 使い方
1. git cloneやら何やらしてローカルにDL


2. cdでnw_vlan.pyのある階層に移動する


3. (初回のみ)以下のコマンドでパッケージのインストールを実施する


`python3 -m pip install -r requirements.txt`


4. やりたいことに応じてコードを叩く

### NW機器のconfig形式のvlanをlistにしたい場合
`python3 nw_vlan.py -c "1-3,5-7"`

### NW機器のconfig形式のvlanをjsonのlistにしたい場合
`python3 nw_vlan.py -c "1-3,5-7" -bj`

### NW機器のconfig形式のvlanをyamlのlistにしたい場合
`python3 nw_vlan.py -c "1-3,5-7" -by`

### NW機器のconfig形式のvlanをflowスタイルのyamlのlistにしたい場合
`python3 nw_vlan.py -c "1-3,5-7" -bfy`

### NW機器のconfig形式のvlanが記載されたファイルを読み込んでlistにしたい場合
`python3 nw_vlan.py -cf {filename}`

### NW機器のconfig形式のvlanが記載されたファイルを読み込んでjsonのlistにしたい場合
`python3 nw_vlan.py -cf {filename} -bj`

### NW機器のconfig形式のvlanが記載されたファイルを読み込んでyamlのlistにしたい場合※1
`python3 nw_vlan.py -cf {filename} -by`

### NW機器のconfig形式のvlanが記載されたファイルを読み込んでflowスタイルのyamlのlistにしたい場合
`python3 nw_vlan.py -cf {filename} -bfy`

### pythonのlist(ファイル)をconfigのvlanの形にしたい場合
`python3 nw_vlan.py -f {filename}`

### yaml形式のlist(ファイル)をconfigのvlanの形にしたい場合※2
`python3 nw_vlan.py -yf {filename}`

### json形式のlist(ファイル)をconfigのvlanの形にしたい場合
`python3 nw_vlan.py -jf {filename}`

## 実行例

上記※1,※2を実行した際の挙動です。
### 例1
```
% cat testfile/config_vlan.txt
1-3,5-9,11
2-4,6-11,13-29

% python3 nw_vlan.py -by -cf testfile/config_vlan.txt
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


### 例2
```
% cat testfile/yaml_list
- 1
- 2
- 3
- 4
- 6

% python3 nw_vlan.py -yf testfile/yaml_list
1-4,6
```
