#open file by making object 
fileUsage = open('Test.txt') 
#Read all the content of file 
#print(fileUsage.read())
print(fileUsage.read(2))#reads 2 bytes of the file of the starting 
fileUsage.readline() # read first line in file 
fileUsage.readline() # read next line in file 
# Remember read(2)followed with readline() starts reading from the character where it left off 
fileUsage.read()
fileUsage.close()