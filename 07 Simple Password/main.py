import re

def SimplePassword(strParam):
  OG_pass = strParam
  passok_or_not_return = "false"
  capital_lett = False
  one_number = False
  special_chr = False
  nopasswordinpass = True
  pass_length = False

  regex =re.compile('[@_!#$%^&*()<>?/\|}{~:=+-]')

  Splitted_pass = []
  for letter in OG_pass:
    Splitted_pass.append(letter)
  
  if "password" in OG_pass.lower():  #check if "password" is in password
    nopasswordinpass = False

  if any(check.isupper() for check in OG_pass): #check if pass has capital letter
    capital_lett = True

  if any(check2.isdigit() for check2 in OG_pass): #check if pass has atleast one num
    one_number = True

  if (regex.search(OG_pass)): #check if special_char
   special_chr = True 

  if 31 > len(OG_pass) > 7: #check pass_length
    pass_length = True

  if one_number and capital_lett and pass_length and nopasswordinpass and special_chr:
    return "true"
  else:
    return "false"

# keep this function call here 
print(SimplePassword(input()))