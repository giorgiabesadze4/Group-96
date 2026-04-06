def greet(name):
    return f'Hello {name}'

def add(a, b):
    return a + b

def check_number(n):
    if n % 2==0:
        return "ლუწია"
    else:
        return 'კენტია'
    
def power(a, b):
    return a ** b

def string_length(text):
    return len(text)

def reverse_word(word):
    return word[::-1]

def sum_list(numbers):
    return sum(numbers)

def check_age(name, age):
    if age < 18:
        return f'{name} is not adult'
    else:
        return f'{name} is adult'