import geopandas as gpd
from shapely.geometry import Point
import os

# 离线逆地理编码
def regeo(latitude,longitude,path=""):
    # 加载 GeoJSON 文件
    package_dir = os.path.dirname(__file__)

    source = "Internal"
    if path:
        try:
            source = "External"
            geojson_file_p = os.path.join(path,"china_province.geojson")
            geojson_file_c = os.path.join(path,"china_city.geojson")
            geojson_file_d = os.path.join(path,"china_district.geojson")
        except Exception as e:
            data = {
                "status": 0,
                "source": source,
                "Info": "External geographic data package not found.",
                "address": {
                    "province": None,
                    "province_code": None,
                    "city": None,
                    "city_code": None,
                    "district": None,
                    "district_code": None
                }
            }
            return data
    else:
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
            "source": source,
            "Info": "Successfully retrieved address.",
            "address": {
                "province": matched_region_p.iloc[0]['name'],
                "province_code": matched_region_p.iloc[0]['gb'],
                "city": matched_region_c.iloc[0]['name'],
                "city_code": matched_region_c.iloc[0]['gb'],
                "district": matched_region_d.iloc[0]['name'],
                "district_code": matched_region_d.iloc[0]['gb']
            }
        }
        return data
    except:
        data = {
            "status": 0,
            "source": source,
            "Info": "Address not retrieved; coordinates are outside of China or beyond the scope of the coordinate database.",
            "address": {
                "province": None,
                "province_code": None,
                "city": None,
                "city_code": None,
                "district": None,
                "district_code": None
            }
        }
    return data
    
        