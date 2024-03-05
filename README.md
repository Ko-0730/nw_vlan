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

### NW機器のconfig形式のvlanが記載されたファイルを読み込んでyamlのlistにしたい場合
`python3 nw_vlan.py -cf {filename} -by`

### NW機器のconfig形式のvlanが記載されたファイルを読み込んでflowスタイルのyamlのlistにしたい場合
`python3 nw_vlan.py -cf {filename} -bfy`

### pythonのlist(ファイル)をconfigのvlanの形にしたい場合
`python3 nw_vlan.py -f {filename}`

### yaml形式のlist(ファイル)をconfigのvlanの形にしたい場合
`python3 nw_vlan.py -yf {filename}`

### json形式のlist(ファイル)をconfigのvlanの形にしたい場合
`python3 nw_vlan.py -jf {filename}`
