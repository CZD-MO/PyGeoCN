# Geo-Reverse Lookup for China

提供了逆地理编码的功能，使用经纬度坐标查询地理位置，最细的粒度到县级市。

## 安装

你可以通过以下命令安装这个包：

```bash
pip install geo
#确保你已经安装了pip和wheel：
```

## 使用方法
```python
#使用这个包，你可以调用reverse_geo函数来获取指定坐标点所在的省、市和县信息：
from geo import reverse_geo

# 示例用法
latitude = 39.9042  # 纬度
longitude = 116.4074  # 经度
regions = reverse_geo(latitude, longitude)

if regions:
    print(f"该点位于: {regions[0]} - {regions[1]} - {regions[2]}")
else:
    print("该点不在中国境内或不在坐标库内")
```




## 包结构
```
geo/
│
├── setup.py
├── geo/
│   ├── __init__.py
│   ├── reverse_geo.py
│   ├── 中国_省.geojson
│   ├── 中国_市.geojson
│   └── 中国_县.geojson
├── README.md
├── MANIFEST.in
└── LICENSE
```

## 注意事项
```
确保你的Python环境支持Unicode文件名，因为GeoJSON文件名包含中文字符。
这个包仅适用于中国的坐标点。如果输入的坐标不在中国境内，函数将返回一个空列表。
```
