# VisualKit

从 CSV 到可交互可视化界面

## CSV 格式

- 无表头
- 5 栏，分别为
  1. X 坐标
  2. Y 坐标
  3. 颜色 tag
  4. 预留
  5. 内部消息

- 每一行是一个数据点

## 用法

```shell
$ python3 setup.py [data.csv]
```

生成的 html 会保存到 `./projects/` 中

## 注意

1. 颜色 tag 那一栏只要给需要着相同颜色的数据点相同的 tag 即可，会自动生成一种独特的颜色
2. 内部消息那一栏在鼠标移动到对应的数据点上时会展示

## 关于

基于 highcharts，感谢 USTC Linux User Group 提供协助