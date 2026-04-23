def numbDig(n1):
    count=0
    while (n1!=0):
        rem=n1%10
        n1=n1//10
        count+=1
    return count

st=int(input("Enter start: "))
so=int(input("Enter stop: "))
for i in range(st,so):
    k=i
    n=numbDig(i) # to find digits
    sum=0
    while(k!=0):
        rem=k%10
        k=k//10
        sum=sum+(rem**n)
    
    if(i==sum):
        print(i)
