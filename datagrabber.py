import pytools

# base data (open weather map, slower)
# --- https://openweathermap.org/api
def getBaseData(url):
    print('Getting Base Data...')
    # url: http://api.openweathermap.org/data/2.5/weather?lat=<lat>&lon=<lon>&appid=<appid>
    data = pytools.net.getJsonAPI(url)
    # [windspeeds, windgusts, visibility, snow]
    try:
        speed = float(data['wind']['speed'])
    except:
        speed = 0
    try:
        gusts = float(data['wind']['gust'])
    except:
        gusts = 0
    try:
        snow = float(data['snow']['1h'])
    except:
        try:
            snow = float(data['snow']['3h'])
        except:
            snow = 0
    array = [speed, gusts, float(data['visibility']), snow]
    print(array)
    return array

# fast data (weather underground, faster)
# --- https://docs.google.com/document/d/1eKCnKXI9xnoMGRRzOL1xPCBihNV2rOet08qpE_gArAY
def getFastData(url):
    print('Getting Fast Data...')
    # url: https://api.weather.com/v2/pws/observations/current?stationId=INOVASCO146&format=json&units=s&apiKey=<apiKey>
    data = pytools.net.getJsonAPI(url)
    # [rainRate, rainTotal, pressure, temp]
    rainRate = data['observations'][0]['metric_si']['precipRate']
    rainTotal = data['observations'][0]['metric_si']['precipTotal']
    pressure = data['observations'][0]['metric_si']['pressure']
    temp = data['observations'][0]['metric_si']['temp']
    array = [float(rainRate) * 2, float(rainTotal) * 10, float(pressure), float(temp)]
    print(array)
    return array

    