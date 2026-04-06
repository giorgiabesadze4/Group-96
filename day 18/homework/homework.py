def hello(name):
    return "Hello " + name


def sum_numbers(a, b):
    return a + b


def even_or_odd(num):
    if num % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"


def power(a, b):
    return a ** b


def string_length(text):
    return len(text)


def reverse_word(word):
    return word[::-1]


def list_sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total


def check_age(name, age):
    if age >= 18:
        return name + " is adult"
    else:
        return name + " is not adult"