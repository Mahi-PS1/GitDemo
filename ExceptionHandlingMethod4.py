# Finally keyword being used for exception handling , 
# can be used with try and catch and in any case exception active or not finally block always works 
CartCount = 0 
if CartCount!=2:
    pass
assert(CartCount==0)
try:
     with open('filelog.txt','r') as reader: # file log do not exist in system : i.e., an exception 
        reader.read()  
# python uses except keyword in place of catch f

except Exception as e:
    print(e)  

finally:
    print("finally block execute in all cases") # example clearing data post usage , deleting cookiies before further execution 
