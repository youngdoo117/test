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

def firstlast(sequence):
    return sequence[:1] + sequence[-1:]
    # slicing returns the same type as the original.
    # indexing returns the type of its individual elements.

def even_odd_sum(seq):
    output = []
    output.append(sum(seq[::2]))
    output.append(sum(seq[1::2]))
    return output
def plus_minus(seq):
    return sum(seq[::2]) - sum(seq[1::2])

def myzip(seq_a, seq_b):
    output = []
    for i in range(len(seq_a)):
        output.append((seq_a[i], seq_b[i]))  # [ tuple, tuple]
    print(output)


def mysum2(*elements):
    if not elements:
        print("Empty sequence!")
        return False
    output = elements[0]
    for el in elements[1:]:
        output += el
    print(output)
    return output


def mysum3(threshold, *args):
    if not args:
        print("Empty sequence")
        return False
    print(args)
    index = 0
    cut_list = []
    for i, el in enumerate(args):
        if el > threshold:
            cut_list.append(el)
    output = cut_list[0]
    for el in cut_list[1:]:
        if el > threshold:
            output += el

    print(output)
            
    
def sum_numeric(*args):
    if not args:
        print("Empty sequence")
        return False
    cut_list = []
    for el in args:
        try:
            cut_list.append(int(el))
        except ValueError as e:
            continue
    output = cut_list[0]
    for el in cut_list[1:]:
        output += el
    print(output)
def sum_numeric2(items):
    for el in items:
        try:
            total += int(el)
        except ValueError:
            pass
    return total

def dict_combine(*args):
    key_list = []
    item_list = []
    output_dict = {}
    for d in args:
        for k, v in d.items():
            if k in output_dict:
                try:
                    output_dict[k].append(v)
                except AttributeError:
                    output_dict[k] = [output_dict[k], v]
            else:
                output_dict[k] = v
    print(output_dict)
    return output_dict

import operator

def alphabetize_names(dicts: list):
    print(operator.itemgetter('last')(sorted))




#mysum3("f", "a", "c", "h", "z")


#mysum2([1,2], [3,4])
#sum_numeric("a", 1, 3, "4")

#output_dict= dict_combine({'a':3}, {'a':3,'b': 4, 'c' :5}, {'b' : 6})




PEOPLE = [
    {'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
    {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
    {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}
]

<<<<<<< HEAD
for p in sorted(PEOPLE, key = lambda x: [x['last'], x['first']]):
    print(f"{p['last']}, {p['first']}, {p['email']}")

def alphabetize_names(lists):
    return sorted(lists, key=operator.itemgetter('last','first') )

def by_vowel_count(one_word):
    total = 0
    for one_character in one_word.lower():
        if one_character in 'aeiou':
            total += 1
    return total

if __name__ == "__main__":
#    name_triangle("youngdoo")
 #   print("\n\n")
  #  pig_latin('Wine!')
   # pig_latin('Eol?')
   # pig_latin3("I have a dream")
    print(plus_minus([10,20,30]))
    myzip([10,20,30], "abc")
    alphabetize_names(PEOPLE)
#print(word_summary(["dog", "plane", "bigbig"]))
=======

from collections import Counter
import operator
from collections import namedtuple


def elementary(words):
    max = 0
    repeated_word= ""
    for w in words:
        if Counter(w).most_common(1)[0][1] > max:
            max = Counter(w).most_common(1)[0][1]
            repeated_word = w
    print(repeated_word)



words= ["this", "dream", "abaracadabra"]



person = namedtuple('Person', ['first', 'last', 'arriving_time'])

PEOPLE2 = [('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]

PEOPLE3 = []
for tup in PEOPLE2:
    PEOPLE3.append(person(tup[0], tup[1], tup[2]))



words= ["this", "dream", "abaracadabra"]

MOVIES = [('Parasite', 132, 'Bong Joon-ho'),
          ('Ford v Ferrari', 152, 'James Mangold'),
          ('The Irishman', 209, 'Martin Scorsese'),
          ('Jojo Rabbit', 108, 'Taika Waititi'),
          ('Joker', 122, 'Todd Phillips'),
          ('Little Women', 135, 'Greta Gerwig'),
          ('Marriage Story', 137, 'Noah Baumbach'),
          ('1917', 119, 'Sam Mendes'),
          ('Once Upon a Time in Hollywood', 161, 'Quentin Tarantino')
          ]

FIELDS = {'name': 0,
          'length': 1,
          'director': 2}

def sort_movie(movies):
    fields = input("Sort by what? name, length, director : ")
    fields = fields.split(',')

    f_num = []
    for f in fields:
        if f == 'name':
            f_num.append(0)
        elif f =='length':
            f_num.append(1)
        elif f == 'director':
            f_num.append(2)
    output =[]
    
    for p in sorted(movies, key=operator.itemgetter(*f_num), reverse=True):
        output.append(f"{p[0]}, {p[1]}")
    print('\n'.join(output))  

# 

def vowel_count(word):
    vowel_num = 0
    a = Counter(word)
    for w in 'aeiou':
        vowel_num += a[w]
    return vowel_num

def repeat_vowel(words):
    print(max(words, key=vowel_count))




def format_sort_records(list_of_tuples):
    template = '{last:10} {first:10} {arriving_time:5.2f}'
    output =[]
    for p in sorted(list_of_tuples, key=operator.attrgetter('last','first')):
        output.append(template.format(**(p._asdict())))
        #$        print(*(p._asdict()))
        #output.append(template.format(*(p._asdict())))
        
    return output

d = dict(sandwich = 10, tea=7)
def restaurant():
    total = 0
    while True:
        order = input("what is your order? ") 
        if not order:
            break
        elif order in d:
            total += d[order]
            print(f"{order} costs {d[order]}, total is {total}")
        else:
            print(f"{order} is not here!!")
            
    print(f"Your total is {total}")


userlist = dict(gyd123=1234, junwoo=2301)

def login_chk():
    while True:
        user = input("userID: ")
        if user not in userlist:
            print("No account information")
            continue        

        pwd = int(input("password: "))
        if pwd == userlist[user]:
            print("Successfully logged in!")
        else:
            print("Your password is wrong!")

import datetime
from datetime import timedelta

startday = datetime.datetime(year=2024, month=1, day=15)
nextday = startday + timedelta(days=1)
startday = startday.strftime("%Y%M%D") 

temp_list = {f"{startday}": 5, f"{nextday}": -2}

family_dict = dict(youngdoo = datetime.datetime(year=1982, month=2, day=5), junwoo = datetime.datetime(2023, month=1, day=17))
               
lived_days = datetime.datetime.today() - family_dict['junwoo'] 

print(lived_days.days)
               


d1 = dict(a=1,b=2, c=3)
d2 = dict(a=1, b=2, c=2)

def dictdiff(d1, d2):
    key1 = d1.keys()
    key2 = d2.keys()
    union_key = set(key1)|(set(key2))
    output = {}
    for k in union_key:
        if d1.get(k) != d2.get(k):
            output[k] = [d1.get(k), d2.get(k)]
    print(output)


def dictmerge(d1, d2):
    key1 = d1.keys()
    key2 = d2.keys()
    union_key = set(key1)|(set(key2))
    for k in union_key:
        if d2.get(k) != None:
            d1[k] = d2[k]
    print(d1)

def create_dict(*arg):
    output = {arg[i] : arg[i+1] for i in range(0, len(arg), 2)}
    print(output)

d3 = dict(a=2, b=3, c=5, d= 6)

def dict_partition(d, f):

    output1 = { k : v for k, v in d.items() if f(v) }
    output2 = { k : v for k, v in d.items() if f(v) == False }
    print("#1 : ", output1)
    print("#2 : ", output2)



def is_even(v):
    if v % 2 == 0:
        return True
    else:
        return False

file_ext = [os.path.splitext(a)[1] for a in os.listdir()]
file_ext


if __name__ == "__main__":
    #elementary(words)
    repeat_vowel(words)
    print('\n'.join(format_sort_records(PEOPLE3)))
    #sort_movie(MOVIES)
    dictdiff(d1,d2)
    dictmerge(d1, d2)
    create_dict('a',1,'b',3)
    dict_partition(d3, is_even)

