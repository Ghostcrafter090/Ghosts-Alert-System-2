import pytools

# Alert Ranges:
#
# L0: 5+ 5-
# L1: 10+ 10-
# L2: 15+ 15-
# L3: 20+ 20-
# L4: 25+ 25-
# L5: 30+ 30-
# L6: 35+ 35-
# L7: 40+ 40-
# L8: 45+ 45-
# L9: 50+ 50-

# LEVEL,  level number for alert
# CLASS,  storm class
# LEVELB, highest level in storm class

class strings:
    class l0:
        subject = 'Subject: Temp Warning Ended (Downgraded to L!LEVEL!)'
        body = 'Warning: The Storm Has Downgraded Itself To !CLASS!. This Storm Is Located In Nova Scotia With A High Catagory Of L1.\n\nenjoy The Clear Weather!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l1v3:
        subject = 'Subject: L!LEVEL! Temp Warning'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of L!LEVELB!.\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l4v9:
        subject = '!!!L!LEVEL! Extreme Temp Warning!!!'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of H-Catagory L!LEVELB!.\n\nIt Is HIGHLY Reccomended That You (If Your Outside) That You Get Indoors Quickly And Stay Indoors!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_watch_email>"

def returnAlertLevel(tempRaten):
    tempRate = float(pytools.calc.abs(tempRaten - 15))
    rateLevel = 0
    if (0 <= tempRate) and (tempRate < 5):
        rateLevel = 0
    if (5 <= tempRate) and (tempRate < 10):
        rateLevel = 1
    if (10 <= tempRate) and (tempRate < 15):
        rateLevel = 2
    if (15 <= tempRate) and (tempRate < 20):
        rateLevel = 3
    if (20 <= tempRate) and (tempRate < 25):
        rateLevel = 4
    if (25 <= tempRate) and (tempRate < 30):
        rateLevel = 5
    if (30 <= tempRate) and (tempRate < 35):
        rateLevel = 6
    if (35 <= tempRate) and (tempRate < 40):
        rateLevel = 7
    if (40 <= tempRate) and (tempRate < 45):
        rateLevel = 8
    if (45 <= tempRate):
        rateLevel = 9
    return rateLevel