import math as m

p=int(input("Enter positive"))
n=int(input("Enter negative"))
entropy = ((-p/(p+n))*m.log((p/(p+n)),2))-((n/(p+n))*m.log((n/(p+n)),2))
print(round(entropy,3))