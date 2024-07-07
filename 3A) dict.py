'''Create a dictionary for words and their meanings. 
Write functions to add a new entry (word: meaning), search for a 
particular word and retrieve meaning, given meaning find words with same meaning, 
remove an entry, display all words sorted alphabetically. 
[Program must be menu driven].'''

def new(w,m):
    d[w]=m
    print("New word added")
def search(w):
    if w in d:
        print("Meaning of",w,"is",d[w])
    else:
        print("Word not found")
def sameMeaning(m):
    for i in d:
        if d[i]==m:
            print(i, end = " ")
    print()
def remove(w):
    if w in d:
        del d[w]
def display():
    for i in sorted(d):
        print(i, end = " ")
    print()
d = {}
while True:
    print("\n1. Add a new word")
    print("2. Search for a word")
    print("3. Find words with same meaning")
    print("4. Remove a word")
    print("5. Display all words")
    print("6. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        w = input("Enter word: ")
        m = input("Enter meaning: ")
        new(w,m)
    elif ch == 2:
        w = input("Enter word: ")
        search(w)
    elif ch == 3:
        m = input("Enter meaning: ")
        sameMeaning(m)
    elif ch == 4:
        w = input("Enter word: ")
        remove(w)
    elif ch == 5:
        display()
    elif ch == 6:
        break
    else:
        print("Invalid choice")
