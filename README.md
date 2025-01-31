# robosys2024 ROS 2

## このパッケージについて
* このパッケージは、2024年ロボットシステム学課題2で作成したパッケージです。

## 使用方法

このリポジトリーをROS 2 ワークスペースのsrc下にクローンしてください.
```
https://github.com/Yuukizaka/mypkg.git
```
そしてタブを2つ用意します。
そのうちの一つにtalker.pyを、もう一つにlistener.pyをを立ち上げてください。
##実行方法
talker.pyの場合  
```
ros2 run mypkg talker talker.py
```    
listener.pyの場合
```
ros2 topic echo /sensor_data
```
##実行結果
talker.pyを実行した場合
```
[INFO] [1737308013.486313086] [talker]: Sensor Publisher Node is running.
[INFO] [1737308014.520027228] [talker]: Published temperature: 20.39 °C
[INFO] [1737308015.521257900] [talker]: Published temperature: 23.91 °C
[INFO] [1737308016.474940986] [talker]: Published temperature: 23.10 °C
[INFO] [1737308017.493496431] [talker]: Published temperature: 20.83 °C
[INFO] [1737308018.501262884] [talker]: Published temperature: 27.85 °C
[INFO] [1737308019.474617413] [talker]: Published temperature: 29.34 °C
[INFO] [1737308020.476956091] [talker]: Published temperature: 28.28 °C
[INFO] [1737308021.485883029] [talker]: Published temperature: 27.99 °C
[INFO] [1737308022.481536050] [talker]: Published temperature: 22.07 °C
[INFO] [1737308023.474744922] [talker]: Published temperature: 22.49 °C
[INFO] [1737308024.481352566] [talker]: Published temperature: 27.05 °C
[INFO] [1737308025.476644632] [talker]: Published temperature: 29.30 °C
```
listener.pyを実行した場合
```
data: 28.593793869018555
---
data: 27.33355712890625
---
data: 24.48151206970215
---
data: 29.760889053344727
---
data: 24.597753524780273
---
data: 22.88915252685547
---
data: 22.71689796447754
---
data: 25.828495025634766
---
data: 25.53400230407715
---
data: 28.87436294555664
```
## 開発環境
* Ubuntu 22.04 LTS
* ROS 2 Humble Hawksb

## テスト環境
* Ubuntu 22.04 LTS

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2024 yuuki ishizaka
