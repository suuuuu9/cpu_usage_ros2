# cpu_usage_ros2
[![test](https://github.com/suuuuu9/cpu_usage_ros2/actions/workflows/test.yml/badge.svg)](https://github.com/suuuuu9/cpu_usage_ros2/actions/workflows/test.yml)
![License](https://img.shields.io/github/license/suuuuu9/Data-Analytics)

CPUの使用率をリアルタイムで出力するROS2パッケージです。
[psutil](https://psutil.readthedocs.io/en/latest/)ライブラリを使用し使用率[%]を出力します。

## ダウンロード方法
このリポジトリをローカル環境にクローンするには以下のコマンドを使用してください。
```bash
$ git clone
```

## 使い方
ディレクトリ```cpu_usage_ros2```に移動後、標準入力で数値を入力し```ros2 run launch usage.launch.py```を実行します。
このとき別ターミナルで```ros2 topic echo /cpu_usage```

## 依存関係
このパッケージは

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- © 2025 SUzuha Kiuchi
