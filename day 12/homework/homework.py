#დავალება 3)
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#დავალება 4)
temp = int(input("Enter temperature: "))

if temp > 30:
    print("It's Hot")
elif temp >= 15:
    print("It's Warm")
else:
    print("It's Cold")
#დავალება 5)
number = int(input("Enter number: "))
if num > 0:
    if num % 2:
        print('Positive even')
    else: 
        print('Positvie odd')
else:
    print("Negative")
#დავალება 6)
num = int(input("Enter number: "))

for i in range(num + 1):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")
#დავალება 7)
positive = 0
negative = 0
zero = 0

for i in range(10):
    num = int(input("Enter number: "))
    
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
#დავალება 8)
fruits = ["apple", "banana", "orange", "grape"]
fruits[1] = "kiwi"
print(fruits)
#დავალება 9)
nums = [4, 8, 12, 16, 20]
result = nums[0] + nums[-1]
print(result)
#დავალება 11)
nums = [1, 2, 3, 4, 5, 6]
for num in nums:
    if num % 2 == 0:
        print(num)
#დავალება 14)
word = 'hello'
for letter in word:
    print(letter)
#დავალება 15)
my_list = [10, 20, 30, 40, 50]
print(my_list[:3])