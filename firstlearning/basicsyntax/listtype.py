# list research


# list cmp
import operator

print("-------------list operator---------------")
list1 = ["abc", 1]
list2 = ["dfs"]
print(operator.eq(list1, list2))  # python3 没有cmp函数
print(operator.lt(list1, list2))

print(list1.index(1))

list1 = ["abc",1,"def"]
print(list1.pop())  # return def, pop: remove and return last obj from list
print(list1)