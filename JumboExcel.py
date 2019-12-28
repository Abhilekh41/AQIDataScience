#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:51:06 2019

@author: abhilekhsahay
"""

import pandas as pd
from openpyxl import load_workbook
import os

def main():
    sheets = ["January",
             "Febuary",
             "March",
             "April",
             "May",
             "June",
             "July",
             "August",
             "September",
             "October",
             "November",
             "December"]
    print(sheets)
    file_to_be_written = "jumboExcel.xlsx"
    cities = ['Delhi','Kolkata','Chennai','Patna','Bangalore','Hyderabad','Thiruvananthapuram','Jaipur']
    for city in cities:
        for year in range(2000,2019):
            finalDataFrame=pd.DataFrame()
            dataFrameList = []
            #print(sheets)
            for sheet in sheets:
                file_to_be_read = "{}/Excel/{}.xlsx".format(city,year)
                data = pd.read_excel(file_to_be_read,sheet_name = sheet)
                #print(len(data))
                
                data = data.drop([data.index[0],data.index[len(data)-2],data.index[len(data)-1]])
                data['Month'] = sheet
                data['Year'] = year
                data['City'] = city
                dataFrameList.append(data)
            finalDataFrame = pd.concat(dataFrameList)
            writer = pd.ExcelWriter(file_to_be_written,engine= 'openpyxl')
            if os.path.exists(file_to_be_written):    
                book = load_workbook(file_to_be_written) 
                writer.book = book
            finalDataFrame.to_excel(writer,sheet_name="Data")
            writer.save()
                

    

if __name__ == '__main__':
    main()