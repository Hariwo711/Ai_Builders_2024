def SumMultiplier(arr):
  sum_all = sum(arr)
  double_sum = sum_all*2
  for leng in range(len(arr)):
    for steps in range(len(arr)):
      if arr[leng]*arr[steps]>double_sum:
        arr = 'true'
        break
      if leng == len(arr)-1 and steps == len(arr)-1:
        arr = 'false'
        break
    else:
      continue
    break

  # code goes here
  return arr

# keep this function call here 
print(SumMultiplier(input()))