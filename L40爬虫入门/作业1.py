import urllib.request
import json

url = 'http://t.weather.sojson.com/api/weather/city/101180101'

resp = urllib.request.urlopen(url)
if resp.code == 200:
    weather_json = resp.read().decode('utf-8')
    weather_data = json.loads(weather_json)

    data = weather_data['data']
    yesterday = data['yesterday']

    yesterday_ymd = yesterday['ymd']
    yesterday_week = yesterday['week']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    yesterday_type = yesterday['type']
    print(yesterday_ymd, yesterday_week, yesterday_high, yesterday_low, yesterday_type)

    forecast = data['forecast']
    for list in forecast:
        forecast_ymd = list['ymd']
        forecast_week = list['week']
        forecast_high = list['high']
        forecast_low = list['low']
        forecast_type = list['type']
        # print(forecast_ymd, forecast_week, forecast_high, forecast_low, forecast_type)

