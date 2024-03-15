def PermutationStep(num):
  num_to_str = str(num)
  finished = '-1'
  for i in range(len(num_to_str)):
    if i == 0:
      pass
    else:
      if num_to_str[-i] > num_to_str[-i-1]:
        finished = num_to_str.replace(num_to_str[-i-1]+num_to_str[-i], num_to_str[-i]+num_to_str[-i-1])
        if i>1:
          for m in range(len(finished)-1):
            if finished[-m-1]<finished[-m-2] and m<=i:
              new_finished = finished.replace(finished[-m-2]+finished[-m-1], finished[-m-1]+finished[-m-2])
              if new_finished < finished and new_finished> num_to_str:
                finished = new_finished
              else:
                break
            else:
              pass
        break

  return finished

# keep this function call here 
print(PermutationStep(input()))