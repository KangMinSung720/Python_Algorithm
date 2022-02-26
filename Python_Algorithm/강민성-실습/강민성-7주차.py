#출석과제 : 피보나치 수열을 재귀함수로 코딩하기
#재귀함수란 함수 안에서 자기 자신을 호출하는 것

n = int(input('숫자입력 : ')) #수 입력 받기

def fib(n): #
     if n == 1 or n == 2: # n입력값이 1 또는 2일때 1 리턴 
        return 1
     return fib(n-1) + fib(n-2) #피보나치 수열 점화식

print(fib(n))

#실습평가 : 재귀호출형식 알고리즘

#재귀 함수를 사용하지 않고 단순 반복문으로 구현한 팩토리얼
n = int(input('숫자입력 : ')) 

def fac(n):
    num = 1
    for i in range(1, n+1): #반복문
        num *= i
    return num

print(fac(n))

#재귀 함수를 사용하여 구현한 팩토리얼
n = int(input('숫자입력 : ')) 

def fac(n):
    if n==1: # 입력값 1일 경우 1 리턴
        return 1;
    else:
        return n*fac(n-1) # 재귀호출(함수 안에서 자기 자신을 호출)

print(fac(n))
