# opening and closing file in one statement in place of open and close seperate statements
#file = open('Test.txt') 
# file.close()
# with helps opening files and after exection close the file automatic 

# problem stmt - read all the elements of the file and store them in list 
# reverse the list 
# write the list back to the file 

with open ('file.txt','r') as reader: # for consistency calling object as "reader"
    content = reader.readlines() # readlines used to read all content of file in form of list [ab bbb cbb dbb ebb]
    reversed(content) # [ebb dbb cbb bbb ab]
    with open('Test.txt','w') as writer:
        for index_content in reversed(content):
            print(index_content)

    # file in 'w' modw will replace it's current text save the file with new content 