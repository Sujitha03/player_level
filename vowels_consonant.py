n=input()
d=[]
a=[]
c=["a","e","i","o","u"]
for x in n:
    if x in c:
        d.append(x)
    else:
        a.append(x)
print(*(d+a),end='')
