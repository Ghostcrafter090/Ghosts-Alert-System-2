import json
import os
import sys
from win32api import GetModuleHandle, PostQuitMessage
import win32con
from win32gui import NIF_ICON, NIF_INFO, NIF_MESSAGE, NIF_TIP, NIM_ADD, NIM_DELETE, NIM_MODIFY, WNDCLASS, CreateWindow, DestroyWindow, LoadIcon, LoadImage, RegisterClass, Shell_NotifyIcon, UpdateWindow
import psutil
import ssl
import smtplib
import urllib
from PIL import Image
from PIL import ImageColor
import subprocess
import requests
from io import BytesIO
from urllib.request import urlopen
from datetime import datetime
import ctypes
from bs4 import BeautifulSoup
import math as mather

class system:
    def getCPU(wait):
        error = 0
        try:
            temp = 50
            temp = psutil.cpu_percent(float(wait))
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            temp = error
        return temp

class IO:
    def getJson(path):
        error = 0
        try:
            file = open(path, "r")
            jsonData = json.loads(file.read())
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            jsonData = error
        return jsonData

    def saveJson(path, jsonData):
        error = 0
        try:
            file = open(path, "w")
            file.write(json.dumps(jsonData))
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        return error

    def getFile(path):
        error = 0
        try:
            file = open(path, "r")
            jsonData = file.read()
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            jsonData = error
        return jsonData

    def saveFile(path, jsonData):
        error = 0
        try:
            file = open(path, "w")
            file.write(jsonData)
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        return error

class winAPI:
    def getWallpaper():
        sbuf = ctypes.create_string_buffer(512) # ctypes.c_buffer(512)
        ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_GETDESKWALLPAPER,len(sbuf),sbuf,0)
        return sbuf.value

    def setWallpaper(path):
        changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
        ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER,0,path.encode(),changed) # "".encode() = b""

    class WindowsBalloonTip:
        def __init__(self, title, msg):
            message_map = {
                    win32con.WM_DESTROY: self.OnDestroy,
            }
            # Register the Window class.
            wc = WNDCLASS()
            hinst = wc.hInstance = GetModuleHandle(None)
            wc.lpszClassName = "PythonTaskbar"
            wc.lpfnWndProc = message_map # could also specify a wndproc.
            classAtom = RegisterClass(wc)
            # Create the Window.
            style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
            self.hwnd = CreateWindow( classAtom, "Taskbar", style, \
                    0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                    0, 0, hinst, None)
            UpdateWindow(self.hwnd)
            iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            try:
                hicon = LoadImage(hinst, iconPathName, \
                        win32con.IMAGE_ICON, 0, 0, icon_flags)
            except:
                hicon = LoadIcon(0, win32con.IDI_APPLICATION)
                flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
                nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
                Shell_NotifyIcon(NIM_ADD, nid)
                Shell_NotifyIcon(NIM_MODIFY, \
                            (self.hwnd, 0, NIF_INFO, win32con.WM_USER+20,\
                            hicon, "Balloon  tooltip",msg,200,title))
                # self.show_balloon(title, msg)
                os.times.sleep(10)
                DestroyWindow(self.hwnd)
        def OnDestroy(self, hwnd, msg, wparam, lparam):
            nid = (self.hwnd, 0)
            Shell_NotifyIcon(NIM_DELETE, nid)
            PostQuitMessage(0) # Terminate the app.

    def balloon_tip(title, msg):
        w=winAPI.WindowsBalloonTip(title, msg)

class calc:
    def tempCalc(temp):
        if temp > 298:
            temptype = "hot"
        elif temp > 285:
            temptype = "warm"
        elif temp > 273:
            temptype = "cool"
        elif temp > 263:
            temptype = "cold"
        elif temp <= 263:
            temptype = "freeze"
        else:
            temptype = "warm"
        return temptype

    def saturateRGB(rgb):
        rgbn = [0, 0, 0]
        if rgb[0] > rgb[1]:
            maxRGB = rgb[0]
        else:
            maxRGB = rgb[1]
        if rgb[2] > maxRGB:
            maxRGB = rgb[2]
        if rgb[0] < rgb[1]:
            minRGB = rgb[0]
        else:
            minRGB = rgb[1]
        if rgb[2] < maxRGB:
            minRGB = rgb[2]
        satMult = 255 / maxRGB
        if minRGB == rgb[0]:
            rgbn[0] = int(rgb[0] / satMult)
        elif maxRGB == rgb[0]:
            rgbn[0] = int(rgb[0] * satMult)
        else:
            rgbn[0] = rgb[0]
        if minRGB == rgb[1]:
            rgbn[1] = int(rgb[1] / satMult)
        elif maxRGB == rgb[1]:
            rgbn[1] = int(rgb[1] * satMult)
        else:
            rgbn[1] = rgb[1]
        if minRGB == rgb[2]:
            rgbn[2] = int(rgb[2] / satMult)
        elif maxRGB == rgb[2]:
            rgbn[2] = int(rgb[2] * satMult)
        else:
            rgbn[2] = rgb[2]
        return rgbn
    
    def subtractLarge(numbera, numberb):
            i = 0
            out = ""
            next = numbera[-(i + 1)]
            while i < len(numbera):
                if numbera[-(i + 1)] != next:
                    math = next - int(numberb[-(i + 1)])
                else:
                    math = int(numbera[-(i + 1)]) - int(numberb[-(i + 1)])
                if math < 0:
                    try:
                        next = int(numbera[-(i + 2)]) - 1
                    except:
                        next = 0 - 1
                    math = math + 10
                else:
                    try:
                        next = int(numbera[-(i + 2)])
                    except:
                        next = 0
                if math < 0:
                    math = 0
                out = str(out) + str(math)
                i = i + 1

    def findLargestPrime(x):
        print("The factors of",x,"are:")
        nonprime = [0]
        i = 1
        exit = 0
        while exit == 0:
            if x % i == 0:
                x = x / i
                n = x
            if i > (n / 2):
                exit = 1
            i = i + 1
        return n

    def addLarge(numbera: str, numberb: str):
        if numbera.find('-') != -1:
            nega = '-'
        else:
            nega = ''
        if numberb.find('-') != -1:
            negb = '-'
        else:
            negb = ''
        numbera = numbera.replace('-', '')
        numberb = numberb.replace('-', '')
        if numbera.find(".") == -1:
            numbera = numbera + ".0"
        if numberb.find(".") == -1:
            numberb = numberb + ".0"
        print(numbera + ";" + numberb)
        decimalloc = calc.findLargestDecimal(numbera, numberb)
        numbera = numbera.replace('.', '')
        numberb = numberb.replace('.', '')
        i = 0
        out = ""
        carry = 0
        while i < len(numbera):
            print(numbera + ";" + numberb)
            math = int(nega + numbera[-(i + 1)]) + int(negb + numberb[-(i + 1)]) + int(carry)
            print(math)
            if math > 9:
                carry = str(math)[0]
                math = str(math)[1]
            else:
                carry = 0
            out = str(out) + str(math)
            i = i + 1
        if int(carry) > 0:
            out = out + str(carry)
        i = 0
        outn = ""
        while i < len(out):
            outn = outn + out[-(i + 1)]
            i = i + 1
        print(decimalloc)
        if outn[1] == '-':
            neg = -1
        else:
            neg = 1
        if neg < 0:
            outf = "-" + (outn[0:mather.floor(decimalloc / 2)] + '.' + outn[mather.floor(decimalloc / 2):len(outn)]).replace('-', '')
            locf = calc.findLargestDecimal(outf, outf)
            if locf != decimalloc:
                print('fuck')
                i = 0
                outl = outf
                while (locf != decimalloc) and (i < len(outl)):
                    try:
                        outf = "-" + (outn[-len(outn):-mather.floor(i / 2)] + '.' + outn[-mather.floor(i / 2):-1] + outn[-1]).replace('-', '')
                        locf = calc.findLargestDecimal(outf, outf)
                    except:
                        pass
                    i = i + 1
                i = 0
                while (locf != decimalloc) and (i < len(outl)):
                    try:
                        outf = "-" + (outn[0:mather.floor(i / 2)] + '.' + outn[mather.floor(i / 2):len(outn)]).replace('-', '')
                        locf = calc.findLargestDecimal(outf, outf)
                    except:
                        pass
                    i = i + 1
        else:
            outf = (outn[-len(outn):-mather.floor(decimalloc / 2)] + '.' + outn[-mather.floor(decimalloc / 2):-1] + outn[-1]).replace('-', '')
            locf = calc.findLargestDecimal(outf, outf)
            if locf != decimalloc:
                print('fuck')
                i = 0
                outl = outf
                while (locf != decimalloc) and (i < len(outl)):
                    try:
                        outf = (outn[0:mather.floor(i / 2)] + '.' + outn[mather.floor(i / 2):len(outn)]).replace('-', '')
                        locf = calc.findLargestDecimal(outf, outf)
                    except:
                        pass
                    i = i + 1
                i = 0
                while (locf != decimalloc) and (i < len(outl)):
                    try:
                        outf = (outn[-len(outn):-mather.floor(i / 2)] + '.' + outn[-mather.floor(i / 2):-1] + outn[-1]).replace('-', '')
                        locf = calc.findLargestDecimal(outf, outf)
                    except:
                        pass
                    i = i + 1
        return outf

    def addLargeInt(numbera: str, numberb: str):
        i = 0
        out = ""
        carry = 0
        while i < len(numbera):
            print(numbera + ";" + numberb)
            math = int(numbera[-(i + 1)]) + int(numberb[-(i + 1)]) + int(carry)
            print(math)
            if math > 9:
                carry = str(math)[0]
                math = str(math)[1]
            else:
                carry = 0
            out = str(out) + str(math)
            i = i + 1
        if int(carry) > 0:
            out = out + str(carry)
        i = 0
        outn = ""
        while i < len(out):
            outn = outn + out[-(i + 1)]
            i = i + 1
        return outn

    def findLargestDecimal(numbera, numberb):
        i = 0
        a = 0
        while i < len(numbera):
            if numbera[-(i + 1)] == '.':
                a = i
            i = i + 1
        i = 0
        b = 0
        while i < len(numberb):
            if numberb[-(i + 1)] == '.':
                b = i
            i = i + 1
        out = a + b
        print(';' + str(out))
        return out

    def multiplyLarge(numbera, numberb):
        i = 0
        outls = []
        if numbera.find(".") == -1:
            numbera = numbera + ".0"
        if numberb.find(".") == -1:
            numberb = numberb + ".0"
        decimalloc = calc.findLargestDecimal(numbera, numberb)
        numbera = numbera.replace('.', '')
        numberb = numberb.replace('.', '')
        while i < len(numberb):
            n = 0
            carry = 0
            outa = ""
            while n < len(numbera):
                math = (int(numbera[-(n + 1)]) * int(numberb[-(i + 1)])) + carry
                if 9 < math:
                    print(math)
                    carry = int(str(math)[0])
                    math = int(str(math)[1])
                else:
                    carry = 0
                outa = outa + str(math)
                n = n + 1
            outa = outa + str(carry)
            f = 0
            outb = ""
            while f < len(outa):
                outb = outb + outa[-(f + 1)]
                f = f + 1
            outls.append(outb)
            i = i + 1
        i = 0
        outn = "0"
        print(outls)
        zero = ""
        while i < len(outls):
            values = calc.equalizeDigits(outn, outls[i] + str(zero))
            outn = calc.addLargeInt(values[0], values[1]).split(".")[0]
            zero = zero + "0"
            print(values)
            i = i + 1
        exit = 0
        i = 0
        while exit == 0:
            if outn[i] != "0":
                sub = i
                exit = 1
            i = i + 1
        return outn[-len(outn):-(decimalloc)] + "." + outn[-(decimalloc):-1] + outn[-1] + "0"

    def equalizeDigits(numbera, numberb):
        if numbera.find('-') != -1:
            nega = '-'
        else:
            nega = ''
        if numberb.find('-') != -1:
            negb = '-'
        else:
            negb = ''
        numbera = numbera.replace('-', '')
        numberb = numberb.replace('-', '')
        if len(numbera.split(".")[0]) < len(numberb.split(".")[0]):
            i = len(numbera.split(".")[0])
            while i < len(numberb.split(".")[0]):
                numbera = "0" + numbera
                i = i + 1
        elif len(numberb.split(".")[0]) < len(numbera.split(".")[0]):
            i = len(numberb.split(".")[0])
            while i < len(numbera.split(".")[0]):
                numberb = "0" + numberb
                i = i + 1
        try:
            if len(numbera.split(".")[1]) < len(numberb.split(".")[1]):
                i = len(numbera.split(".")[1])
                while i < len(numberb.split(".")[1]):
                    numbera = numbera + "0"
                    i = i + 1
            elif len(numberb.split(".")[1]) < len(numbera.split(".")[1]):
                i = len(numberb.split(".")[1])
                while i < len(numbera.split(".")[1]):
                    numberb = numberb + "0"
                    i = i + 1
        except:
            pass
        return [nega + numbera, negb + numberb]
    
    def cleanNumber(number: str):
        i = 0
        while i < len(number):
            if number[i] != "0":
                start = i
                if number[i] == '.':
                    start = i - 1
                i = len(number)
            i = i + 1
        i = 0
        while i < len(number):
            if number[-(i + 1)] != "0":
                end = -(i)
                if number[i] == '.':
                    end = -i + 1
                i = len(number)
            i = i + 1
        print(str(start) + ";" + str(end))
        out = number[start:end]
        if start == 0:
            if end == 0:
                out = number
        return out + "0"

    def mathLargeFloat(numbera: str, arth: str, numberb: str):
        if arth == "+":
            if numbera.find('.') == -1:
                numbera = numbera + ".0"
            if numberb.find('.') == -1:
                numberb = numberb + ".0"
        values = calc.equalizeDigits(numbera, numberb)
        numberan = values[0]
        numberbn = values[1]
        if arth == "+":
            print(numberan + '#' + numberbn)
            outn = calc.addLarge(numberan, numberbn)
        if arth == "-":
            i = 0
            out = ""
            next = numbera[-(i + 1)]
            while i < len(numbera):
                if numbera[-(i + 1)] != next:
                    math = next - int(numberb[-(i + 1)])
                else:
                    math = int(numbera[-(i + 1)]) - int(numberb[-(i + 1)])
                if math < 0:
                    try:
                        next = int(numbera[-(i + 2)]) - 1
                    except:
                        next = 0 - 1
                    math = math + 10
                else:
                    try:
                        next = int(numbera[-(i + 2)])
                    except:
                        next = 0
                if math < 0:
                    math = 0
                out = str(out) + str(math)
                i = i + 1
        if arth == "*":
            outn = calc.multiplyLarge(numbera, numberb)
            # outn = ""
            # while i < len(out):
            #     outn = outn + out[-(i + 1)]
            #     i = i + 1
        print(outn)
        return calc.cleanNumber(outn)

    def abs(num):
        out = num
        if str(num)[0] == '-':
            out = str(num)[1:]
        return out

class net:
    def sendEmail(userEmail, password, toEmail, inputType, messageData, server, port):
        try:
            error = 0
            smtp_server = server
            sender_email = userEmail
            receiver_email = toEmail
            if inputType == 0:
                message = messageData
            elif inputType == 1:
                message = str(IO.getFile(messageData)).encode('ascii', 'ignore')
            else:
                error = 1
                print("Please enter a valid message format, formats are < -text | -file>")
            try:
                if error != 1:
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()  # Can be omitted
                        server.starttls(context=context)
                        server.ehlo()  # Can be omitted
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                    print("email sent")
                    error = 0
                else:
                    print("email failed to send.")
                    error = 1
            except Exception as err:
                print("email failed to send.")
                print("Email messaging error:", sys.exc_info())
                error = err
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            error = err
        return error

    def getJsonAPI(url):
        ssl._create_default_https_context = ssl._create_unverified_context
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        response = urlopen(req)
        data_json = json.loads(response.read())
        return data_json
    
    def getRawAPI(url):
        ssl._create_default_https_context = ssl._create_unverified_context
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        response = urlopen(req)
        data_json = response.read()
        return data_json

    def getTextAPI(url):
        ssl._create_default_https_context = ssl._create_unverified_context
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        response = urlopen(req)
        data_json = BeautifulSoup(response.read(), 'html.parser')
        text = data_json.find_all(text=True)
        data_out = cipher.listToString(text)
        return data_out

    def postAPI(url, node, data, encodeBool):
        ssl._create_default_https_context = ssl._create_unverified_context
        if int(encodeBool) != 0:
            encodedData = cipher.base64_encode(data)
        else:
            encodedData = data
        url = url + "?" + node + "=" + encodedData
        print(url)
        response = urlopen(url)
        data_json = response.read()
        return data_json

class cipher:  
    def base64_encode(s):
        error = 0
        try:
            temp = str(os.environ['temp'])
            file = open(temp + "\\out_ser.cxl", "w")
            file.write(s)
            file.close()
            try:
                subprocess.check_output("certutil -f -encode \"" + temp + "\\out_ser.cxl\" \"" + temp + "\\dump_ser.base64\"", shell=True)
                file = open(temp + "\\dump_ser.base64", "r")
                encode = str(file.read())
                file.close()
                encode = encode.replace("=", "$")
                encode = encode.replace("+", "?")
                encode = encode.replace("/", "!")
                encode = (encode.split("-----BEGIN CERTIFICATE-----")[1]).split("-----END CERTIFICATE-----")[0].replace("\n", "")
            except:
                encode = "ZWNobyBmdWNrIA0K"
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            encode = error
        return encode
        
    def base64_decode(s):
        error = 0
        try:
            temp = str(os.environ['temp'])
            encode = s.replace("$", "=")
            encode = encode.replace("?", "+")
            encode = encode.replace("!", "/")
            encode = encode.replace("\n", "")
            encode = encode.replace(" ", "")
            encode = encode.replace("\"", "")
            file = open(temp + "\\out_ser.cxl", "w")
            file.write(encode)
            file.close()
            try:
                subprocess.check_output("certutil -f -decode \"" + temp + "\\out_ser.cxl\" \"" + temp + "\\dump_ser.base64\"", shell=True)
                file = open(temp + "\\dump_ser.base64", "r")
                decode = str(file.read())
                file.close()
            except:
                decode = "Operation was sucsessful."
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            decode = error
        return decode

    def listToString(s):
        str1 = " "
        return (str1.join(s))

class imageWorker:
    def getRGB(path):
        image_url = path
        resp = requests.get(image_url)
        assert resp.ok
        img = Image.open(BytesIO(resp.content)).convert('RGB')
        img2 = img.resize((1, 1))
        color = img2.getpixel((0, 0))
        colorrgb = ImageColor.getcolor('#{:02x}{:02x}{:02x}'.format(*color), "RGB")
        # print('#{:02x}{:02x}{:02x}'.format(*color))
        return colorrgb

class clock:
    def getDateTime():
        daten = datetime.now()
        dateArray = [1970, 1, 1, 0, 0, 0]
        dateArray[0] = int(str(daten).split(" ")[0].split("-")[0])
        dateArray[1] = int(str(daten).split(" ")[0].split("-")[1])
        dateArray[2] = int(str(daten).split(" ")[0].split("-")[2])
        dateArray[3] = int(str(daten).split(" ")[1].split(":")[0])
        dateArray[4] = int(str(daten).split(" ")[1].split(":")[1])
        dateArray[5] = int(str(daten).split(" ")[1].split(":")[2].split(".")[0])
        return dateArray
    
def dummy(*args):
    if args[0] == args[0]:
        pass
    return 0
    
def runFile(path):
    code = IO.getFile(path)
    out = exec(code)
    return out
    
def help():
    print("there are 10 options: ")
    print("-------------------- ")
    print("pyexec -executescript \"<escaped commands>\"                ///   Executes python commands")
    print("pyexec -getfile \"<path>\"                                  ///   Returns text within a file.")
    print("pyexec -getjson \"<path>\"                                  ///   Returns json formatted text within a file")
    print("pyexec -savefile \"<path>\" \"<data>\"                        ///   Saves text into file")
    print("pyexec -savejson \"<path>\" \"<data>\"                        ///   Saves json formatted text into file")
    print("pyexec -getcpu <wait time (double) {seconds}>             ///   Returns average cpu usage within the time limit given")
    print("pyexec -encodebase64 \"<data>\"                             ///   Returns encryped base64 data")
    print("pyexec -getrgbavg \"<image url>\"                           ///   Returns average RGB value of the specified image url")
    print("pyexec -getapi \"<url>\"                                    ///   Returns json data of api call")
    print("pyexec -postapi \"<url>\"                                    ///   Posts data to the specified url page")
    print("pyexec -decodebase64 \"<data>\"                             ///   Returns decryped base64 data")
    print("pyexec -linedcsvtojson \"<path>\"                           ///   Converts linedCSV data to json")
    print("pyexec -getwallpaper                                      ///   Returns wallpaper location path")
    print("pyexec -setwallpaper \"<path>\"                             ///   Sets wallpaper based on location path")
    print("pyexec -temptoword \"<temp (double) {kelvin}>\"             ///   Converts temperature value (kelvin) to a word")
    print("pyexec \"<path>\"                                           ///   Execute python file (.py) as is")
    print("pyexec -help                                              ///   Shows this menu\n")
    
    print("pyexec -saturatergb <red (int) {0 - 255}>                 ///   Saturates given rgb values")
    print("    <green (int) {0 - 255}> <blue (int) {0 - 255}>\n")
    print("pyexec -sendemail \"<user email>\" \"<user password>\"        ///   Sends emails based on the input perameters")
    print("    \"<to email>\" < -text | -file> \"<message / file>\"")
    print("        optional peramiters: \"<smtp server>\" \"<port>\"\n")
    return 0