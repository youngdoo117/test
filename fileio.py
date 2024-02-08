
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


dict_csv(d1)

