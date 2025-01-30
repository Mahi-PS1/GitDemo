from OopsConceptwithconstructor import Calculator

class Inheritance(Calculator): 
# synax for inheritated class is - class classname(class name to be inheritated) suggestion "from parent filename import classname(in parent class)"
    num2=200

    def __init__(self):
        Calculator.__init__(self,2, 4)  

    def getcompleteData(self):
        return self.num2 + self.num+self.Summation()      

obj= Inheritance() 
obj.getcompleteData()