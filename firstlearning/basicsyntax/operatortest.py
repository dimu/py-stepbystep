# this chapter is about basic operators

print("----------arithmetic operators--------------")
a = 21
b = 10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(2 ** 3)  # 次方
print(5 // 2)  # floor除法，去掉小数位
print(11 // 3)

print("----------comparison operators--------------")
print(1 > 2)
print(1 != 2)
print(1 == 2)
print(1 <= 2)
print(1 >= 2)

print("----------assignment operators--------------")
c = 10
c *= 2
print(c)
c += 10
print(c)

print("----------bitwise operators--------------")

print("----------logical operators--------------")
print(10 and 20)
if 10 and 20:
    print("true")
print(10 or 0)
print("false" or 0)
print(not (10 and 20))

print("----------memberships operators--------------")
a = [1, 2, 3, 4, 5]
print(1 in a)
print(15 in a)
print(1 not in a)
print(15 not in a)
