import requests
import json
import pandas as pd
response = requests.get("https://coderbyte.com/api/challenges/logs/user-info-csv")
csv_as_text = response.content.decode('utf-8')
new_list = csv_as_text.split('\n')
list_for_dict = [] #create list for all the dicts
set_flags = [] #for the flags name email and phone
for i in new_list: #for so long as list has
  new_dict = {}
  splitted_new = i.split(',')
  if i == new_list[0]: #if its the first colum then set flags
    flaggy = []
    for comm in range(len(splitted_new)):
      flaggy.append((splitted_new[comm]).lower())
    set_flags = flaggy.copy()
  else: #every other colum
    count = 0
    for m in splitted_new: #setting dicts with flags
      new_dict[set_flags[count]] = m
      count+=1
    list_for_dict.append(new_dict) #adding them to list

df = pd.DataFrame.from_dict(list_for_dict) #turning dict into pandas df
df_sort = df.sort_values(by=['email']) #sort by second cloum 'email'
json_fin = df_sort.to_json(orient='records')
parsed = json.loads(json_fin)
print(json.dumps(parsed, indent=1)) #printing output