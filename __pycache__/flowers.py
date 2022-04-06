import pytools
from bs4 import BeautifulSoup

def getFlowers():
    links = pytools.IO.getFile('flowers.txt')
    i = 0
    flowerlist = pytools.IO.getFile('flowers_act.txt')
    while i < len(links.split('\n')):
        try:
            if flowerlist.find(links.split('\n')[i].split('. ')[1].split('/')[3]) == -1:
                soup = BeautifulSoup(pytools.net.getRawAPI(links.split('\n')[i].split('. ')[1]), 'html.parser')
                flowerlinks = soup.find_all(class_='product-image')
                n = 0
                while n < len(str(flowerlinks).split('\n')):
                    try:
                        if flowerlist.find('\nhttps://www.halifaxseed.ca' + str(flowerlinks).split('\n')[n].split('href=')[1].split('"')[1]) == -1:
                            print('https://www.halifaxseed.ca' + str(flowerlinks).split('\n')[n].split('href=')[1].split('"')[1])
                            flowerlist = flowerlist + '\nhttps://www.halifaxseed.ca' + str(flowerlinks).split('\n')[n].split('href=')[1].split('"')[1]
                    except:
                        pass
                    n = n + 1
        except:
            print('Error. Skipping flower...')
        i = i + 1
        print(i)
    return flowerlist