num = int(input('Enter a number: '))

if num > 0:
    print('positive')
elif num < 0:
    print('negative')
else:
    print('zero')


password = input('Enter password: ')

if password == 'python123':
    print('Access granted')
else:
    print('Wrong password, try again')

fruits = ["banana" , "apple" , "orange" , "mango" , "cherry"]
print(fruits[1])
print(fruits[2])
print(fruits[4])