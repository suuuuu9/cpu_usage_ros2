# cpu_usage_ros2
[![test](https://github.com/suuuuu9/cpu_usage_ros2/actions/workflows/test.yml/badge.svg)](https://github.com/suuuuu9/cpu_usage_ros2/actions/workflows/test.yml)
![License](https://img.shields.io/github/license/suuuuu9/Data-Analytics)

CPUの使用率をリアルタイムで出力するROS2パッケージです。  
[psutil](https://psutil.readthedocs.io/en/latest/)ライブラリを使用し使用率[%]を出力します。

## インストール方法
### psutil
psutilライブラリを使用しているためインストールしてください。
```bash
pip install psutil
```
### パッケージ
以下のコマンドを使用してパッケージをインストールしてください。
```bash
# ダウンロード
cd ~/<ワークスペース名>/src
git clone https://github.com/suuuuu9/cpu_usage_ros2.git

# ビルド
cd ~/<ワークスペース名>
colcon build
source ~/ros2_ws/install/setup.bash

# ３行目のコマンドは、~/.bashrcに書いておくことを推奨します。   
# 下のコマンドで.bashrcに追記できます。  
echo 'source ~/ros2_ws/install/setup.bash' >> ~/.bachrc
# .bashrcに書いてあるとき下のコマンドが代わりにできます。
source ~/.bashrc
```

## 使い方
```ros2 run launch usage.launch.py```で実行できます。
このとき別の端末で```ros2 topic echo /cpu_usage```でros2を使ってサブスクライブして確認できます。

## ノード
**cpu_usage**
cpuの使用率をパブリッシュします。

## 必要なソフトウェア
- Python
- psutil

## テスト環境
- Ubuntu 22.04 LTS
- ROS2 humble

## 依存関係
このパッケージはpsutilライブラリを使用しています。

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- © 2025 SUzuha Kiuchi
