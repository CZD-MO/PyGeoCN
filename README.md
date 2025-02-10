# Geo-Reverse Lookup for China

提供了离线处理中国境内经纬度坐标逆地理编码的功能，使用经纬度坐标查询地理位置信息（包括位置和行政编码），最细的粒度到区县级市。

## 安装

你可以通过以下命令安装这个包：

```bash
pip install pygeo-cn
#确保你已经安装了pip和wheel：
```

## 使用方法

```python
#使用这个包，你可以调用regeo函数来获取指定坐标点所在的省、市和县信息：
from PyGeoCN.regeo import regeo

latitude = 31.924167 # 纬度
longitude = 120.492326  # 经度

result = regeo(latitude, longitude)
print(result)

# 输出结果：
# {'status': 1, 'source': 'Internal', 'Info': 'Successfully retrieved address.', 'address': {'province': '江苏省', 'province_code': '156320000', 'city': '苏州市', 'city_code': '156320500', 'district': '张家港市', 'district_code': '156320582'}}
```

## 返回值结构

```
{
  "status": 1, # 1为成功，0为失败
  "source": "Internal",  # Internal为引用内部数据，External为引用外部数据
  "Info": "Successfully retrieved address.", # 返回信息概述
  "address": {
    "province": "江苏省",  # 省份
    "province_code": "156320000", 省份行政编码
    "city": "苏州市",  # 城市
    "city_code": "156320500", # 城市行政编码
    "district": "张家港市", # 区县
    "district_code": "156320582"  # 区县行政编码
  }
}
```

## 数据来源

数据来源于[天地图](https://cloudcenter.tianditu.gov.cn/administrativeDivision/)，地图数据可能会更新，如果pygeo-cn包的数据未及时更新可自行去天地图下载，然后使用自己下载的地理坐标数据,并重命名成固定的文件名（chain_province.geojson(省份坐标数据)、china_city.geojson（城市坐标数据）、china_district.geojson（区县坐标数据）），使用时只需要再传入指定的目录即可：

```python
from PyGeoCN.regeo import regeo

latitude = 31.924167 # 纬度
longitude = 120.492326  # 经度
# 下载包存放目录路径
geo_dir = "/data"
result = regeo(latitude, longitude,geo_dir)
print(result)

# 输出结果：
# {'status': 1, 'source': 'External', 'Info': 'Successfully retrieved address.', 'address': {'province': '江苏省', 'province_code': '156320000', 'city': '苏州市', 'city_code': '156320500', 'district': '张家港市', 'district_code': '156320582'}}
```

## 注意事项

```
确保你的Python环境支持Unicode文件名，因为坐标库中包含中文字符。
这个包仅适用于中国的坐标点的逆地址编码。
```
