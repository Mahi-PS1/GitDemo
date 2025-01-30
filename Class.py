##self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

class Cal():
    num1=3

    def getNum(self):
        print("Method in Class")
Ref_Obj = Cal() # syntax to create object of class 
Ref_Obj.getNum()
print(Ref_Obj.num1)