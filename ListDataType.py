Value =[2 ,4,"num1"]
print(Value[0])

# List is the data type that is array and allows different data type to be used together 
# for last Index -1 is used 
print(Value[-1])
#sub list values 
print(Value[0:2]) # do not take the last index value if takes index - 1 value in the index 
#Insert values in existing list 
Value.insert(3 , "Last Value")
print(Value)
# to add value in the last index of list use - Append 
Value.append("END")
print(Value)
Value.insert(-1 , "-----")
print(Value)

#Update values in List for existing values 
Value[2] = "NUM1"
print(Value)

# Deletion of element in list 

del Value[1]
print(Value)