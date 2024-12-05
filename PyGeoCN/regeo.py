import geopandas as gpd
from shapely.geometry import Point
import os

def regeo(latitude,longitude):
    # 加载 GeoJSON 文件
    package_dir = os.path.dirname(__file__)

    geojson_file_p = os.path.join(package_dir,"china_province.geojson")
    geojson_file_c = os.path.join(package_dir,"china_city.geojson")
    geojson_file_d = os.path.join(package_dir,"china_district.geojson")

    geo_data_p = gpd.read_file(geojson_file_p)
    geo_data_c = gpd.read_file(geojson_file_c)
    geo_data_d = gpd.read_file(geojson_file_d)

    # 创建一个坐标点
    point = Point(longitude, latitude)

    # 判断坐标点属于哪个区域
    matched_region_p = geo_data_p[geo_data_p.contains(point)]
    matched_region_c = geo_data_c[geo_data_c.contains(point)]
    matched_region_d = geo_data_d[geo_data_d.contains(point)]

    
    try:
        data = {
            "status": 1,
            "Info": "Successfully retrieved address.",
            "address": {
                "province": matched_region_p.iloc[0]['name'],
                "city": matched_region_c.iloc[0]['name'],
                "district": matched_region_d.iloc[0]['name'],
            }
        }
        return data
    except:
        data = {
            "status": 0,
            "Info": "Address not retrieved; coordinates are outside of China or beyond the scope of the coordinate database.",
            "address": {
                "province": None,
                "city": None,
                "district": None,
            }
        }
    return data
    
        