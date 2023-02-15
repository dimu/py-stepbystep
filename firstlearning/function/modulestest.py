import math

print(math.pow(2,3))

total = 1
def addNum():
    global total
    total +=1

print(total)
addNum()
print(total)