#accept the string check the string is palindrome (madam=madam)

str=input("enter a string : ")
rev=str[::-1]
  
if str==rev:
    print(str,"is a palindrome numbers")
else:
    print(str,"is not a palindrome numbers")
