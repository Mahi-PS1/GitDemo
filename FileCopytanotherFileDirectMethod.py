import shutil 

# use copyfile() 
with open ('Sample.txt','r') as firstfile:
    file_content = firstfile.readlines()
    print(file_content)

shutil.copyfile('first.txt','second.txt')  # method to copy content from base file to destination file 
