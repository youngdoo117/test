
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


for aa in b:
    for i in range(aa):
        if aa % (i+1) == 0:
            print(i+1)
            try:
                output3[str(i+1)].append(aa)
            except KeyError:
                output3[str(i+1)] = [aa]
