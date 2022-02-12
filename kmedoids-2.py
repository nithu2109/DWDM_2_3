from math import *
l,m,d,c1,c2,c3=[],[],[],[],[],[]
n=int(input("enter the no of points"))
'''for i in range(0,n):
    temp=[]
    x=int(input("enter x value"))
    y=int(input("enter y value"))
    temp=[x,y]
    l.append(temp)'''
#l=[[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
l=[[7,6],[2,6],[3,8],[8,5],[7,4],[4,7],[6,2],[7,3],[6,4],[3,4]]
#l=[[8, 7], [3, 7], [4, 9], [9, 6], [8, 5], [5, 8], [7, 3], [8, 4], [7, 5], [4, 5]]
print(l)
for i in range(0,2):
    temp=[]
    x=float(input("enter x value"))
    y=float(input("enter y value"))
    temp=[x,y]
    m.append(temp)
print(m)

for i in range(0,n):
    temp=[]
    #type2
    for j in range(0,2):
        tvalue1=(m[j][0]-l[i][0])
        tvalue2=(m[j][1]-l[i][1])
        if(tvalue1<0):
            tvalue1=-tvalue1
        if(tvalue2<0):
            tvalue2=-tvalue2
        temp.append(tvalue1+tvalue2)

    print(i,temp)    
    temp1=min(temp[0],temp[1])         
    if(temp1==temp[0]):
        c1.append(temp1)
    else:
        c2.append(temp1)
        
print(c1)
print(c2)
print(sum(c1) + sum(c2))


    #type1
''' for j in range(0,2):
        temp.append(sqrt((m[j][0]-l[i][0])*2  +  (m[j][1]-l[i][1])*2))
        '''