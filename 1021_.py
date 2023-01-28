'''
t=int(input("times"))#횟수
tot=0
i=0
while (i<t):
    x=int(input(":"))
    if x<0:
        x=0                       #x가 음수이면 x는 0으로 처리
    tot+=x
    i=i+1                        #step
print(tot)

t=int(input("times")) #횟수
i=0
tot=0
while (i<t):
    x=int(input(":"))
    if x<0:                     #x가 음수일 때 no count, no plus=i가 카운트 역할, x는 플러스 
        i=i+0
        x=0
    else:
        i=i+1
    tot+=x
print(tot)

#위를 간단하게 정리하면 이렇게
t=int(input("times")) #횟수
i=0
tot=0
while (i<t):
    x=int(input(":"))
    if x>0:
        i=i+1
        tot+=x
print(tot)

f=int(input("factorial"))
tot=1
i=0
while (i<f):
    i=i+1                           #i가 1씩 증가
    tot=tot*i                   
print(tot)

n=int(input("number"))
i=0
while (i<n):
    x=int(input(":"))

n=int(input("number"))
x=int(input(":"))
bg=0
sm=0
for i in range(0,x,1):
    z=int(input(":"))
    if z>n:
        bg+=1
    elif z<n:
        sm+=1
print(n,"보다 큰 수:",bg,"개\n", n,"보다 작은 수:",sm,"개")

n=int(input("n"))
i=0
mx=0
mn=0
while (i<n):
    x=int(input("x"))
    if x>mx:
        mx=x
    elif x<mx:
           mn=x 
    i=i+1    
print("이 중 최대는",mx,"이며 최소는",mn,"이다")
'''        
        



