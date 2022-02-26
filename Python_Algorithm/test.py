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
