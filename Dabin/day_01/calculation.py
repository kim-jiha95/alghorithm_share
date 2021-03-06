# 사칙연산

def sum (a,b) :
    return a+b

def substract (a,b) :
    return a-b

def multiply (a,b) :
    return a*b

def division (a,b) :
    return a//b

def remainder (a,b) :
    return a%b

a = int(input('first number : '))
b = int(input('second number : '))

if 1 <= a <= 10000 and 1 <= b <= 10000 :
    sum = sum (a, b)
    substract = substract (a, b)
    multiply = multiply (a, b)
    division = division (a, b)
    remainder = remainder (a, b)
    print(sum)
    print(substract)
    print(multiply)
    print(division)
    print(remainder)
else :
    print('벗어난 범위 입니다.')

