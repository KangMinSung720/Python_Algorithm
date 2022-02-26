#과제1 : 현재 상황에서는 동영상강의파일 다운로드 해서 하는 수업이 좋은 것 같습니다.

#과제2 : 사용자로부터 3개의 숫자를 받아서 평균과 합을 계산하고 결과를 출력하는 프로그램(변수 사용할 것)
x = int(input("첫 번째 정수 입력 : "))
y = int(input("두 번째 정수 입력 : "))
z = int(input("세 번째 정수 입력 : "))
sum = x + y + z
avg = sum/3
print(x, "와 ", y, "와 ", z, "의 합은 ", sum, "이고 평균 값은 ", avg)

#과제3 : 터들그래픽을 이용하여 그림을 화면에 출력하는 프로그램
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

t.rt(90)
t.fd(50)
t.rt(90)
t.fd(100)

t.rt(90)
t.fd(50)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(100)

#과제4 : 다각형 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

shape = int(input("몇 각형을 그리나요? : "))

if shape == 3:
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)

if shape == 4:
    t.fd(100)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(100)

if shape == 5:
    t.lt(72)
    t.fd(100)
    t.lt(72)
    t.fd(100)
    t.lt(72)
    t.fd(100)
    t.lt(72)
    t.fd(100)
    t.lt(72)
    t.fd(100)

if shape == 6:
    t.fd(100)
    t.rt(60)
    t.fd(100)
    t.rt(60)
    t.fd(100)

#과제5 : 자동 판매기 프로그램
x = int(input("투입한 돈 : "))
y = int(input("물건 값 : "))
z = x - y

n500 = z//500
n100 = (z%500)//100
n50 = (z%100)//50
n10 = (z%50)//10

print("거스름돈 : ", z)
print("500원 : ", n500)
print("100원 : ", n100)
print("50원 : ", n50)
print("10원 : ", n10)

