# Dictionary is the Key : Value pair 
Dic = {1:"First Name",2:"Second Name",3:"Third Name"}
print(Dic[1])
print(Dic[3])
#dictionary should be having "" in case of string in key or value respectively 
#important ------
#how to create dictionary at run time add data to it 
print("-----Dynamically Insert Data in Dictionary-----")
Dict={}
Dict["First Name"]="ABC"
Dict["Last Name"]="DEF"
print(Dict)
print(Dict["Last Name"])