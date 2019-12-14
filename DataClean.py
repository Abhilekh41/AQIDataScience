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
import json
import csv
def main():
    
    x_file = open("Data/Html_Data/2016/1.html","r")
    page_soup = soup(x_file,"html.parser")
    data = []
    header = []
    contentMap = {"nthi":".",
                  "ntjk":"1",
                  "ntrs":"2",
                  "ntza":"3",
                  "ntaa":"4",
                  "ntbz":"5",
                  "ntgy":"6",
                  "ntox":"7",
                  "ntqr":"8",
                  "ntnt":"9",
                  "ntbc":"0",
                  "ntvr":".",
                  "ntzz":"-"}
    
    table = page_soup.find("table",attrs={'class':'medias mensuales numspan'})
    i = 0
    for hr in table.findAll('th'):
        header.append(hr.text)
    header.pop()
    for row in table.findAll('tr'):
        cells = row.findAll('td')
        new_data = []
        for cell in cells:
            if(cell.text == "" or cell.text == None):
                spans = cell.findAll('span')
                contents = ""
                for value in spans:
                    for content in contentMap:
                        if(value.get('class')[0]==content):
                            if(value.get('class')[0] != None):
                                contents+=contentMap.get(value.get('class')[0])
                new_data.append(contents)
            else:
                new_data.append(cell.text)
        data.append(new_data)
    sys.stdout.flush()
    df = pd.DataFrame(data,columns = header)
    print(df)
    if not os.path.exists("Data/Excel/2016/"):
        os.makedirs("Data/Excel/2016/")
    with open('1.csv','w',newline='') as file:
        writer = csv.writer(file)
    df.to_csv(r'Data/Excel/2016/1.csv')
       
        
    

if __name__ == '__main__':
    main()