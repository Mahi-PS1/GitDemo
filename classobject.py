class C:

    # class attribute
    name = ""
    age = 0

# create C1 object
C1 = C()
C1.name = "Blu"
C1.ge = 10

# create another object C2
C2 = C()
C2.name = "Woo"
C2.age = 15

# access attributes
print(f"{C1.name} is {C1.age} years old")
print(f"{C2.name} is {C2.age} years old")