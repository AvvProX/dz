n=int(input())
x=n//2 + 1
s=0
for i in range(1,x):
    if n%i==0:
        s=s+1
    if s>1 :
        break
if s == 1:
    print('YES')
else:
    print('NO')