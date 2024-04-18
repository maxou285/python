n=2
count=0
while True:
    for x in range(2,n):
        if n%x==0:
            break
    else:  
        count=count+1
    if count==10001:
        print(n)
        break
    n=n+1    
        