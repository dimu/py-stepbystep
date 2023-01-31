#
import heapq

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("unpacking element from iterarable of arbitrary length！ ")
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    lineSplit = line.split(':')
    print(lineSplit)
    uname, *fields, homedir, sh = lineSplit
    print(homedir)
    print(fields)
    print(sh)
    heapq.nlargest()
