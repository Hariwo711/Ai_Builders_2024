def LetterCountI(strParam):
  word_list = strParam.split()
  answer = "-1"
  max_char = 0
  longest = {}
  for word in word_list:
    word_dict = {}
    for letter in word:
      if letter in word_dict:
        word_dict[letter]+=1
      else:
        word_dict[letter] = 1
      max_char = max(word_dict.values())
    longest[word]=max_char
  for i in range(len(word_list)):
    if max(longest.values()) != longest[word_list[i]]:
      answer = "-1"
    elif max(longest.values())>1:
      answer = word_list[i]
      break
    else:
      break
  
  return answer

# keep this function call here 
print(LetterCountI(input()))