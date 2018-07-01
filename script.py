import numpy as np
import pandas as pd 
from pandas import Series, DataFrame

##Name, Roll Number, Room Number, Hostel Name

#CSV file for lookup and it's cleaning up

col_Names=['rollNumber', 'name', 'string']
lookup_df = pd.read_csv('lookup.csv', names=col_Names)
lookup_df.dropna(axis=0, how='any')
del lookup_df['string']

#CSV file up for hostel allotment and it's cleaning up

col_Names=['rollNumber', 'hostelName', 'roomNumber']
hostel_df = pd.read_csv('hostel.csv', names=col_Names)
hostel_df.dropna(axis=0, how='any')
hostel_df['Address'] = hostel_df['hostelName']+' - '+hostel_df['roomNumber'].astype(str)
del hostel_df['hostelName']
del hostel_df['roomNumber']

lookup_df['hostelName'] = 'str'
lookup_df['floor'] = 'str'
lookup_df['roomNumber'] = 'str'
for index, rows in lookup_df.iterrows():
    
    substring = str(rows['rollNumber'])
    for index1, rows1 in hostel_df.iterrows():
        string = str(rows1['rollNumber'])
        if(string.find(substring) != -1 ):
            
            address = rows1['Address']
            hostelName = address[:7]
            floorName = address[8:13]
            roomNumber = address[17:]
            #lookup_df.set_value(index, 'hostelName',hostelName)
            lookup_df['hostelName'][index] = hostelName
            lookup_df['floor'][index] = floorName
            lookup_df['roomNumber'][index] = roomNumber
            break; 
                        
        



        

lookup_df.to_csv('output.csv')



