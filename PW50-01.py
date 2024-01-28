import random


def number_guess():
    bb = random.randint(1,100)
    required_base = random.choice([2,8, 10, 16])
    count = 0

    while True:
        print(required_base)
        # 진법에 맞춰 숫자 입력해야 함

        in_number = int(input('Give me the answer as integer between 10~20: '), required_base)
        if in_number < bb:
            print(f"it's higher than {in_number:#>10}")
            count += 1
        elif in_number > bb:
            print(f"it's lower than {in_number:#>10}")
            count += 1
        else:
            print("You got it!!")
            break
        
        if count > 2:
            print("ByeBye!!")
    
def word_guess():
    bb = random.choice(["cat", "dog", "plane", "axe", "humor", "ultra"])


    while True:
        input_word = input('Give me the word')
        if input_word < bb:
            print(f"it's later than {bb}")
        elif input_word > bb:
            print(f"it's earlier than {bb}")
        else:
            print("You got it!!")
            break
        
def mysum(*number):
    output = 0
    for i in number:
        output += i
    print(output)

def word_summary(words):
    length = [len(word) for word in words]
    return max(length), min(length), sum(length) / len(words)


def int_convertible(obj): # 2-3
    try:
        a = int(obj)
        return a
    except ValueError:
        return False

def object_sum(objs):  # 2-3
    return sum(obj for obj in objs if int_convertible(obj))


def run_timing():
    count = 0
    sum_min = 0
    while True:
        run_time = input("enter 10km run time: ")
        if not run_time: # emtpy string is False, so not empty is True
            break
        try:
            run_time = float(run_time)
        except ValueError as e:
            print("wrong number!!")
        count += 1
        sum_min += run_time
    print(f"Average of {sum_min/count:5f}, over {count:4d} runs") 

def float_format(a: float, before_decimal, after_decimal):
    string_float = str(a)
    i = string_float.index('.')
    return float(string_float[i-before_decimal:i+after_decimal+1])

from decimal import Decimal

def sum_decimal():
    a = input("Enter number 1: ")
    b = input("Enter number 2: ")
    c = Decimal()
    c = Decimal(a) + Decimal(b)
    print(c)


def hex_dec(hex_a):
    hex_str = str(hex_a)
    length = len(hex_str)
    b = 0
    for index, number in enumerate(reversed(hex_str)):
        b += int(number, 16) * (16 ** index)
    print(b)
#a= object_sum(["words", 4, 6])
#print(a)
#mysum(3,4,5)
    
def name_triangle(name: str):
    for index, chracter in enumerate(name):
        print(name[:index+1])

def ord_hex_output():
    """Get a hex number to convert. Use ord to turn it into an integer,
and print the decimal equivalent.
"""

    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        if 48 <= ord(digit) <= 57:
            dec_digit = ord(digit) - 48
        elif 97 <= ord(digit) <= 102:
            dec_digit = ord(digit) - 87
        # 0 unicode : 48, 9 unicode = 57, so minux 48
        # a unicode : 97, f unicdoe = 102, so minus 87
        
        
        decnum += dec_digit * (16 ** power)
    print(decnum)


if __name__ == "__main__":
    name_triangle("youngdoo")

#print(word_summary(["dog", "plane", "bigbig"]))

