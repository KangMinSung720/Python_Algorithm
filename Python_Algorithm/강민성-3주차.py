while True:
    num = input('숫자를 입력하세요 : ')
    sum = 0
    if num == '0':
        break
    for i in num:
        sum += int(i)
    print(sum)
    

    
    

