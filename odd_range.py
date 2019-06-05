l,r=map(int,input().split())
sum=0
for num in range(l,r+1):
    if(num%2!=0):
        sum=sum+num
print(sum)
