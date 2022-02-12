#python 3.7.1

from math import *
l,m,d,c1,c2,c3=[],[],[],[],[],[]
e=1.9

mpt=4

n=int(input("enter the no of points"))

l=[[7,4],[6,4],[5,6],[4,2],[6,3],[5,2],[3,3],[4,5],[6,5],[3,6],[4,4],[8,2]]
print(l)
final=[]
for i in range(0,n):
    temp=[]
    for j in range(0,n):
        temp1=sqrt((l[j][0]-l[i][0])**2  +  (l[j][1]-l[i][1])**2)
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