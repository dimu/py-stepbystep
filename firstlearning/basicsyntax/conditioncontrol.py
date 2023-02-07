# if statement

print("------------------if statement----------------------")
if 100:
    print("condition is true!")

if 100 == 200:
    print("step into if statement")
else:
    print("step into else condition")

if 100 == 200:
    print("100=200")
elif 100 == 300:
    print("100==300")
else:
    print("all is wrong!")

# while statement
print("------------------while statement----------------------")
count = 0
while count < 10:
    print("The count is:", count)
    count += 1


count = 0
while count < 10:
    print("The count is:", count)
    count += 1
else:
    print("count is greater or equal 10!")

# for statement
print("------------------for statement----------------------")
for letter in "hello":
    print("current letter is: ", letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('Current fruit :', fruit)

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print("Current fruit :", fruits[index])