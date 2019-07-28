# Uses python3
import sys

def binary_search(a, x):
    l =0
    r = len(a)-1
    while(l<=r):
        mid = l + (r-l)//2
        if a[mid]==x:
            return mid
        elif a[mid] < x:
            l = mid + 1
        elif a[mid]>x:
            r = mid -1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

 
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    # a = [1,5,8,12,13]
    # data = [8,1,23,1,11]
    for x in data[n + 2:]:
    # for x in data:
        #replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
