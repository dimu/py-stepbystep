def sum1(a, b):
    """add function"""  # function doc string place
    print("step into function!")
    return a + b


print(sum1(1, 2))

# all function parameter are passed by reference
def parameterbyreference(list):
    list[0]="change me"
    return list

print(parameterbyreference([123,345,22]))
