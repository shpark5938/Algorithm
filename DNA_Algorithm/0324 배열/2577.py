a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)

for i in range(0, 10):
    arr = mul.count(str(i))
    print(arr)