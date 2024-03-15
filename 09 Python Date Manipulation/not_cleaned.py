import requests
import pandas as pd
import json
from datetime import datetime, timedelta
from dateutil import parser
response = requests.get("https://coderbyte.com/api/challenges/json/date-list")

# date_list = eval(response.content.decode('utf-8'))
date_list = response.json()

dates = [item['date'] for item in date_list]
values = [item['value'] for item in date_list]
# print(date_list)
# print(type(dates[1]))

def turnintomilitary_time_iso(value):
  return_new = (value.isoformat())+".000Z"
  # return_new = str(value)
  return return_new

def military_iso_for_utc(value):
  return_new = value.isoformat().replace("+00:00",".000Z")
  return return_new


# print(values)
dates.sort()

isoformat_want = 0

new_dates=[]
count = 0
# datefor_test
for datesss in dates:
  new = parser.parse(datesss)
  if count == 0:
    count += 1
    new_dates.append(military_iso_for_utc(new)) #adding the first value of all
  else:
    # print(count)
    first = parser.parse(dates[count-1])
    second = parser.parse(datesss)
    # print(first)
    # print("sfd",second)

    

    distance = second.day - first.day
    if distance >=1:
      # print("hell")
      # print(distance)
      for i in range(distance-1):
        datetime_date = datetime(first.year, first.month, first.day+i+1, 5, 0, 0) #setting dates manually for missing
        iso_date = turnintomilitary_time_iso(datetime_date)
        new_dates.append(iso_date) #adding missing to list
        # print(iso_date)
    new_dates.append(military_iso_for_utc(second)) #adding dates that already existed
    count+=1

new_dates.sort() #just for safe if something goes haywire

finished_hopefully = []

for dating in new_dates:
  # print(dating)
  
  new_dict = {}

  new_dict["date"] = dating

  for wow in date_list:
    if dating == wow["date"]:
      new_dict["value"]=wow["value"]
      break
    else:
      new_dict["value"]=0

  # if dating
  # print(new_dict)

  finished_hopefully.append(new_dict)



    # m= new.date()
    # f = new.day
    # print(f)



  # count+=1



# date_new_old = datetime(2021, 2, 4, 6, 0, 0, 0)
# print("gsdg",date_new_old)

# dates_iso = (date_new_old.isoformat())+".000Z"
# print(dates_iso)
# print(date_list)

# print(finished_hopefully)
print(json.dumps(finished_hopefully)) 

#   # new_dates.append(parser.parse(datesss))
#   # print(datetime.strftime(datesss))
# new_dates.sort()

# print(new_dates)

# print(dates)
# print(json.dumps(date_list, indent=1))
# write your solution here
# print(date_list)