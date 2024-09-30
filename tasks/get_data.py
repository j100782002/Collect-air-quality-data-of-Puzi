from datetime import datetime 
import requests
currentDateAndTime = datetime.now()

print(type(currentDateAndTime.strftime(r"%Y%m%d%H")))


ymdh = currentDateAndTime.strftime(r"%Y%m%d%H")

ymdh = str(int(ymdh)-1)

url = f"https://airtw.moenv.gov.tw/json/airlist/airlist_21_{ymdh}.json"

response = requests.get(url)
data = response.json()

print(data)