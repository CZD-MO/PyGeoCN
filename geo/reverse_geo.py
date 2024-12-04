import geopandas as gpd
from shapely.geometry import Point
import os

def reverse_geo(latitude,longitude):
    # 加载 GeoJSON 文件
    package_dir = os.path.dirname(__file__)

    geojson_file_p = os.path.join(package_dir,"中国_省.geojson")
    geojson_file_c = os.path.join(package_dir,"中国_市.geojson")
    geojson_file_d = os.path.join(package_dir,"中国_县.geojson")

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
        return [matched_region_p.iloc[0]['name'],matched_region_c.iloc[0]['name'], matched_region_d.iloc[0]['name']]
    except Exception as e:
        return []