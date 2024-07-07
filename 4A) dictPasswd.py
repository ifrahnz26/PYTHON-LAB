''' Write a python program to initialize a dictionary of usernames and passwords
associated with it.passwd={"rahul": "genius", "kumar": "smart", "ankita": "intelligent"} 
Perform the following functions:
• To print all the items in the dictionary.
• To print all the keys in the dictionary.
• To print all the values in the dictionary.
• To get the passwords of users. For example, passwd["rahul"]= genius
• e) Change the password of a particular user. For example, passwd["ankita"]="brilliant""'''

passwd={"rahul": "genius", "kumar": "smart", "ankita": "intelligent"} 
print("All the items in the dictionary are:")
print(passwd.items())
print("All the keys in the dictionary are:")
print(passwd.keys())
print("All the values in the dictionary are:")
print(passwd.values())
print("To get the passwords of users")
print("Rahul: ", passwd["rahul"])
print("Kumar: ", passwd["kumar"])
print("Ankita: ", passwd["ankita"])
print("To change the password of a particular user")
passwd["ankita"]="brilliant"
print(passwd)





