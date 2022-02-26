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
