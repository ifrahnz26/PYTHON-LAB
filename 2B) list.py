
'''Write a python program to create a list with all the subject names of the 4th semester 
and perform the following operations.
• Display the list using for loop.
• Display 2nd and 5th element of the list.
• Display first 4 elements of the list using the range of indexes.
• Display last 4 elements of the list using the range of negative indexes.
• Display if "Python Programming Lab" is available in the List or not.
• Demonstrate the working of append () and insert () function.
• Demonstrate the working of remove() and pop() function.'''

sub = ['Math', 'MC & IOT', 'DAA', 'DCN', 'FAFL', 'Python Programming lab', 'Data Analysis Using R']

# Display the list using for loop.
print("List of 4th semester subjects:")
for subject in sub:
    print(subject, end=", ")
print("\n")  

# Display 2nd and 5th element of the list
print(f"2nd element: {sub[1]}")
print(f"5th element: {sub[4]}\n")

# Display first 4 elements of the list using the range of indexes.
print("First 4 elements:")
for i in range(4):
    print(sub[i])
print()

# Display last 4 elements of the list using the range of negative indexes.
print("Last 4 elements:")
for i in range(-4, 0):
    print(sub[i])
print()

# Display if "Python Programming Lab" is available in the List or not.
if "Python Programming lab" in sub:
    print("Yes, 'Python Programming lab' is a 4th semester subject.\n")
else:
    print("No, 'Python Programming lab' is not a 4th semester subject.\n")

# Demonstrate the working of append() and insert() function.
print("List after append() and insert() operations:")
sub.append("DAA Lab")
sub.insert(4, "DCN Lab")
print(sub)
print()

# Demonstrate the working of remove() and pop() function.
print("List after remove() and pop() operations:")
sub.remove("FAFL")
sub.pop()
print(sub)
