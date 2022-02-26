x = int(input('x값 입력 :'))
y = int(input('y값 입력 :'))
list = []

sum = 0

for i in range(x, y):
    for j in range(2, i):
        if i%j == 0:
            sum += i
            break;
    print(sum)
