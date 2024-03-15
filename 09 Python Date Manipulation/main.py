import requests
import json
from datetime import datetime
from dateutil import parser
response = requests.get("https://coderbyte.com/api/challenges/json/date-list")

date_list = response.json()

dates = [item['date'] for item in date_list] #getting only the dates out of list with dicts

def turnintomilitary_time_iso(value): #turn into iso 8601 for datetime without utc
  return_new = (value.isoformat())+".000Z"
  return return_new

def military_iso_for_utc(value):#turn into iso8601 for datetime with utc
  return_new = value.isoformat().replace("+00:00",".000Z")
  return return_new

dates.sort() #sorting dates to be in right order
new_dates=[] #creeating new list for values that are missing to add to this list
count = 0 #a counter for for loop
for datesss in dates:
  if count == 0:
    count += 1
    new = parser.parse(datesss) #the new date for first time running
    new_dates.append(military_iso_for_utc(new)) #adding the first value of all
  else:
    first = parser.parse(dates[count-1]) #getting the date one step before to compare
    second = parser.parse(datesss) #getting second date to compare to first
    distance = second.day - first.day #finding the distance between both dates
    if distance >=1: #if dates are missing
      for i in range(distance-1):  #distance -1 because only need to run the date that is missing
        datetime_date = datetime(first.year, first.month, first.day+i+1, 5, 0, 0) #setting dates manually for missing
        iso_date = turnintomilitary_time_iso(datetime_date) #giving it to the function
        new_dates.append(iso_date) #adding missing to list
    new_dates.append(military_iso_for_utc(second)) #adding dates that already existed
    count+=1

new_dates.sort() #just for safe if something goes haywire

finished_hopefully = [] #making a hopefully last list

for dating in new_dates:
  new_dict = {} #creating dict for each date and their value
  new_dict["date"] = dating #setting dates in dict
  for wow in date_list:
    if dating == wow["date"]:
      new_dict["value"]=wow["value"] #if same date set the value for that
      break
    else:
      new_dict["value"]=0 #if not same date set value to 0

  finished_hopefully.append(new_dict) #put set into list

print(json.dumps(finished_hopefully)) #finishing by printing