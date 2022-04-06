import pytools
from wind import strings as windstrings
from rain import strings as rainstrings
from snow import strings as snowstrings
from pres import strings as presstrings
from temp import strings as tempstrings
from visi import strings as visistrings

# Class: lw[0 - 9]lr[0 - 4]ls[0 - 4]lp[0 - 4]lt[0 - 4]

# This file contains running code for the alert deployment process. when using, replace the <password> field with the global password 
# for your different email accounts for the service. Than, go into each alert type file (eg: wind.py) and replace the email fields 
# <eg: "<alert_watch_email>"> with the corrisponding email account setup on the smtp server.

class wind:
    def L0(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(windstrings.l0.email, '<password>', toEmail, 0, (windstrings.l0.subject + '\n\n' + windstrings.l0.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def L1v3(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(windstrings.l1v3.email, '<password>', toEmail, 0, (windstrings.l1v3.subject + '\n\n' + windstrings.l1v3.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)
    
    def L4v9(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(windstrings.l4v9.email, '<password>', toEmail, 0, (windstrings.l4v9.subject + '\n\n' + windstrings.l4v9.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel):
        lClass = 'lw' + str(windLevel) + 'lr' + str(rainLevel) + 'ls' + str(snowLevel) + 'lp' + str(presLevel) + 'lt' + str(tempLevel) + 'lv' + str(visiLevel)
        if windLevel < 1:
            wind.L0('9022193848@txt.bell.ca', lClass, windLevel)
        if (1 <= windLevel) and (windLevel < 4):
            wind.L1v3('9022193848@txt.bell.ca', lClass, windLevel)
        if 4 <= windLevel:
            wind.L4v9('9022193848@txt.bell.ca', lClass, windLevel)

class rain:
    def L0(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(rainstrings.l0.email, '<password>', toEmail, 0, (rainstrings.l0.subject + '\n\n' + rainstrings.l0.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def L1v3(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(rainstrings.l1v3.email, '<password>', toEmail, 0, (rainstrings.l1v3.subject + '\n\n' + rainstrings.l1v3.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)
    
    def L4v9(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(rainstrings.l4v9.email, '<password>', toEmail, 0, (rainstrings.l4v9.subject + '\n\n' + rainstrings.l4v9.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel):
        lClass = 'lw' + str(windLevel) + 'lr' + str(rainLevel) + 'ls' + str(snowLevel) + 'lp' + str(presLevel) + 'lt' + str(tempLevel) + 'lv' + str(visiLevel)
        if rainLevel < 1:
            rain.L0('9022193848@txt.bell.ca', lClass, rainLevel)
        if (1 <= rainLevel) and (rainLevel < 4):
            rain.L1v3('9022193848@txt.bell.ca', lClass, rainLevel)
        if 4 <= rainLevel:
            rain.L4v9('9022193848@txt.bell.ca', lClass, rainLevel)

class snow:
    def L0(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(snowstrings.l0.email, '<password>', toEmail, 0, (snowstrings.l0.subject + '\n\n' + snowstrings.l0.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def L1v3(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(snowstrings.l1v3.email, '<password>', toEmail, 0, (snowstrings.l1v3.subject + '\n\n' + snowstrings.l1v3.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)
    
    def L4v9(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(snowstrings.l4v9.email, '<password>', toEmail, 0, (snowstrings.l4v9.subject + '\n\n' + snowstrings.l4v9.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel):
        lClass = 'lw' + str(windLevel) + 'lr' + str(rainLevel) + 'ls' + str(snowLevel) + 'lp' + str(presLevel) + 'lt' + str(tempLevel) + 'lv' + str(visiLevel)
        if snowLevel < 1:
            snow.L0('9022193848@txt.bell.ca', lClass, snowLevel)
        if (1 <= snowLevel) and (snowLevel < 4):
            snow.L1v3('9022193848@txt.bell.ca', lClass, snowLevel)
        if 4 <= snowLevel:
            snow.L4v9('9022193848@txt.bell.ca', lClass, snowLevel)

class pres:
    def L0(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(presstrings.l0.email, '<password>', toEmail, 0, (presstrings.l0.subject + '\n\n' + presstrings.l0.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def L1v3(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(presstrings.l1v3.email, '<password>', toEmail, 0, (presstrings.l1v3.subject + '\n\n' + presstrings.l1v3.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)
    
    def L4v9(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(presstrings.l4v9.email, '<password>', toEmail, 0, (presstrings.l4v9.subject + '\n\n' + presstrings.l4v9.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel):
        lClass = 'lw' + str(windLevel) + 'lr' + str(rainLevel) + 'ls' + str(snowLevel) + 'lp' + str(presLevel) + 'lt' + str(tempLevel) + 'lv' + str(visiLevel)
        if presLevel < 1:
            pres.L0('9022193848@txt.bell.ca', lClass, presLevel)
        if (1 <= presLevel) and (presLevel < 4):
            pres.L1v3('9022193848@txt.bell.ca', lClass, presLevel)
        if 4 <= presLevel:
            pres.L4v9('9022193848@txt.bell.ca', lClass, presLevel)

class temp:
    def L0(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(tempstrings.l0.email, '<password>', toEmail, 0, (tempstrings.l0.subject + '\n\n' + tempstrings.l0.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def L1v3(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(tempstrings.l1v3.email, '<password>', toEmail, 0, (tempstrings.l1v3.subject + '\n\n' + tempstrings.l1v3.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)
    
    def L4v9(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(tempstrings.l4v9.email, '<password>', toEmail, 0, (tempstrings.l4v9.subject + '\n\n' + tempstrings.l4v9.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel):
        lClass = 'lw' + str(windLevel) + 'lr' + str(rainLevel) + 'ls' + str(snowLevel) + 'lp' + str(presLevel) + 'lt' + str(tempLevel) + 'lv' + str(visiLevel)
        if tempLevel < 1:
            temp.L0('9022193848@txt.bell.ca', lClass, tempLevel)
        if (1 <= tempLevel) and (tempLevel < 4):
            temp.L1v3('9022193848@txt.bell.ca', lClass, tempLevel)
        if 4 <= tempLevel:
            temp.L4v9('9022193848@txt.bell.ca', lClass, tempLevel)
    
class visi:
    def L0(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(visistrings.l0.email, '<password>', toEmail, 0, (visistrings.l0.subject + '\n\n' + visistrings.l0.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def L1v3(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(visistrings.l1v3.email, '<password>', toEmail, 0, (visistrings.l1v3.subject + '\n\n' + visistrings.l1v3.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)
    
    def L4v9(toEmail, lClass, level):
        i = 0
        max = 0
        while i < len(lClass.split('l')):
            try:
                n = 1
                print(str(lClass.split('l')[i]))
                if int(str(lClass.split('l')[i])[1]) == '-':
                    n = 2
                if max < int(str(lClass.split('l')[i])[n]):
                    max = int(str(lClass.split('l')[i])[n])
            except:
                pass
            i = i + 1
        result = pytools.net.sendEmail(visistrings.l4v9.email, '<password>', toEmail, 0, (visistrings.l4v9.subject + '\n\n' + visistrings.l4v9.body).replace('!LEVEL!', str(level)).replace('!CLASS!', str(lClass)).replace('!LEVELB!', str(max)), 'smtp.gmail.com', '587')
        if result != 0:
            print(result)

    def deploy(windLevel, rainLevel, snowLevel, presLevel, tempLevel, visiLevel):
        lClass = 'lw' + str(windLevel) + 'lr' + str(rainLevel) + 'ls' + str(snowLevel) + 'lp' + str(presLevel) + 'lt' + str(tempLevel) + 'lv' + str(visiLevel)
        if visiLevel < 1:
            visi.L0('9022193848@txt.bell.ca', lClass, visiLevel)
        if (1 <= visiLevel) and (visiLevel < 4):
            visi.L1v3('9022193848@txt.bell.ca', lClass, visiLevel)
        if 4 <= visiLevel:
            visi.L4v9('9022193848@txt.bell.ca', lClass, visiLevel)