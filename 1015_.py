'''
#3의 배수가 100보다 적을때 출력
for i in range(1,101,1):
    if 3*i<100:
        print("3*",i,"=",3*i)

#내가 푼거/15*i가 100보다 작으면 출력
for i in range(1,101,1):
    if 3*5*i<100:
            print(3*5*i)

#민우의도, i나누기 3,5했을 때 나머지가 0이면 출력
for i in range (1,101,1):
    if i%3==0 and i%5==0:
        print(i)

for i in range (9,0,-1):
    print(3*i)


#tot 값이 0이어야 1부터 시작가능
tot=0
for i in range(1,101,1):
    tot=tot+i
print(tot)

st=int(input("start")) #st는 시작값
end=int(input("end"))#end는 마지막 값
tot=0
for i in range(st,end+1,1):
    tot=tot+i
print(tot)

L=int(input("minwoo"))
for i in range(L):
    print("민우야 사랑해")

#input은 즉각활용 혹은 변수에 담아 바로 출력, int(input(""))=input 형변환 int로
tot=0
n=int(input("number")) #반복 횟수
for i in range(n):
    tot=tot+int(input(":"))
print(tot)

tot=0
n=int(input("number")) #반복 횟수
for i in range(n):
    x=int(input(":"))
    tot=tot+x
print(tot)
'''
