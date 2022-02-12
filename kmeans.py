from math import *
l,m,d,c=[],[],[],[]
n=int(input("enter the no of points"))
'''for i in range(0,n):
    temp=[]
    x=int(input("enter x value"))
    y=int(input("enter y value"))
    temp=[x,y]
    l.append(temp)'''

#l=[[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
l=[[1,1],[1.5,2],[3,4],[5,7],[3.5,5],[4.5,5],[3.5,4.5]]
print(l)

#change1
for i in range(0,3):
    temp=[]
    x=float(input("enter x value"))
    y=float(input("enter y value"))
    temp=[x,y]
    m.append(temp)
print(m)

for i in range(0,n):
    temp=[]
    #change2
    for j in range(0,3):
        tvalue1=(m[j][0]-l[i][0])
        tvalue2=(m[j][1]-l[i][1])
        if(tvalue1<0):
            tvalue1=-tvalue1
        if(tvalue2<0):
            tvalue2=-tvalue2
        temp.append(tvalue1+tvalue2)

    print(temp)    #print all the values in the table except cluster
    temp1=min(temp[0],temp[1],temp[2]) #change3 add temp[3] in case or delete any one from it.
    if(temp1==temp[0]):
        c.append(1)
    elif(temp1==temp[1]):
        c.append(2)
    else:
        c.append(3)
        
print(c)  #print cluster values
mean1x,mean1y,mean2x,mean2y,mean3x,mean3y,m1,m2,m3=0,0,0,0,0,0,0,0,0   #change4
for i in range(0,n):
    if(c[i]==1):
        mean1x+=l[i][0]
        mean1y+=l[i][1]
        m1+=1
    elif(c[i]==2):
        mean2x+=l[i][0]
        mean2y+=l[i][1]
        m2+=1
    else:
        mean3x+=l[i][0]
        mean3y+=l[i][1]
        m3+=1
#change5
mean1x=mean1x/m1
mean1y=mean1y/m1
mean2x=mean2x/m2
mean2y=mean2y/m2
mean3x=mean3x/m3
mean3y=mean3y/m3
print(mean1x,mean1y)
print(mean2x,mean2y)
print(mean3x,mean3y) #printing mean values