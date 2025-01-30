# base class
class Base:
    def method1 (self):
        print( "First Method from Base class")
    
    def method2(self):
        print("First Method from Base class")

# derived class
class Derived_Class(Base):
    
    def derivedclass_menthod(self):
        print("Method from Derived class")

# Create object of the Derived class
dog1 = Derived_Class()

# Calling members of the base class
dog1.method1()
dog1.method2()

# Calling member of the derived class
dog1.derivedclass_menthod();