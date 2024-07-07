'''Write a python program to create a tuple and perform the following operations  
• Adding an items
• Displaying the length of the tuple
• Checking for an item in the tuple
• Accessing an items'''

t = ()
lst = list(map(str, input("Enter items in tuple: ").split()))
# Adding items to the tuple
for i in lst:
    t = t + (i,)
print(f"Tuple after adding items: {t}")

# Displaying the length of the tuple
print(f"Length of the tuple: {len(t)}")

# Checking for an item in the tuple
item = 'DAA'
print(f"Is '{item}' present in the tuple? {'Yes' if item in t else 'No'}")

# Accessing an item from the tuple
index_to_access = 2
print(f"Item at index {index_to_access}: {t[index_to_access]}")


