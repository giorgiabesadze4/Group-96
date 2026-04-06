#დავალება 1)

word = input("შეიყვანე სიტყვა: ")

if word.isupper():
    print("სიტყვა მთლიანად დიდი ასოებითაა")
else:
    print("სიტყვა არ არის მთლიანად დიდი ასოებით")

#დავალება 2)

word = input("შეიყვანე სიტყვა: ")
letter = input("შეიყვანე ასო: ")

print(word.find(letter))

#დავალება 3)

fruits = ['apple','banana','peach','pineapple']

fruits.append('orange')
fruits.append('kiwi')
fruits.append('mango')

print(len(fruits))


