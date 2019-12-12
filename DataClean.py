#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:39:39 2019

@author: abhilekhsahay
"""

import os
import time
import requests
import sys
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import pandas as pd
def main():
    
    x_file = open("Data/Html_Data/2016/1.html","r")
    page_soup = soup(x_file,"html.parser")
    data = []
    header = []
    table = page_soup.find("table",attrs={'class':'medias mensuales numspan'})
    i = 0
    for hr in table.findAll('th'):
        header.append(hr.text)
    header.pop()
    print(len(header))
    for row in table.findAll('tr'):
        cells = row.findAll('td')
        new_data = []
        for cell in cells:
            new_data.append(cell.text)
        print(len(new_data))
        data.append(new_data)
    print(header)
    #print(data)
    sys.stdout.flush()
    df = pd.DataFrame(data,columns = header)
    print(df)

if __name__ == '__main__':
    main()