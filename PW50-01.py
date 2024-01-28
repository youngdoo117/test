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

#a= object_sum(["words", 4, 6])
#print(a)
#mysum(3,4,5)

if __name__ = "__main__":
    run_timing()

#print(word_summary(["dog", "plane", "bigbig"]))


