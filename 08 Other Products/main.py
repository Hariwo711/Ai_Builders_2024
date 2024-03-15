def OtherProducts(arr):
  og_arr = arr
  answer = []

  for number in og_arr: #running for every number
    new_list = og_arr.copy()
    new_list.remove(number)
    calculation = 1
    for multiply_nums in new_list: #for multiplying numbers
      calculation = calculation * multiply_nums
    else:
      answer.append(calculation)
  
  hypen = "-" #set seperator
  answer_str = hypen.join(str(int_answer) for int_answer in answer) #join list by making int into str
  
  return answer_str

# keep this function call here 
print(OtherProducts(input()))