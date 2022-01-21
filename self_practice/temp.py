# coding: utf-8
# @Author : lryself
# @Date : 2021/2/3 10:39
# @Software: PyCharm
import json

import requests

if __name__ == '__main__':
    url = "https://api.map.baidu.com/reverse_geocoding/v3/?output=json&coordtype=wgs84ll"
    lat = "38.43971"
    lng = "106.21974"
    data = {"ak": '0hYGiH3Ob5ZhV0eWzrGVXCD3bEdBCi6L', "location": lat + ',' + lng}
    response = requests.get(url=url+"&ak={}&location={}".format(data["ak"], data["location"]), data=data)
    print(response)
    print(json.loads(response.text))
    var = {"type": "complete",
           "info": "SUCCESS",
           "status": 1,
           "$Da": "jsonp_424797_",
           "position": {"Q": 38.43971, "R": 106.21974, "lng": 106.21974, "lat": 38.43971},
           "message": "Get ipLocation success.Get address success.",
           "location_type": "ip",
           "accuracy": null,
           "isConverted": true,
           "addressComponent": {"citycode": "0951", "adcode": "640106", "businessAreas": [], "neighborhoodType": "",
                                "neighborhood": "", "building": "", "buildingType": "", "street": "宁安大街",
                                "streetNumber": "ibi号", "country": "中国", "province": "宁夏回族自治区", "city": "银川市",
                                "district": "金凤区", "township": "长城中路街道"},
           "formattedAddress": "宁夏回族自治区银川市金凤区长城中路街道宁夏绿叶信息科技有限公司",
           "roads": [],
           "crosses": [],
           "pois": []
           }
