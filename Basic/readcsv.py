# -*- coding: utf-8 -*-
import csv
try:
    with open("c:\\data1.csv") as csvfile:
        rowdata = csv.reader(csvfile, delimiter=',')
        dates = []
        colors = []
        for row in rowdata:
            dates.append(row[0])
            colors.append(row[3])
        print(dates)
        print(colors)
except Exception  as e:
    print("File is not found")
    

        
