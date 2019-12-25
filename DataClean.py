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
from openpyxl import load_workbook
def main():
    citiesAndCode  =  {"421820":"Delhi",
         "428090":"Kolkata",
         "432790":"Chennai",
         "424920":"Patna",
         "432950":"Bangalore",
         "431280":"Hyderabad",
         "433710":"Thiruvananthapuram",
         "423480":"Jaipur"}
    
    monthNames = {1:"January",
             2:"Febuary",
             3:"March",
             4:"April",
             5:"May",
             6:"June",
             7:"July",
             8:"August",
             9:"September",
             10:"October",
             11:"November",
             12:"December"}
    
    for codes in citiesAndCode:
        for year in range(2000,2019):
            excel_file_location = "{}/Excel".format(citiesAndCode.get(codes))
            if not os.path.exists(excel_file_location):
                os.makedirs(excel_file_location) 
            file_to_be_written = excel_file_location+"/{}.xlsx".format(year)
            for month in range(1,13):
                html_file_location= "{}/Html_Data/{}/{}.html".format(citiesAndCode.get(codes),year,month)
                x_file = open(html_file_location,"r")
                page_soup = soup(x_file,"html.parser")
                data = []
                header = []
                contentMapList = [{
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
                           "ntzz":"-"
                          },
                          { "ntvw":"2",
                             "ntfg":"0",
                             "ntkk":".",
                             "ntpo":"7",
                             "ntdr":"6",
                             "ntno":"1",
                             "ntgo":"5",
                             "ntht":"8",
                             "ntjj":"-",
                             "ntef":"3",
                             "ntjg":"9",
                             "ntee":"4"
                             },
                          {"ntpq":"2",
                             "ntab":"0",
                             "ntxy":"3",
                             "ntxo":"7",
                             "ntyy":"6",
                             "nthi":"1",
                             "ntaz":"5",
                             "ntre":"8",
                             "ntkf":"-",
                             "ntux":".",
                             "ntll":"9",
                             "ntgg":"4"
                         },
                        {"nttu":"2",
                             "ntde":"0",
                             "ntcd":"3",
                             "ntfs":"7",
                             "nthj":"6",
                             "ntlm":"1",
                             "ntzb":"5",
                             "ntas":"8",
                             "ntio":"-",
                             "ntyc":".",
                             "nttn":"9",
                             "ntbb":"4"}]
    
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
                                for contentMap in contentMapList:
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
                writer = pd.ExcelWriter(file_to_be_written,engine= 'openpyxl')
                #print(df)
                if os.path.exists(file_to_be_written):    
                    book = load_workbook(file_to_be_written) 
                    writer.book = book
                    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
                #print(month)
                sheetName= monthNames[month]
                #print(sheetName)
                df.to_excel(writer,sheet_name=sheetName)
                writer.save()
            
                
    
       
        
    

if __name__ == '__main__':
    main()