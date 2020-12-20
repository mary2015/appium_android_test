from datetime import datetime
from datetime import timedelta
import requests
import json


url ="https://pda.weather.gov.hk/locspc/android_data/fnd_e.xml"
headers ={
"Cache-Control": "no-cache",
"Host": "pda.weather.gov.hk",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip"
}

res = requests.request("GET", url, headers=headers)
if res.status_code == 200 :
    print("response status is successful!")
else:
    print("response status is not successful!")

res_json = json.loads(res.text)
the_day_after_tomorrow =datetime.now() + timedelta(days=2)
Date_Formatted = the_day_after_tomorrow.strftime('%Y%m%d')
print(Date_Formatted)
for item in res_json["forecast_detail"]:
    if  Date_Formatted == item["forecast_date"]:
        min_humidity = item["min_rh"]
        max_humidity = item["max_rh"]
        print("the relative min humidity is " + str(min_humidity) +"%")
        print("the relative max humidity is " + str(max_humidity) +"%")


