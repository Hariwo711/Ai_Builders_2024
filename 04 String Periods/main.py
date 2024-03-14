def StringPeriods(strParam):
  # code goes here
  result = "-1"
  for test_leng in range(len(strParam)):
    test_func = test_leng+1
    if strParam[:test_func] == strParam[test_func:test_func*2]:
      result = strParam[:test_func]
      break
    else:
      result = "-1"
  return result
# keep this function call here 
print(StringPeriods(input()))