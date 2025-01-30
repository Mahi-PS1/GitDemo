print("-----List-----")
my_list = [1, 2, 3, "apple", 4.5]
print(my_list[0])  # Access first element: 1
my_list.append(10)  # Add an item to the end
print(my_list)      # Output: [1, 2, 3, 'apple', 4.5, 10]
print("------Dict-----")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Output: Alice
my_dict["age"] = 26     # Modify value
print(my_dict)          # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}
print("------Tuple-----")
my_tuple = (1, 2, 3, "apple")
print(my_tuple[1])  # Access second element: 2
# my_tuple[1] = 10  # This will cause an error because tuples are immutable
print("----Exception Handling----")
try:
    x = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always run.")
# This is a single-line comment
print("----Comment----")
"""
This is a multi-line comment.
You can write multiple lines of text here.
"""



