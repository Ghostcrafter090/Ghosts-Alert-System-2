import pytools

# Alert Ranges:
#
# L0: 0-4 mm
# L1: 4-8 mm
# L2: 8-12 mm
# L3: 12-16 mm
# L4: 16-20 mm
# L5: 20-24 mm
# L6: 24-28 mm
# L7: 28-32 mm
# L8: 32-36 mm
# L9: 36-40 mm

# LEVEL,  level number for alert
# CLASS,  storm class
# LEVELB, highest level in storm class

class strings:
    class l0:
        subject = 'Subject: Rain Warning Ended (Downgraded to L!LEVEL!)'
        body = 'Warning: The Storm Has Downgraded Itself To !CLASS!. This Storm Is Located In Nova Scotia With A High Catagory Of L1.\n\nenjoy The Clear Weather!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l1v3:
        subject = 'Subject: L!LEVEL! Rain Warning'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of L!LEVELB!.\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l4v9:
        subject = '!!!L!LEVEL! Hurricane Rain Warning!!!'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of H-Catagory L!LEVELB!.\n\nIt Is HIGHLY Reccomended That You (If Your Outside) That You Get Indoors Quickly And Stay Indoors!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_watch_email>"

def returnAlertLevel(rainRate):
    rateLevel = 0
    if (0 <= rainRate) and (rainRate < 4):
        rateLevel = 0
    if (4 <= rainRate) and (rainRate < 8):
        rateLevel = 1
    if (8 <= rainRate) and (rainRate < 12):
        rateLevel = 2
    if (12 <= rainRate) and (rainRate < 16):
        rateLevel = 3
    if (16 <= rainRate) and (rainRate < 20):
        rateLevel = 4
    if (20 <= rainRate) and (rainRate < 24):
        rateLevel = 5
    if (24 <= rainRate) and (rainRate < 28):
        rateLevel = 6
    if (28 <= rainRate) and (rainRate < 32):
        rateLevel = 7
    if (32 <= rainRate) and (rainRate < 36):
        rateLevel = 8
    if (36 <= rainRate):
        rateLevel = 9
    return rateLevel