x=input()
list=['a','e','i','o','u']
if len(x)<2:
  if x in list:
    print("Vowels")
  else:
    print("Consonants")
else:
  print("invalid")
