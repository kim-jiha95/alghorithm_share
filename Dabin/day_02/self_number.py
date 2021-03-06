n = list(range(1,10001))
dn =[]

for i in n:
    str_i = str(i)
    list_i = list(str_i)
    int_list_i = list(map(int, list_i))
    list_sum = sum(int_list_i[0:]) + i
    dn.append(list_sum)

self = list(set(n) - set(dn))
result_list = sorted(self)
for result in result_list:
    print(result)
