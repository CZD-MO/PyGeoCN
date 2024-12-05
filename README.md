# Geo-Reverse Lookup for China

提供了处理中国境内经纬度坐标逆地理编码的功能，使用经纬度坐标查询地理位置，最细的粒度到县级市。

## 安装

你可以通过以下命令安装这个包：

```bash
pip install geo
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
# {'status': 1, 'Info': 'Successfully retrieved address.', 'address': {'province': '江苏省', 'city': '苏州市', 'district': '张家港市'}}
```

## 返回值结构

```
{
  "status": 1, # 1为成功，0为失败
  "Info": "Successfully retrieved address.", # 是否返回信息概述
  "address": {
    "province": "江苏省",  # 省
    "city": "苏州市",  # 市
    "district": "张家港市", #区县
  }
}
```

## 注意事项

```
确保你的Python环境支持Unicode文件名，因为坐标库中包含中文字符。
这个包仅适用于中国的坐标点的逆地址编码。
```
