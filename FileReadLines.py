File_Line = open('Test.txt')
#values = [ab bbb cbb dbb ebb]
Line_By_Line=File_Line.readlines()
# read and readlines read all lines difference is readlines read and store data in form of list 
#readlines store file in form of list data 
for line in Line_By_Line:
    print(line)