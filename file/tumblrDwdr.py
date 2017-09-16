# coding: utf-8
#Simple tumblr image downloader by Logan Tann
#Under the MIT/X11 license.Read the readme file if you want to discover it !
#it is not recommended to copy paste this code (ahah python indent error lol).In github web interface,click on the RAW button and ctrl+s !

import os
try:
    from bs4 import BeautifulSoup
except ImportError as e:
    print("""Unable to load BeatifulSoup Librairy !\nTry to install it manually,or using pip !!""")
    input("press a key to continue")
    raise ImportError("""Unable to load BeatifulSoup Librairy !\nTry to install it manually,or using pip.
    error : {}""".format(e))
try:
    import urllib.request
except ImportError as e:
    print("""Unable to load urllib !! Are you using python 3 ?""")
    input("press a key to continue")
    raise ImportError("""Unable to load urllib !! Are you using python 3 ?
    error : {}""".format(e))


def download(url,name):
    urllib.request.urlretrieve(url, name)
    return True

def isPageOK(url):
    try:
        test = urllib.request.urlopen(url)
    except urllib.request.HTTPError as e:
        return False
    else:
        return True
    
def job(url):
    jobList = []
    html = urllib.request.urlopen(url).read()
    allFigures = BeautifulSoup(html,"html.parser").find_all('figure')
    
    for figure in allFigures:
        allImg = BeautifulSoup(str(figure),"html.parser").find_all('img')
        for img in allImg:
            jobList.append(img['src'])
    
    return jobList

def main():
    #main loop
    quit = False
    while not quit:
        
        #Set download directory
        path = input('Enter a folder to download : ')
        if not os.path.isdir(path):
            os.mkdir(path)
        os.chdir(path)

        #set tumblr url and download
        inputUrl = input("Enter the tumblr url : ")
        if isPageOK(inputUrl):
            print("Page is OK. Reading  : " + inputUrl)
            jobList = job(inputUrl)
            compteur = 1
            for url in jobList:
                extension = "." + url.split('.')[-1]
                print("Downloading : ",url," to ",compteur,extension)
                download(url,str(compteur) + extension)
                compteur += 1
        else:
            print("An error occured ! Did the url is valid or correct ?")
            
        os.chdir('..')
        
        choix = input("Do you want to download another page ? [y/n]:")
        if choix != "y":
            quit = True
    
    
if __name__ == '__main__':
    main()
    print('Program finished.')
    input('Press a key to exit')
