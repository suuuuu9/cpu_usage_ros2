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
```

## 使い方
```bash
# 実行
ros2 run cpu_usage_ros2 cpu_usage
```
このとき別の端末でros2を使ってサブスクライブして確認できます。
```bash
ros2 topic echo /cpu_usage
```

## ノード
**cpu_usage**  
- cpuの使用率をパブリッシュします。

## 必要なソフトウェア
- Python (動作確認済み 3.10)
- psutil (動作確認済み 5.9.0)

## テスト環境
- Ubuntu 22.04 LTS
- ROS2 humble

## 依存関係
このパッケージはpsutilライブラリを使用しています。

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- © 2025 SUzuha Kiuchi
