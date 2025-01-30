#process to declare and use multiple datatype together - using format method

a,b=3,"number"
print("{}{}{}".format("code",a,b))

# Same type of data type can be concatnate together by + 

c = "string 1 : hello "
d = "string 2 : Hi "

print("concatate the 2 strings - "+c+d)

# to find the datatype in python as python do not need explict declaration for any data type
print(type(b))
print(type(a))