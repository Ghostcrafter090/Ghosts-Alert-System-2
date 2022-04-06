import pytools

# Alert Ranges:
#
# L9: 0-600 m
# L8: 600-1200 m
# L7: 1200-1800 m
# L6: 1800-2400 m
# L5: 2400-3000 m
# L4: 3000-3600 m
# L3: 3600-4200 m
# L2: 4200-4800 m
# L1: 4800-5400 m
# L0: 5400+ m

# LEVEL,  level number for alert
# CLASS,  storm class
# LEVELB, highest level in storm class

class strings:
    class l0:
        subject = 'Subject: Visibility Warning Ended (Downgraded to L!LEVEL!)'
        body = 'Warning: The Storm Has Downgraded Itself To !CLASS!. This Storm Is Located In Nova Scotia With A High Catagory Of L1.\n\nenjoy The Clear Weather!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l1v3:
        subject = 'Subject: L!LEVEL! Low Visibility Warning'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of L!LEVELB!.\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l4v9:
        subject = '!!!L!LEVEL! Extreme Low Visibility Warning!!!'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of H-Catagory L!LEVELB!.\n\nIt Is HIGHLY Reccomended That You (If Your Outside) That You Get Indoors Quickly And Stay Indoors!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_watch_email>"

def returnAlertLevel(rainRate):
    rateLevel = 0
    if (0 <= rainRate) and (rainRate < 600):
        rateLevel = 9
    if (600 <= rainRate) and (rainRate < 1200):
        rateLevel = 8
    if (1200 <= rainRate) and (rainRate < 1800):
        rateLevel = 7
    if (1800 <= rainRate) and (rainRate < 2400):
        rateLevel = 6
    if (2400 <= rainRate) and (rainRate < 3000):
        rateLevel = 5
    if (3000 <= rainRate) and (rainRate < 3600):
        rateLevel = 4
    if (3600 <= rainRate) and (rainRate < 4200):
        rateLevel = 3
    if (4200 <= rainRate) and (rainRate < 4800):
        rateLevel = 2
    if (4800 <= rainRate) and (rainRate < 5400):
        rateLevel = 1
    if (5400 <= rainRate):
        rateLevel = 0
    return rateLevel