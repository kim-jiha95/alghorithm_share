a = str(input())
a_list = list(a)
cro = ['dz=','c=','c-','d-','lj','nj','s=','z=']
for i in cro :
    if i in a :
        a = a.replace(i, 'a')
alphabet = list(a)
result = len(alphabet)
print(result)
