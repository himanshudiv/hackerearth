n= input()
for i in range (2, n):
    cnt=0
    for j in range(1, i):
        if(i%j==0):
            cnt+=1
    if (cnt==1):
        print i,
