str = input("enter your input:")
print("receive str is :", str)

testfile = open("text.txt", "w")
testfile.writelines("I'm dwx, \nI'm four years old now!")
# must close the file stream
testfile.close()

testb = open("text.txt", "ab")
# python 3.5以上必须用encode以及decode进行byte转换，以前版本直接使用
testb.write("ssd".encode(encoding='utf-8'))
testb.close()