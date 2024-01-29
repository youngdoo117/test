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

def pig_latin(aa: str):
    length = len(aa)
    bb = ""
    # if aa[0].isupper():
    #     vowels = "AEIOU"
    # else:
    #     vowels = "aeiou"

    punctuation = ''
    if aa[-1] in ".!?":
        punctuation = aa[-1]
        aa = aa[0:-1]

    if aa[0].lower() in "aeiou":
        bb = f"{aa[0:]}way"
    else:
        bb = f"{aa[1:]}{aa[0]}ay"
    bb += punctuation
    print(bb)

def pig_latin2(aa: str):
    if len(set("aeiou") & set(aa)) > 1:
        bb = f"{aa}way"
    else:
        bb = f"{aa[1:]}{aa[0]}ay"
    print(bb)

def pig_latin3(aa: str):
    result = []
    for word in aa.split():
        if word.lower() in "aeiou":
            result.append(f"{word[0:]}way")
        else:
            result.append(f"{word[1:]}{word[0]}ay")
    print(' '.join(result))







def strsort(instr):
    print(''.join(sorted(instr)))


strsort("youngdoo")
          


def transpose_array():
    a= ["With the ring", "of light from", "his lantern dancing"]
    bb = []
    cc= []
    for words in a:
        word = words.split()
        bb.append(word)

    print(bb)

    for i, _ in enumerate(a):
        for j, _ in enumerate(a):
            bb[i][j] = bb[j][i]


    print(bb)
     
def ips_for_404s(filename):
    """Given the name of an Apache logfile,
print the IP address where the response code
is 4040

"""
    for one_line in open(filename):
        if ' 404 ' in one_line:
            print(one_line.split()[0])\

def ubbi_dubbi(in_str: str):
    output = []
    for ch in in_str:
        if ch.lower() in 'aeiou':
            if ch.islower():
                output.append(f"ub{ch}")
            else:
                output.append(f"Ub{ch.lower()}")
        else:
            output.append(ch)
    print(''.join(output))

def url_encoding(in_str):
    output = []
    for ch in in_str:
        if ch.lower() not in "abcdefghijklmnopqrstuvwxyz1234567890":
            output.append(f"%{hex(ord(ch))}")
        else:
            output.append(ch)
    print(''.join(output))
    

    
                                        
def filetext_pig():
    with open("d:/sample.txt", "r", encoding='utf-8') as f:
        lines= f.readlines()
        f.seek(0)
        contents =f.read()
        print(contents)
        result = []
        for index, line in enumerate(lines):
            words = line.split()
            if index > len(words):
                break
            result.append(words[index])

        print(' '.join(result))

    modified_contents = contents.replace('.','.\n').replace('!','!\n').replace('?','?\n')


    print(modified_contents)

    with open("d:/sample2.txt", "w", encoding='utf-8') as f:
         f.write(modified_contents)


def last_word():
    with open("d:/sample.txt", "r", encoding="utf-8") as f:
        content = f.read()
        words = content.split()
        print("last word : ", words[-1])
        longest_word = ""
        for w in words:
            if len(w) > len(longest_word):
                longest_word = w
        print(longest_word)
        

def last_word2():
    i = 0
    result = []
    for w in open("d:/sample.txt", encoding="utf-8"):
        words = w.split()
        for wd in words:
            result.append(wd)
        
    print(result)


if __name__ == "__main__":
    name_triangle("youngdoo")
    print("\n\n")
    pig_latin('Wine!')
    pig_latin('Eol?')
    pig_latin3("I have a dream")

#print(word_summary(["dog", "plane", "bigbig"]))

