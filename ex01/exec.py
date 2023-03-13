import sys

list = sys.argv[1:]
if list:
    tmp = ' '.join(list[::1])
    swap = tmp.swapcase()
    print(swap[::-1])
else :
    exit
