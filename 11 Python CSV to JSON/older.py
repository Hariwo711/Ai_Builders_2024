import requests
import json

response = requests.get("https://coderbyte.com/api/challenges/logs/user-info-csv")
csv_as_text = response.content.decode('utf-8')
# print(csv_as_text)
new_list = csv_as_text.split('\n')
# print(new_list)
list_for_dict = []
set_flags = []
for i in new_list:
  new_dict = {}
  splitted_new = i.split(',')
  if i == new_list[0]:
    flaggy = []
    for comm in range(len(splitted_new)):
      flaggy.append((splitted_new[comm]).lower())
    set_flags = flaggy.copy()
  else:
    count = 0
    for m in splitted_new:
      new_dict[set_flags[count]] = m
      count+=1
    list_for_dict.append(new_dict)
  # print(list_for_dict)

print(json.dumps(list_for_dict, indent=1))

# write your solution here
# print(response)