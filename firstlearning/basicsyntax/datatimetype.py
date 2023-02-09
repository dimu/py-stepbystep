# date and time basic syntax
import time

print("current time:%d"%time.time())

localtime = time.localtime(time.time())
print("local current time:", localtime)