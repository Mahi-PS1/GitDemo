var1=3
while var1>1:
    print(var1)
    var1-=1
print("while runs till the condition is reached")

# to skip elements inbetween i.e., 3
var2 = 4
while var2>1:
    if var2!=3:
        print(var2)

    var2-=1

print("3 is not printed")

#Break Statement Usage 
var3=4
while var3>1:
    if var3 ==2:
        break
    print(var3)
    var3-=1
print("Break statement execution done")


    
    