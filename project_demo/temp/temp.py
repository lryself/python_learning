# coding: utf-8
# @Author : lryself
# @Date : 2021/2/3 10:39
# @Software: PyCharm
# import json

# import requests

# if __name__ == '__main__':
#     url = "https://api.map.baidu.com/reverse_geocoding/v3/?output=json&coordtype=wgs84ll"
#     lat = "38.43971"
#     lng = "106.21974"
#     data = {"ak": '0hYGiH3Ob5ZhV0eWzrGVXCD3bEdBCi6L', "location": lat + ',' + lng}
#     response = requests.get(url=url+"&ak={}&location={}".format(data["ak"], data["location"]), data=data)
#     print(response)
#     print(json.loads(response.text))
#     var = {"type": "complete",
#            "info": "SUCCESS",
#            "status": 1,
#            "$Da": "jsonp_424797_",
#            "position": {"Q": 38.43971, "R": 106.21974, "lng": 106.21974, "lat": 38.43971},
#            "message": "Get ipLocation success.Get address success.",
#            "location_type": "ip",
#            "accuracy": null,
#            "isConverted": true,
#            "addressComponent": {"citycode": "0951", "adcode": "640106", "businessAreas": [], "neighborhoodType": "",
#                                 "neighborhood": "", "building": "", "buildingType": "", "street": "宁安大街",
#                                 "streetNumber": "ibi号", "country": "中国", "province": "宁夏回族自治区", "city": "银川市",
#                                 "district": "金凤区", "township": "长城中路街道"},
#            "formattedAddress": "宁夏回族自治区银川市金凤区长城中路街道宁夏绿叶信息科技有限公司",
#            "roads": [],
#            "crosses": [],
#            "pois": []
#            }
# if __name__ == '__main__':
#     s = json.dumps([450, 463, 466, 490, 496, 505])
#     print(s)

import requests

if __name__ == '__main__':
    # kwargs = [{
    #             'PaperID': "2022031015128931",
    #             'FromTaskID': "2022031119295367",
    #             'FromType': "3"
    #         }]

    # kwargs = [{"NextType": 4, "NextUserID": 2022030917364093, "NextUserName": "\u5f90\u4e13\u5bb6",
    #             "Workunit": "\u534e\u7535"}, {"NextType": 4, "NextUserID": 2022030717000531, "NextUserName": "\u5f90\u4e13\u5bb6",
    #             "Workunit": "\u534e\u7535"}]
    # print(json.dumps(kwargs))
    resp = requests.post("http://localhost:5000/api_2_0//paper/download", data={
        "UserID": "202201111700",
        "PaperID": "2022031817204206",
        "UserType": "2"
    }, headers={"token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTY0NzU5NTI2NSwiZXhwIjoxNjQ4NTk1MjY0fQ.eyJpZCI6IjIwMjIwMTExMTcwMCIsInVzZXJfdHlwZSI6Mn0.V3tLF6xVnje3oR7pMf4gc799CHdG_GXW5GzhoLs0gIZELlSpIJmWaRCvukiZmY0BTOTWrXj3Kwgvidy6ROo53g"})
    print(resp)
