# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    [count, result] = mergesort(a)
    return count

def mergesort(a):
    if len(a)==1:
        return [0,a]
    mid = len(a)//2
    left = mergesort(a[0:mid])
    right = mergesort(a[mid:])
    return merge(left, right)

def merge(left, right):
    count = left[0] + right [0]
    left_arr = left[1]
    right_arr = right[1]
    result = []

    while len(left_arr)>0 and len(right_arr)>0:
        if left_arr[0]>right_arr[0]:
            result.append(left_arr[0])
            count += len(right_arr)
            del (left_arr[0])
        else:
            result.append(right_arr[0])
            del (right_arr[0])
    result += left_arr
    result += right_arr
    return [count,result]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
