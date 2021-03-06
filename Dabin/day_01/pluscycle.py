a = int(input()) # 26
n = a
num = 0 # 1
while True :
    num += 1
    if a < 10 :
        a_set = '0' + str(a) 
        b_set = int(a_set)
        c_set = str(a % 10) + str(b_set % 10)
        a = int(c_set)
    else :
        a_set = str((a // 10) + (a % 10))
        b_set = int(a_set) % 10
        c_set = str(a % 10) + str(b_set)
        a = int(c_set)
    if a == n :
        print(num)
        break

        
