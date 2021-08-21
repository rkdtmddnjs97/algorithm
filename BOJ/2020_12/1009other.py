num = int(input())
inputs = []

for i in range(num):
    inputs.append(list(map(int, input().split())))

for i in range(num):
    result = inputs[i][0]**(inputs[i][1]%4+4) % 10
    if (result == 0):
        print(10)
    else:
        print(result)

