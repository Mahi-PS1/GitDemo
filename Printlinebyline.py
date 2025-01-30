# Print Line by Line Using Read Line Method 

File_Line = open('Test.txt')
Line_By_Line=File_Line.readline()
while Line_By_Line!="":
    print(Line_By_Line)
    Line_By_Line=File_Line.readline()



