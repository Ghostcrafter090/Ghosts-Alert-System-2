import pytools

# Alert Ranges:
#
# L0: 0-6 m/s
# L1: 6-12 m/s
# L2: 12-18 m/s
# L3: 18-24 m/s
# L4: 24-30 m/s
# L5: 30-42 m/s
# L6: 42-54 m/s
# L7: 54-66 m/s
# L8: 66-78 m/s
# L9: 78-90 m/s

# LEVEL,  level number for alert
# CLASS,  storm class
# LEVELB, highest level in storm class

class strings:
    class l0:
        subject = 'Subject: Wind Warning Ended (Downgraded to L!LEVEL!)'
        body = 'Warning: The Storm Has Downgraded Itself To !CLASS!. This Storm Is Located In Nova Scotia With A High Catagory Of L1.\n\nenjoy The Clear Weather!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l1v3:
        subject = 'Subject: L!LEVEL! Wind Warning'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of L!LEVELB!.\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l4v9:
        subject = '!!!L!LEVEL! Hurricane Wind Warning!!!'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of H-Catagory L!LEVELB!.\n\nIt Is HIGHLY Reccomended That You (If Your Outside) That You Get Indoors Quickly And Stay Indoors!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_watch_email>"

def returnAlertLevel(windGust, windSpeed):
    gustLevel = 0
    speedLevel = 0
    if (0 <= windGust) and (windGust < 6):
        gustLevel = 0
    if (6 <= windGust) and (windGust < 12):
        gustLevel = 1
    if (12 <= windGust) and (windGust < 18):
        gustLevel = 2
    if (18 <= windGust) and (windGust < 24):
        gustLevel = 3
    if (24 <= windGust) and (windGust < 30):
        gustLevel = 4
    if (30 <= windGust) and (windGust < 42):
        gustLevel = 5
    if (42 <= windGust) and (windGust < 54):
        gustLevel = 6
    if (54 <= windGust) and (windGust < 66):
        gustLevel = 7
    if (66 <= windGust) and (windGust < 78):
        gustLevel = 8
    if (78 <= windGust):
        gustLevel = 9
    if (0 <= windSpeed) and (windSpeed < 6):
        speedLevel = 0
    if (6 <= windSpeed) and (windSpeed < 12):
        speedLevel = 1
    if (12 <= windSpeed) and (windSpeed < 18):
        speedLevel = 2
    if (18 <= windSpeed) and (windSpeed < 24):
        speedLevel = 3
    if (24 <= windSpeed) and (windSpeed < 30):
        speedLevel = 4
    if (30 <= windSpeed) and (windSpeed < 42):
        speedLevel = 5
    if (42 <= windSpeed) and (windSpeed < 54):
        speedLevel = 6
    if (54 <= windSpeed) and (windSpeed < 66):
        speedLevel = 7
    if (66 <= windSpeed) and (windSpeed < 78):
        speedLevel = 8
    if (78 <= windSpeed):
        speedLevel = 9
    return gustLevel + speedLevel