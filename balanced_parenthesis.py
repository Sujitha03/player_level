n=input()
k=0
l=0
for x in n:
    if(x=='('):
        k=k+1
    elif(x==')'):
        l=l+1
if(k==l):
    print('yes')
else:
    print('no')
