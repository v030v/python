#변수는 X띄어쓰기, 숫자로 시작, 특수문자X/_는 가능
# for i in range():
#()=(stop)-0부터 1step씩 stop 직전까지 증가,(start,stop,step)- start로 시작해 step만큼 증가, stop전에 멈춤
'''
for i in range (5):
    print("사랑해 민우야")
#i="사랑해민우야"라고 했을 시, for i in range():에서 i말고 다른 변수 입력해줘야 print(i)했을 때 원하는 값 나옴
다른 변수를 입력하지 않았을 시 0부터 stop전 값까지 나옴

i=3

for i in range(1,10,1):
    print("3*",i,"=",3*i)

n=int(input("n"))

for i in range (1,10,1):
    print(n,"*",i,"=",n*i)

m=int(input("multiple")) #m은 배수다 임마
st=int(input("start"))#st는 스타트 난 노예
end=int(input("end"))#end 끝내라 임마

for i in range(st,end+1,1):
    print(m*i)
'''
#1. (start, stop, step)-start에서 시작해 stop 직전까지 step씩 반복
for i in range(0, 10, 1):
    print(i)

#2.(stop)-0에서 시작해 1step씩 stop 전까지 반복
for i in range(10):
    print(i)

#3. i는 0에서 30까지 반복->if i가 30일 때 출력, 두개 더해져 30 두번 출

for i in range(31):
    if i == 30 :
        print(i)
        
    print(i)

#4. for=i 0~30까지 반복해, if=i가 30이면 출력해, else=그 외에 출력해=>for은 출력 없으므로 0~30까지 출
    
for i in range(31):
    if i == 30 :
        print(i)
    else :        
        print(i)

#5. i는 30이야, for=k는 0~30까지 반복, if=i가 30이면 출력->i가 30이니까 30번 반복,k는 출력하지 않아서 출력안됨 
   
i = 30

for k in range(0, 30, 1):
    if i == 30 :
        print(i)

#6. k를 0부터 9까지 5씩 출력

for k in range(0, 10, 5):
    print(k)

#7. start가 30부터인데 10 전에서 stop이니까 출력X 
for k in range(30, 10, 5):
    print(k)

#8. for=j를 1부터 9까지 1씩 반복, i에 j를 곱해서 출력=구구단
 
i = 3

for j in range(1, 10, 1):
    print(i, "*", j, "=",i * j)

#9. i를 입력, for=j를 1부터 9까지 1씩 반복, i입력값*j 출력=입력한 수의 구구단 출력

i = int(input(":"))

for j in range(1, 10, 1):
    print(i, "*", j, "=",i * j)






