#Avg Information Entropy
t=int(input("Enter no of divisions"))
oe=float(input("Enter Entropy"))
pt=int(input("Enter total positive"))
nt=int(input("Enter total negative"))
sum=0
for i in range(0,t):
    p=int(input("Enter positive"))
    n=int(input("Enter negative"))
    entropy=float(input("Enter entropy"))
    sum=sum+((p+n)/(pt+nt))*entropy
print("Avg Information Entropy : ",round(sum,3))
gain=oe-round(sum,3)
print("Gain :",gain)
