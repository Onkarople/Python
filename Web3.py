import os
import bs4
import requests
from sys import*

def MarvellousLinksDsiplay(URL):
    res=requests.get(URL)
    print(type(res))


    soup=bs4.BeautifulSoup(res.text,'lxml')
    print(type(soup))
    links=soup.find_all('a',href=True)

    return links


def main():
    print("Application Name:",argv[0])

    if len(argv)==2:
        if(argv[1]=='-h') or (argv[1]=='-H'):
            print("Used to fetch links from wikipedia file")
            exit()
        
        if(argv[1]=='-u') or (argv[1]=='-U'):
            print("Useges:Application Name")
            exit()
    
    url='https://en.wikipedia.org/wiki/Python_(programming_language)'

    arr=MarvellousLinksDsiplay(url)

    print("Links are")

    for element in arr:
        if "#" not in element['href']:
            print(element['href'])


if __name__ == "__main__":
    main()
