# import requests
#
# if __name__ == '__main__':
#     # requests.get("https://www.example.com")
#     # print(val_req.text)
#
#     val_req = requests.get("https://www.example.com")
#     print(val_req.text)
#
#     print(val_req.status_code)
#
#     dict_param = {
#         "latitude": 53.32,
#         "longitude": -6.41,
#         "current": ["temperature_2m"],
#     }
#     req = requests.get("https://api.open-meteo.com/v1/forecast", dict_param)
#     # print(req.text)
#     var_2 = req.json()
#     var_3 = var_2["current"]
#     print(var_3)
#     # print(req.json()["current"])

import requests

if __name__ == '__main__':

    dict_1 = {
        "latitude": 52.5244,
        "longitude": 13.4105,
        "current": ["wind_speed_10m"],

    }

    req = requests.get("https://api.open-meteo.com/v1/forecast", dict_1)

    print(req.json()["current"])

