import pytools

# Alert Ranges:
#
# L0: 1000 hpa
# L1: 995 hpa
# L2: 990 hpa
# L3: 985 hpa
# L4: 980 hpa
# L5: 975 hpa
# L6: 970 hpa
# L7: 965 hpa
# L8: 960 hpa
# L9: 955 hpa

# LEVEL,  level number for alert
# CLASS,  storm class
# LEVELB, highest level in storm class

class strings:
    class l0:
        subject = 'Subject: Pressure Warning Ended (Downgraded to L!LEVEL!)'
        body = 'Warning: The Storm Has Downgraded Itself To !CLASS!. This Storm Is Located In Nova Scotia With A High Catagory Of L1.\n\nenjoy The Clear Weather!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l1v3:
        subject = 'Subject: L!LEVEL! Pressure Warning'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of L!LEVELB!.\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_warning_email>"
    class l4v9:
        subject = '!!!L!LEVEL! Hurricane Pressure Warning!!!'
        body = 'Warning: There Is Currently A !CLASS! Catagory Storm Located In Nova Scotia With A High Catagory Of H-Catagory L!LEVELB!.\n\nIt Is HIGHLY Reccomended That You (If Your Outside) That You Get Indoors Quickly And Stay Indoors!\n\nPlease continue to monitor alerts sent by Schwarzwald Station Fall River NS.\n\nLightning Detection System --- circa February 2019 --- By Ghostcrafter090, Developer of sleep rays, creator of GhostCraft'
        email = "<alert_watch_email>"

def returnAlertLevel(presRate):
    rateLevel = 0
    if (1000 <= presRate):
        rateLevel = 0
    if (995 <= presRate) and (presRate < 1000):
        rateLevel = 1
    if (990 <= presRate) and (presRate < 995):
        rateLevel = 2
    if (985 <= presRate) and (presRate < 990):
        rateLevel = 3
    if (980 <= presRate) and (presRate < 985):
        rateLevel = 4
    if (975 <= presRate) and (presRate < 980):
        rateLevel = 5
    if (970 <= presRate) and (presRate < 975):
        rateLevel = 6
    if (965 <= presRate) and (presRate < 970):
        rateLevel = 7
    if (960 <= presRate) and (presRate < 965):
        rateLevel = 8
    if (960 > presRate):
        rateLevel = 9
    return rateLevel