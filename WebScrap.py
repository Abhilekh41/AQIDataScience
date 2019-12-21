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
    citiesAndCode  =  {"421820":"Delhi",
         "428090":"Kolkata",
         "432790":"Chennai",
         "424920":"Patna",
         "432950":"Bangalore",
         "431280":"Hyderabad",
         "433710":"Thiruvananthapuram",
         "423480":"Jaipur"}
    for codes in citiesAndCode:
        for year in range(2000,2019):
            for month in range(1,13):
                if(month<10):
                    url = "https://en.tutiempo.net/climate/0{}-{}/ws-{}.html".format(month,year,codes)
                else:
                    url = "https://en.tutiempo.net/climate/{}-{}/ws-{}.html".format(month,year,codes)
            
                uClient = ureq(url)
                page_html=uClient.read()
                uClient.close()
                page_soup = soup(page_html,"html.parser")
                
                texts = requests.get(url)
                text_utf = texts.text.encode("utf=8")
              
                if not os.path.exists("{}/Html_Data/{}".format(citiesAndCode.get(codes),year)):
                    os.makedirs("{}/Html_Data/{}".format(citiesAndCode.get(codes),year))
                with open("{}/Html_Data/{}/{}.html".format(citiesAndCode.get(codes),year,month),"wb") as output:
                    output.write(text_utf)
                sys.stdout.flush()


if __name__ == '__main__':
    main()