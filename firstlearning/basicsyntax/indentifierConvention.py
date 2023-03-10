# ptyhon  is a case sensitive programming language, class name start with an uppercase letter, underscore indentifier
# is private

import sys
import getopt

if 1 == 2:
    print('oh,no')
else:
    print("yes")

# get cmd line args
print(sys.argv)
print(len(sys.argv))

a = b = c = 1
c = 2
print(a)
print(b)
print(c)

# python string
str1 = "hello world!"
print(str1)
print(str1[0])
print(str1[2:5])
print(str1[2:])
print(str1 * 2)
print(str1 + "yummy")

# python list like c array, can hold different type value
list1 = ["abc", 123, "xdf", ("def", 66, "ou")]
print(list1)
print(list1[0])
print(list1[2:])
print(list1[3][2])
print(list1 * 2)
print(list1 + ["ok", 222])

# python tuple, can't update value
tupletest = ("abc", 123, "cdf")
print("--------------------tupletest----------------")
print(tupletest)
print(tupletest[0])
print(tupletest[1:])
print(tupletest * 2)
# can't concatenate
# print(tupletest + [133])
# can't updata tuple value
# tupletest[0] = 'ddd'
# print(tupletest)

# python data type conversion
print("---------------------data type conversion-------------------")
print(int('123') + 123)
print(chr(0x61))  # 将数值转换为对应的字符形式
print(ord('c'))  # 将字符对应的证书值显示出来
print(hex(97))  # 将整形转换成对应的十六进制字符串形式
print(dict({"name": "dwx", "age": 24}))  # 将对象转换为字典类型
print(tuple(("abc", 123)))
