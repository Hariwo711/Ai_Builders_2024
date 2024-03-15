def ThreeNumbers(strParam):
  splitted = strParam.split()
  unique= "false"
  m = 0
  next_to = 0
  for i in splitted:
    unique_letter = set()
    m +=1
    for letter in i:
      if next_to ==3:
        break
      elif letter.isnumeric():
        unique_letter.add(letter)
        next_to +=1
      else:
        next_to = 0
    if len(unique_letter)>=3 and m >= len(splitted)-1:
      unique = "true"
    elif len(unique_letter)<3:
      unique = "false"
      break
  # code goes here
  
  return unique
# keep this function call here 
print(ThreeNumbers(input()))