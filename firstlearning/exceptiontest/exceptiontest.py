
fh = open("test.txt","w")
try:
    fh.write("exception test!");
finally:
    print("deal excepption over!");
    fh.close()