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
    sheets = {"January",
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
             "December"}
    file_to_be_written = "/Users/abhilekhsahay/AQIDataScience/jumboExcel.xlsx"
    cities = ['Delhi','Bangalore','Chennai','Patna','Jaipur','Hyderabad','Thiruvananthapuram','Kolkata']
    for city in cities:
        for year in range(2000,2001):
            for sheet in sheets:
                file_to_be_read = "/Users/abhilekhsahay/AQIDataScience/{}/Excel/{}.xlsx".format(city,2000)
                data = pd.read_excel(file_to_be_read,sheet_name = sheet)
                print(data)
                dataFrame = pd.concat(data[frame] for frame in data.keys())
                writer = pd.ExcelWriter(file_to_be_written,engine= 'openpyxl')
                if os.path.exists(file_to_be_written):    
                    book = load_workbook(file_to_be_written) 
                    writer.book = book
                dataFrame.to_excel(writer,sheet_name="Data")
                writer.save()
                

    

if __name__ == '__main__':
    main()