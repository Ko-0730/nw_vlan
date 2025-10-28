#!/bin/bash

echo "nw_vlan のインストールを開始します..."

# 仮想環境の作成とアクティベート
if [ ! -d ".venv" ]; then
    echo "仮想環境を作成します..."
    python3 -m venv .venv
fi

echo "仮想環境をアクティベートします..."
source .venv/bin/activate

# 依存関係のインストール
echo "依存関係をインストールします..."
pip install -r requirements.txt

# パッケージのインストール
echo "nw_vlan パッケージをインストールします..."
pip install .

echo "インストールが完了しました。"
echo "仮想環境をアクティベートするには 'source .venv/bin/activate' を実行してください。"
echo "nw_vlan コマンドは仮想環境内で利用可能です。"
