word = input('Enter a word: ')

if word == word.upper():
    print("The word is in uppercase")
else:
    print('The word is not in uppercase')

word = input("Enter word: ")
letter = input("Enter letter: ")

index = word.find(letter)

print(index)


fruits = ['apple','banana','peach','pineapple']
fruits.append('orange')
fruits.append('kiwi')
fruits.append('mango')
print('Length of list:', len(fruits))


