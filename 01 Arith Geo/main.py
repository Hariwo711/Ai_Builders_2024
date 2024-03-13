def ArithGeo(arr):
  for i in range(len(arr)):
    if arr[i]==(arr[2]-arr[1])*(i+1) and i+1 == len(arr): #checking array if same and checking len if over list length
      arr = "Arithmetic"
    elif i+1 == len(arr): #before going over give it -1
      arr = "-1"
  # code goes here
  return arr

# keep this function call here 
print(ArithGeo(input()))

#input only works in codebytes cause in VScode it comes as string not list