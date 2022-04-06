import datagrabber
import pytools
import wind
import rain
import snow
import pres
import temp
import visi
import alertDeployer
import time

# Globals
windLevel = 0
rainLevel = 0
snowLevel = 0
presLevel = 0
tempLevel = 0
visiLevel = 0
baseMin = 0
fastMin = 0

# handlers class, is the primary code for data collection and interfacing.
# replace corrisponding fields in api links with correct values. Documentation references can be found in datagrabber.py
class handlers:
    class data:
        def handler(dataArray):
            global baseMin
            global fastMin
            dataa = dataArray[0]
            datab = dataArray[1]
            dateArray = pytools.clock.getDateTime()
            if (((dateArray[4] / 15) % 1) == 0.0) and (baseMin != dateArray[4]):
                baseMin = dateArray[4]
                dataold = dataa
                try:
                    dataa = datagrabber.getBaseData('http://api.openweathermap.org/data/2.5/weather?lat=<lat>&lon=<lon>&appid=<appid>')
                except:
                    dataa = dataold
            if (((dateArray[4] / 2) % 1) == 0.0) and (fastMin != dateArray[4]):
                fastMin = dateArray[4]
                dataold = datab
                try:
                    datab = datagrabber.getFastData('https://api.weather.com/v2/pws/observations/current?stationId=INOVASCO146&format=json&units=s&apiKey=<apiKey>')
                except:
                    datab = dataold
            return [dataa, datab]

        def startHandler():
            try:
                dataa = datagrabber.getBaseData('http://api.openweathermap.org/data/2.5/weather?lat=<lat>&lon=<lon>&appid=<appid>')
                datab = datagrabber.getFastData('https://api.weather.com/v2/pws/observations/current?stationId=INOVASCO146&format=json&units=s&apiKey=<apiKey>')
            except:
                dataa = [0.0, 0.0, 15000.0, 0.0]
                datab = [0.0, 0.0, 1000.0, 15.0]
            return [dataa, datab]
    
    # alerts class, defines alert types and running detection code.
    class alerts:
        def wind(dataArray):
            global windLevel
            global rainLevel
            global snowLevel
            global presLevel
            global tempLevel
            global visiLevel
            level = wind.returnAlertLevel(dataArray[0][1], dataArray[0][0])
            if level != windLevel:
                windLevel = level
                alertDeployer.wind.deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel)

        def rain(dataArray):
            global windLevel
            global rainLevel
            global snowLevel
            global presLevel
            global tempLevel
            global visiLevel
            level = rain.returnAlertLevel(dataArray[1][0])
            if level != rainLevel:
                rainLevel = level
                alertDeployer.rain.deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel)

        def snow(dataArray):
            global windLevel
            global rainLevel
            global snowLevel
            global presLevel
            global tempLevel
            global visiLevel
            level = snow.returnAlertLevel(dataArray[0][3])
            if level != snowLevel:
                snowLevel = level
                alertDeployer.snow.deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel)

        def pres(dataArray):
            global windLevel
            global rainLevel
            global snowLevel
            global presLevel
            global tempLevel
            global visiLevel
            level = pres.returnAlertLevel(dataArray[1][2])
            if level != presLevel:
                presLevel = level
                alertDeployer.pres.deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel)

        def temp(dataArray):
            global windLevel
            global rainLevel
            global snowLevel
            global presLevel
            global tempLevel
            global visiLevel
            level = temp.returnAlertLevel(dataArray[1][3])
            if level != tempLevel:
                tempLevel = level
                alertDeployer.temp.deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel)

        def visi(dataArray):
            global windLevel
            global rainLevel
            global snowLevel
            global presLevel
            global tempLevel
            global visiLevel
            level = visi.returnAlertLevel(dataArray[0][2])
            if level != visiLevel:
                visiLevel = level
                alertDeployer.visi.deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel)

# Running code
def main():
    dataArray = handlers.data.startHandler()
    while True:
        dataArray = handlers.data.handler(dataArray)
        handlers.alerts.wind(dataArray)
        handlers.alerts.rain(dataArray)
        handlers.alerts.snow(dataArray)
        handlers.alerts.pres(dataArray)
        handlers.alerts.temp(dataArray)
        handlers.alerts.visi(dataArray)
        time.sleep(1)

main()