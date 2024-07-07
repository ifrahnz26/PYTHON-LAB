n1 = int(input("Enter number 1: "))
n2 = int(input("Enter numebr 2: "))
print("1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE")
choice = int(input("Enter your choice "))
if choice == 1:
    print("Sum: ", n1+n2)
elif choice == 2:
    print("Difference: ", n1-n2)
elif choice == 3:
    print("Product: ", n1*n2)
elif choice == 4:
    print("Quotient: ", n1/n2)
else:
    print("Invalid choice")