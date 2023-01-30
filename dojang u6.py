'''
a, b = input('문자열을 두 개 입력하세요').split() #input에 값 여러개 나눠줘 공백기준!
print (a)
print (b)

a , b = input('문자열').split()
a=int(a) 
b=int(b)
print(a+b) #or print(int(a)+int(b))

a,b= map(int, input('문자열').split()) #map 사용하면 input.split을 한번에 int로 전환 가능
print(a+b)

a,b,c=map(int, input('숫자를 입력').split())
print(a+b+c)
'''
a,b,c,d=map(int, input().split())
print((a+b+c+d)//4)

print(a,b, sep='') #값 사이 공백 아닌 다른 문자를 사용하고 싶을 시 sep 사용,end=''는 바로 뒤에 다음 값 옴