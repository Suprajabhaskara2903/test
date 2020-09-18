from collections import Counter
n=int(input("enter no shoes"))
l=Counter(map(int,input("enter shoe sozes").split()))
k=int(input("noof pairs"))
s=0
for i in range(k):
	l1=list(map(int,input("enter size and cost").split()))
	if l[l1[0]]:
		s=s+l1[1]
		l[l1[0]]-=1
print(s)

