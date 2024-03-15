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
print(type(dates[0]))
# print(date_list)
new_list = []
for datesss in dates:
#   hi = parser.parse(datesss)
#   timestamp = datetime.strptime(hi, '%Y-%m-%d %H:%M:%S')
#   
    hi=datetime.fromisoformat(datesss)
    # print(hi)
    new_list.append(str(hi))  
  # print(datetime.strftime(datesss))

new_list.sort()

print(new_list)
dates.sort()


# # Parse the JSON data directly
# date_list = response.json()

# # Extract dates for easier comparison
# dates = [item["date"] for item in date_list]

# # Find earliest and latest dates
# from datetime import datetime
# dates = [datetime.fromisoformat(date[:-1]) for date in dates]
# earliest = min(dates)
# latest = max(dates)

# # Create a new list with the complete date range
# new_data = []
# current_date = earliest
# while current_date <= latest:
#     date_str = current_date.strftime("%Y-%m-%dT05:00:00.000Z")
#     found = False
#     for item in date_list:
#         if item["date"] == date_str:
#             new_data.append(item)
#             found = True
#             break
#     if not found:
#         new_data.append({"date": date_str, "value": 0})
#     current_date += timedelta(days=1)

# # Print the final JSON object
# print(json.dumps(new_data, indent=1))

# print(dates)

# print(date_list)
# print(new_dates)

# print(dates)
# print(json.dumps(date_list, indent=1))
# write your solution here
# print(date_list)



# test = ['2022-02-04T06:00:00.000Z', '2022-02-08T06:00:00.000Z', 
#  '2022-02-10T13:10:00.000Z', '2022-02-10T13:15:00.000Z', 
#  '2022-02-10T13:20:00.000Z', '2022-02-10T13:30:00.000Z', 
#  '2022-02-12T07:00:00.000Z', '2022-02-28T06:00:00.000Z']

# 2022-02-04T06:00:00.000Z
# 2022-02-04T06:00:00.000Z