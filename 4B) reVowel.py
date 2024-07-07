'''Develop a python program to count all the occurrences of vowels, 
consonants and digits from the given text 
using Regular expressions.'''

import re
text = input("Enter the text: ")
text = text.lower()
vowels = re.findall('[aeiou]', text)
consonants = re.findall('[b-df-hj-np-tv-z]', text)
digits = re.findall('\d', text)
print("Vowels: ", len(vowels))
print("Consonants: ", len(consonants))
print("Digits: ", len(digits))