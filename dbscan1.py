from math import *
l,m,d,c1,c2,c3=[],[],[],[],[],[]
e=1.9
mpt=4

n=int(input("enter the no of points"))

l=[1,2,2,2,2,2,6,8,10,12,14]
print(l)
final=[]
for i in range(0,n):
    temp=[]
    for j in range(0,n):
        temp1=sqrt((l[j]-l[i])**2)
        temp1=round(temp1,2)
        temp.append(temp1)
    print(i,temp)
    final.append(temp)


for i in range(0,n):
    count=0
    for j in range(0,n):
        if (final[j][i] <=e):
            count=count+1
    if(count >=mpt):
        print(count,"---",i+1," is an core point")
    else:
        print(count,"---",i+1," is an outlier")