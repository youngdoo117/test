
sum = 0

for current_line in open('d:/sample.txt', encoding='utf-8'):
    for w in current_line.split():
        if w.isdigit():
            print(w)
            sum += int(w)


print(sum, "\n\n")
            
            
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]

        

c1 = 0
c2 = 0
result = 0

for current_line in open('d:/sample3.txt', encoding='utf-8'):
    try:
        numbers = [int(a) for a in current_line.split()]
        result += numbers[0] * numbers[1]
    except ValueError:
        
        pass
    
print(result)    
            

count = 0 

vowel_output = {}

for current_line in open('d:/sample.txt', encoding='utf-8'):
    for w in current_line.split():
        for c in w:
            if c.lower() in "aeiou":
                
                vowel_output[c] = vowel_output.get(c, 0)
                vowel_output[c] += 1


print("\n", vowel_output, "\n\n")


for i in open("d:/text/passwd.txt"):
    if not i.startswith(("#", "\n")):
        infos = i.split(":")
        output[infos[-1]] = infos[0]

for i in open("d:/text/passwd.txt"):
    if not i.startswith(("#", "\n")):
        infos = i.split(":")
        try:
            output[infos[-1]].append(infos[0])
        except AttributeError:
            output[infos[-1]] = [infos[0]]

for i in open("d:/text/passwd.txt"):
    if not i.startswith(("#", "\n")):
        infos = i.split(":")
        output2[infos[0]] = {"userid": infos[2], "homedir": infos[-2], "shell": infos[-1]}

b = [1,2,6,8,10,14,15]

for aa in b:
    for i in range(aa):
        if aa % (i+1) == 0:
            print(i+1)
            try:
                output3[str(i+1)].append(aa)
            except KeyError:
                output3[str(i+1)] = [aa]

for aa in b:
    for i in range(aa):
        if aa % (i+1) == 0:
            print(i+1)
            if output3.get(str(i+1)):
                output3[str(i+1)].append(aa) 
            else:
                output3[str(i+1)] = [aa]



import glob
a = glob.glob("d:/texts")
for f in a:
    filestat[os.path.basename(f)] = os.stat(f).st_size

for f in a:
    for line in open(f, encoding="utf-8"):
        for w in line.split():
            if w[-1] in ",.;:?!":
                w = w[:-1]
            if word_count.get(w.lower()):
                word_count[w.lower()] += 1
            else:
                word_count[w.lower()] = 1


Counter(word_count).most_common(5)



import csv

def password_csv(f1, f2=0):

    with open('d:/password.csv', 'w') as f, open('d:/passwd.txt', 'r') as g:
        r = csv.reader(g, delimiter=':')
        o = csv.writer(f, delimiter=',')
        for record in r:
            if len(record) > 1:
                o.writerow((record[0], record[2]))
##        for line in open(f1, encoding='utf-8'):
##            if not (line.startswith('#')):
##                line = line.split(':')
##                o.writerow((line[0], line[2]))


def password_csv2():
    fields = input("Select field numbers : ")
    print(fields)
    fields = [int(i) for i in fields.split()]
    delimiter = input("Select delimiter : ")
    with open('d:/password2.csv', 'w') as f, open('d:/passwd.txt', 'r') as g:
        r= csv.reader(g, delimiter=':')
        o = csv.writer(f, delimiter=delimiter)
        for record in r:
            if len(record) > 1:
                o.writerow((record[i] for i in fields))


#password_csv2()


def dict_csv(d):
    with open('d:/dict_csv.csv','w') as f:
        o = csv.writer(f, delimiter=":")
        o.writerow((k, v, type(v)) for k, v in d.items())
    
d1 = dict(a=1, b=2, c=33, d=44)



import json
import glob

def print_scores(dirname):
    scores = {}

    for fn in glob.glob(f"d:/{dirname}/*.json"):
        scores[fn] = {}

        with open(fn) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[fn].setdefault(subject, [])
                    scores[fn][subject].append(score)

    print(scores)
    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)

            print(subject)
            print(f"\tmin {min_score}")


print_scores("python")

            



dict_csv(d1)




import csv
import json
import glob

import os 

with open('d:/text/passwd.txt') as f, open("d:/text/pass.json", "w") as output:
    a = csv.reader(f, delimiter =':')
    for line in a:
        if len(line) > 1:
            print(line)
            bb = line
            aa = dict(username=bb[0], password=bb[2], shell=bb[-2], userdir=bb[-1])
            json.dump(aa, output)



            
with open("d:/text/fileinfo.json", "w") as f:
    for aa in glob.glob("d:/cinema/*.*"):
        stat_result = os.stat(aa)
        stat_dict = dict((key, getattr(stat_result, key)) for key in dir(stat_result) if key.startswith('st_'))
        print(stat_dict)
        json.dump(stat_dict, f)


dd = dict((key, getattr(aa, key)) for key in dir(aa) if key.startswith("st_"))




def reverse_lines(infile, outfile):
    with open(infile, "r") as input_file, open(outfile, "w") as output_file:
        for line in input_file:
            output_file.write(f"{line.rstrip()[::-1]}\n")

reverse_lines("d:/text/passwd.txt", "d:/text/rev.text")



def myxml(tagname, content="", **kwargs):
    attrs = ''.join([f""""{k}="{v}" """ for k, v in kwargs.items()])
    return f"<{tagname} {attrs}>{content}</{tagname}>"

print(myxml("foo", "hello", a=1, b=2))


import shutil
import os
from pathlib import Path 

def copyfile(source_file, *args):
    base = Path(source_file).parent
    dest_files = [Path(base, fn) for fn in args]
    for df in dest_files:
        shutil.copyfile(source_file, df)


copyfile("d:/text/passwd.txt", "b1.txt", "c1.txt")

    
def num_factorial(*args):
    output = 1
    for i in args:
        output *= i
    print(output)

num_factorial(1, 4, 5)

def anyjoin(seq, glue=" "):
    seq2 = [str(i) for i in seq]
    print(glue.join(seq2))

anyjoin([1,2,3], glue=":")


import operator
import random

def calc_func():
    op_dict = {
        '+': operator.add, '-': operator.sub, '*': operator.mul,
        '/': operator.truediv, '**': operator.pow, '%': operator.mod}
    user_input = input("What to calculate? ")
    op, *numstr = user_input.split()
    num = [ float(i) for i in numstr]
    print(num)
    output = num[0]        
    for i, _ in enumerate(num):
        if i + 1 >= len(num):
            break
        output = op_dict[op](output, num[i+1])
    print(output)



def add_one(i):
    try:
        return int(i) + 1
    except ValueError:

        return i + " "
    

def apply_to_each(func, seq):
    result = [func(el) for el in seq]

    print(result)

def apply_to_eachline(func, infile, outfile):
    with open(infile, "r") as f1, open(outfile, "w") as f2:
        for line in f1.read():
            f2.write(str(func(line)))

def create_pwd_generator(chs):
    def func(a: int):
        output = []
        for i in range(a):
            output.append(random.choice(chs))
        print(''.join(output))
    return func
def create_pwd_checker(min_uppercase, min_digits):
    def func(pwd):
        uppercase = 0
        digit = 0 
        for ch in pwd:
            if ch.isupper():
                uppercase += 1
                print("upper")
            if ch.isdigit():
                digit += 1
                print("digit")
        if uppercase >= min_uppercase and digit >= min_digits:
            print(f"Ok!! {uppercase}   {digit}")
            return True
    return func

def getitem(index):
    def f(seq):
        print(seq[index])
    return f

def doboth(f1,f2):
    def f(x):
        return f1(f2(x))
    return f

apply_to_eachline(add_one, "d:/text/passwd.txt", "d:/text/aaww.txt")

alpha_password = create_pwd_generator("abcde*&^")
alpha_password(21)
aa = create_pwd_checker(2, 2)
print(aa("A111"))
print(aa("BBb1111"))


d1 = {'a': 1, 'b': 3}

getter = getitem('b')
getter(d1)

def f1(a):
    return a + 2

def f2(b):
    return b * 5


doboth_func = doboth(f1, f2)
print(doboth_func(3))



##
##
##with open("d:/sample.txt", encoding="utf-8") as f:
##    for line in f:
##        print(' '.join([i for i in  reversed(line.split())]))
##        

user_input = input("Enter number : ")
user_input = user_input.split()

print(sum(int(i) for i
          in user_input
          if i.isdigit())
      )


def contain_wvxyz(line):
    chk_ch = "q"
    return any(char in chk_ch for char in line)
      
with open("d:/sample.txt", encoding="utf-8") as f:
    print([line for line in f
           if len(line) > 40 and contain_wvxyz(line)])

def inc_areacode(telnum):
    if int(telnum[4]) <= 5:
        return f"{telnum[:2]}{int(telnum[2])+1}{telnum[3:]}"
    else:
        return telnum

def increment_area_code(telnum):
    area_code, phone_number = telnum.split('-', 1)
    if phone_number[0] in '012345':
        area_code = str(int(area_code) + 1)

    return f'{area_code}-{phone_number}'
    
tel = ['123-456-7890', '123-333-4444', '123-777-8888']
name = ['chusoo', 'suni', 'younghee', 'minkwon']
age = [ 30, 18, 24, 17]
print([increment_area_code(t) for t in tel])
persons_edited = [{'name': a, 'age' : b, 'age_in_month': b*12}
                  for a, b in zip(name,age)
                  if b > 20
                  ]

persons = [{'name': a, 'age' : b} for a, b in zip(name, age)]

def age_in_months(mylist):
    return [dict(**one_person, age_in_months=one_person['age'] * 12)
            for one_person in mylist
            if one_person['age'] <= 20]

for i in persons:
    print("{name} is {age} years old".format(**i))

print(age_in_months(persons))


def odd_num(a):
    try:
        if int(a) % 2 != 0:
            return True
    except ValueError:
        return False
blist = [[10, 21, "33"], ["40e", 17], [44, 67]]
print([int(one_element) for sublist in blist for one_element in sublist
       if str(one_element).isdigit() and int(one_element) % 2 != 0])


family = {'A':['B', 'C', 'D'], 'E':['F', 'G']}
import random

b = [dict(name=child, age=random.randint(10,30))
            for parent in family.values() for child in parent]

import operator
print([onechild
       for onechild in sorted(b, key=operator.itemgetter('age'), reverse=True)])





def piglatin(word):
    if word[0].lower() in "aeiou":
        return f"{word[0:]}way"
    else:
        return f"{word[1:]}{word[0]}ay"
    
    
def plword_file(file):
    return ' '.join(piglatin(word)
                    for line in open(file, encoding='utf-8')
                    for word in line.split())
if __name__ == "__main__":
    print(plword_file("d:/text/sample.txt"))
    
d = {'a':1, 'b':2, 'c':3, 'd': 4}


def transform_values(d, func, filter_func):
    return {k : func(value) for k, value in d.items() if filter_func(k, value)}

def filter_func(k, value):
    if k == 'a' or value % 2 == 0:
        return True


def idpwd_dict(file):
    d = {line.split(':')[0] : line.split(':')[2]
         for line in open(file, encoding='utf-8')
         if not line.startswith('#')}

    f = { line.split(':')[-1]
         for line in open(file, encoding='utf-8')
         if not line.startswith('#')}
    print("# of distinct shells :", len(f))
    print(d)

        
import glob
import os

def dir_dict(path):
    d = {os.path.basename(file): os.stat(file).st_size
         for file in glob.glob(os.path.join(path, '*.*'))
         if os.path.isfile(file)
         }
    print(d)

dir_dict('d:/')

print(transform_values(d, lambda x: x*x, filter_func))

idpwd_dict('d:/passwd.txt')

def volcanic():
    vowel = set('aeiou')
    b = { word.strip() for word in open('d:/words.txt', encoding='utf-8') if vowel < set(word)}
    print(b)

# volcanic()

def diff_words(file):
    d = {word
        for line in open(file, encoding='utf-8')
        for word in line.split()}
    w_length = {len(word) for word in d}
    print(w_length)
    

diff_words('d:/sample.txt')

family = {'youngdoo', 'hyomi', 'junwoo', 'hyeonok'}
def ch_family(family):
    d = {ch for name in family
         for ch in name}
    print(d)

ch_family(family)


import string

g1 = {c : index for index, c in enumerate(string.ascii_lowercase, 1)}

def gamatria(word):
    return sum(g1.get(c, 0) for c in word)

gamatria("abc")

def gematria_equal(word):
    val = gamatria(word)
    output = [word.strip() for word in open("d:/words.txt", encoding="utf-8")
              if gamatria(word.lower().strip()) == val]
    print(output)
    print(gamatria('aubusson'), gamatria('vulnerable'), '####')

gematria_equal('vulnerable')
d = [dict(user=line.split('=')[0], preference=line.split('=')[1])
     for line in open('d:/config.txt', encoding='utf-8')
     if line.split('=')[1].strip().isdigit()]


import json
with open('d:/cities.json', encoding='utf-8') as f:
    b = json.load(f)

c = {(city['state'], city['city']) : city['population'] for city in b}
        
