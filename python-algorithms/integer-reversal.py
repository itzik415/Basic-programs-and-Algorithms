#Integer reversal

def reverse_integer(num):
    stringNum = str(num)
    newNum = ''
    if stringNum[0] == "-":
        for i in range(len(stringNum)-1, 0, -1):
            newNum = newNum + stringNum[i]
        print(int("-" + newNum))
    else:
        for i in range(len(stringNum)-1, -1, -1):
            newNum = newNum + stringNum[i]
        print(int(newNum))
        
reverse_integer(-5)


def reverse_integer(num):
    if num == 1 or num > 1:
        print(str(num)[::-1])
    else:
        new_num = num * (-1)
        print("-" + str(new_num)[::-1])

reverse_integer(-500)
        
