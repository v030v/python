'''
f=int(input("factorial")) #f는 팩토리얼
tot=1
for i in range(1,f+1):
    tot=tot*i
    if i==f:
        print(tot)

f=int(input("factorial")) #f는 팩토리얼
tot=1
for i in range(1,f+1):
    tot=tot*i
print(tot) #print 위치에 따라 결과값 달라짐 정렬중요 

while (true) : #괄호는 조건=참일 때만 실행, for와 달리 변수 및 조건을 디테일하게 생각 필요

#두개는 같은 값 도출, 그러나 for는 반복횟수 직접 제시, while은 조건에 따른 반복 실행이 이뤄짐
i=0
while (i<5):
    print(i)
    i=i+1

for i in range(5):
    print(i)

n=int(input("number"))
m=0
while (m<n): #m은 start,n은 end 값 느낌
    print("사랑해민우야")
    m+=1 #step 값 느낌

i=1
n=int(input("number"))
while (i<10):
    print(i,"*",n,"=",i*n)
    i=i+1

i=1
n=int(input("number"))
while (i<=n):
    if (i%7==0): #7의 배수는 7로 나눴을 때 나머지가 0
        print(i)
    i=i+1    

i=1
n=int(input("number"))
while (i<=n):
    if(n%i==0):
        print(i)
    i=i+1

i=1
n1=int(input("number1"))
n2=int(input("number2"))
if n1<n2:
    while(i<=n2):
        if(n1%i==0)and(n2%i==0):
            print(i)
        i=i+1
else :
    while(i<=n1):
        if(n1%i==0)and(n2%i==0):
            print(i)
        i=i+1

#sm이라는 변수를 이용해 더 간략
i=1
n1=int(input("number1"))
n2=int(input("number2"))

if (n1<n2):
    sm=n1
else:
    sm=n2
while(i<=sm):
        if(n1%i==0)and(n2%i==0):
            print(i)
        i=i+1
'''
