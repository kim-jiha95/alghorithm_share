a = str(input())
list_data = (list(a.upper()))
upper_a = list(set(a.upper()))
result = dict()
final = []
for i in upper_a:
    result[i] = list_data.count(i)
    
result_max = max(result.values())
for key, value in result.items():
    if value == result_max:
        final.append(key)
if len(final) > 1 :
    print('?')
else :
    real_final = str(final[0])
    print(real_final)
