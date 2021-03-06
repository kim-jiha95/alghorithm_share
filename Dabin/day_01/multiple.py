def multiple (a,b):
    return a*b
    
a = int(input('first number:'))
b_list = list(input('second number'))

b1 = int(b_list[-1])
b2 = int(b_list[-2])
b3 = int(b_list[-3])

b_str = str(b3) + str(b2) + str(b1)
b = int(b_str)

multiple3 = multiple(a,b1)
multiple4 = multiple(a,b2)
multiple5 = multiple(a,b3)
multiple6 = multiple(a,b)

print(multiple3)
print(multiple4)
print(multiple5)
print(multiple6)


