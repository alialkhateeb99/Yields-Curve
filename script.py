# importing the requests module
from math import nan
import requests
from zipfile import ZipFile
import pandas as pd
import json
import openpyxl
# pip install requests, pandas, openpyxl

print('Downloading started')
url = 'https://www.bankofengland.co.uk/-/media/boe/files/statistics/yield-curves/glcnominalmonthedata.zip'

# Downloading the file by sending the request to the URL
req = requests.get(url)
 
# Split URL to get the file name
filename = url.split('/')[-1]
 
# Writing the file to the local file system

with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')


# Create a ZipFile Object and load sample.zip in it

with ZipFile(filename, 'r') as zipObj:
# Extract all the contents of zip file in current directory
    zipObj.extractall()


MATURITY_YEAR = "date"
ITEM = "item"
VALUE = "value"

list_of_items = []

df = pd.read_excel(
    io='GLC Nominal month end data_2016 to present.xlsx',
    sheet_name='2. fwd curve',skiprows=3)
df = df.astype(str)

dates_lists = []

dict = df.to_dict()
for index,item in dict['years:'].items():
    dates_lists.append(item)

for index,item in dict.items():
    i = 0
    maturity_in_years = index
    if(maturity_in_years == 'years:'):
        continue
    for key, val in item.items():
        if(val == 'nan'):
            i+=1
            continue

        list_of_items.append({
            MATURITY_YEAR: dates_lists[i],
            ITEM:"GBP_inf_fwd_"+str(index),
            VALUE:round(float(val),2)
        })
        i+=1


for item in list_of_items:
    print(item)

# for i in range(len(list_of_items)):
#     if(list_of_items[i]['item'] == "GBP_inf_fwd_24.5"):
#         print(list_of_items[i])
