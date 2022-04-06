import pytools

# Alert Ranges:
#
# L0: 0-4 cm
# L1: 4-8 cm
# L2: 8-12 cm
# L3: 12-16 cm
# L4: 16-20 cm
# L5: 20-24 cm
# L6: 24-28 cm
# L7: 28-32 cm
# L8: 32-36 cm
# L9: 36-40 cm

# LEVEL,  level number for alert
# CLASS,  storm class
# LEVELB, highest level in storm class

class strings:
    class l0:
        subject = 'Subject: Snow Warning Ended (Downgraded to L!LEVEL!)'
        body = 'Warning: The Storm Has Downgraded Itself To !CLASS!. This Storm Is Located In Nova Scotia With A High Catagory Of L1.\n\nenjoy The Clear Weather!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l1v3:
        subject = 'Subject: L!LEVEL! Snow Warning'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of L!LEVELB!.\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l4v9:
        subject = '!!!L!LEVEL! Hurricane Snow Warning!!!'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of H-Catagory L!LEVELB!.\n\nIt Is HIGHLY Reccomended That You (If Your Outside) That You Get Indoors Quickly And Stay Indoors!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_watch_email>"

def returnAlertLevel(snowRate):
    rateLevel = 0
    if (0 <= snowRate) and (snowRate < 4):
        rateLevel = 0
    if (4 <= snowRate) and (snowRate < 8):
        rateLevel = 1
    if (8 <= snowRate) and (snowRate < 12):
        rateLevel = 2
    if (12 <= snowRate) and (snowRate < 16):
        rateLevel = 3
    if (16 <= snowRate) and (snowRate < 20):
        rateLevel = 4
    if (20 <= snowRate) and (snowRate < 24):
        rateLevel = 5
    if (24 <= snowRate) and (snowRate < 28):
        rateLevel = 6
    if (28 <= snowRate) and (snowRate < 32):
        rateLevel = 7
    if (32 <= snowRate) and (snowRate < 36):
        rateLevel = 8
    if (36 <= snowRate):
        rateLevel = 9
    return rateLevel