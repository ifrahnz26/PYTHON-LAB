'''Write a python program to create a text file and ask the user 
to enter 5-6 lines of text. Display the longest 
and the shortest word from the file. 
Display the length of these words.'''

lines = [input(f"Enter line {i+1}: ") for i in range(5)]
f = open("file.txt", "w")
f.writelines(lines)
f.close()
f = open("file.txt", "r")
words = f.read().split()
words = sorted(words)
longest = words[-1]
shortest = words[0]
print(f"Longest word: {longest} (length: {len(longest)})")
print(f"Shortest word: {shortest} (length: {len(shortest)})")
f.close()
