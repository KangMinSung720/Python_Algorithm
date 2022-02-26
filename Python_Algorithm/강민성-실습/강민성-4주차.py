#6개의 원 그리기(리스트, 함수 넣기 전)
import turtle as t

for count in range(6):
    t.circle(100)
    t.left(60)

#6개의 원 그리기에서 사이즈 값 받고 색상 넣어서 그리기(리스트, 함수 넣은 후)    
import turtle as t
t.shape("turtle")

color_list = ["yellow","red","blue","green","black","pink"] #색상값 리스트

def drawCircle(size): #원을 그리는 함수
    for i in color_list:
        t.fillcolor(i)
        t.begin_fill()
        t.circle(size)
        t.end_fill()
        t.left(60)

x = int(input("원의 크기:")) #인수값 받기
drawCircle(x) #인수값 넘겨서 원 그리기
