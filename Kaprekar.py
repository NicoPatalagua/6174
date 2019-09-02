"""
Author: Nico Patalagua
"""
kaprekarnumbers = []
def ascending(n):
    return int(''.join(sorted(str(n))))
def descending(n):
    return int(''.join(sorted(str(n))[::-1]))
n = input("Enter a 4-digit number: ")
while True:
    print(descending(n), "-", ascending(n), "=", descending(n)-ascending(n))
    n = descending(n) - ascending(n)
    if n not in kaprekarnumbers:
        kaprekarnumbers.append(n)
    else:
        if kaprekarnumbers.index(n) == len(kaprekarnumbers)-1:
            kaprekarnumbers = []
            kaprekarnumbers.append(n)
        else:
            kaprekarnumbers = kaprekarnumbers[kaprekarnumbers.index(n):]
        break
print('Eureka!:', kaprekarnumbers)
