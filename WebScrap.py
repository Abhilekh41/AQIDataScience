# -*- coding: utf-8 -*-
"""
Spyder Editor

Author : bajasahay
"""


import os
import time
import requests
import sys
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

def main():
    for year in range(2000,2019):
        for month in range(1,13):
            if(month<10):
                url = "https://en.tutiempo.net/climate/0{}-{}/ws-432950.html".format(month,year)
            else:
                url = "https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month,year)
            
            uClient = ureq(url)
            page_html=uClient.read()
            uClient.close()
            page_soup = soup(page_html,"html.parser")
            
            texts = requests.get(url)
            text_utf = texts.text.encode("utf=8")
    
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                    output.write(text_utf)
            sys.stdout.flush()


if __name__ == '__main__':
    main()