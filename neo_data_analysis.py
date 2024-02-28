import datetime
from datetime import datetime, date, timedelta
import requests
import json
import texttable

def DateConvertPlus (z):

    Convert = datetime.strptime(StartDate,'%Y-%m-%d').date()
    result = str(Convert + timedelta(days=z))
    return result

print("Date format YYYY-MM-DD")

StartDate = input("Enter the Start date :")
EndDate = input("Enter the End date :")
try:
    day,month,year=StartDate.split('-')
    day, month, year = EndDate.split('-')
except :
    print('Error: the split between year,month and date are '-' :')

try:
    datetime.strptime(StartDate,'%Y-%m-%d').date()
    datetime.strptime(EndDate, '%Y-%m-%d').date()
except:
    print("Error: Date format should be as YYYY-MM-DD :")

try:
    def StartLessThanEndDate():
        Convert1 = datetime.strptime(StartDate, '%Y-%m-%d').date()
        Convert2 = datetime.strptime(EndDate, '%Y-%m-%d').date()
        result = (Convert2 - Convert1).days
        return result
    if StartLessThanEndDate() >0:
        print('Pass')
except:
    print("The start date should be less than the end date :")


ApiKey = 'UE0gpRB3LCjeLYMBvclvjgZJbPvCizq0qZhbcOuG'

res = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={StartDate}&end_date={EndDate}&api_key={ApiKey}')
data = json.loads(res.text)

NTable=texttable.Texttable(max_width=0)
NTable.set_cols_align(["c", "c", "c", "c", "c"])
NTable.set_cols_dtype(["a", "a", "a", "a", "a"])
NTable.set_cols_valign(["m", "m", "m", "m", "m"])

KResult=StartDate
D=0
k=0
while D <= 6:
            for i in res.json()['near_earth_objects'][KResult]:
               name_of_objects = i['name']
               estimated_diameter_min = i['estimated_diameter']['kilometers']['estimated_diameter_min']
               estimated_diameter_max = i['estimated_diameter']['kilometers']['estimated_diameter_max']
               for item in i['close_approach_data']:
                   close_approach_data = item['close_approach_date_full']
                   miss_distance = item['miss_distance']['kilometers']

                   # print(name_of_objects, estimated_diameter_min, estimated_diameter_max, close_approach_data, miss_distance)
                   NTable.add_row([name_of_objects, estimated_diameter_min, estimated_diameter_max, close_approach_data,
                                  miss_distance])
                   print(NTable.draw())
            D+=1
            while KResult != EndDate:
              k+=1
              KResult=DateConvertPlus(k)
              break
