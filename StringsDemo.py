str = "first. String"
str_second=" second string"
str_third=" String"
# print character in a string - starts from 0th Index 
print(str[1]) #i
# Substring in python 
print(str[0:5]) # 0 to n-1 and it is exclusive for last index 
#concatenation of 2 strings 
print(str +str_second)
# how to check 1 string or it's part is present in second string or not IMPORTANT
# str_third in str 
# sub string check 
print(str_third in str)
#split in string
# store the splitted string in a variable , and split it in form of list 
var = str.split(".")
print(var)
# extract first from the list 
print(var[0])
# trim =  used to remove white spaces from starting and end 
trim_str = "   Good  B  "
#method to trim 
print(trim_str.strip())
#method to trim from left side 
print(trim_str.lstrip())
print(trim_str.rstrip())