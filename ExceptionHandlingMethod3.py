# try & catch is being used when user know that exception can come but test case execution need not be to stopped 
# try handle with the exception & catch contains the code 
CartCount = 0 
if CartCount!=2:
    pass
assert(CartCount==0)
try:
     with open('filelog.txt','w') as reader: # file log do not exist in system : i.e., an exception 
        reader.read()  
# python uses except keyword in place of catch f

except:
    print("Some failure is there")    # customized error message 

try:
     with open('filelog.txt','w') as reader: # file log do not exist in system : i.e., an exception 
        reader.read()  
# python uses except keyword in place of catch 
except Exception as e:
    print(e)    # pthon self error message 
