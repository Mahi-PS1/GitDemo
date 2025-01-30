# first file print content and in second empty file copy the content from first file 

with open ('Sample.txt','r') as firstfile: # for consistency calling object as "reader"
    file_content = firstfile.readlines()
    print(file_content)

with open('copyfile.txt','a') as copyfile: # append file 'a'
        for line in file_content: 
              copyfile.write(line)
        

