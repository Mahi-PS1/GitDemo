#Itterate in list using for loop 
dict = [2,5,3,4]
for i in dict:
    print(i)
print("{}".format("list printed"))
#Loops examples 1st 
print("----------------")
# Multiple of 2 needs to be print in the list elements
for i in dict:
    print(i*2)
print("multiple of 2 in list elements")
# Sum of first five natural numbers 
#range (i.j) -> i to j-1
sum_output =0
for j in range(1,6):
    sum_output=sum_output+j
print(sum_output)
# with Increment 
for m in range(1,15,5):
    print(m)
print("-------------------")
# when there is no starting range the index provided in the for loop is taken as the end index 
for w in range(10):
    print(w)

#Loop example 2 ------
