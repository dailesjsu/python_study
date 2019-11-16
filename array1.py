# Given an array, , of  integers, print each element in reverse order as a single line of space-separated integers.

def reverseArray(a):
    for i in reversed(arr):
        print(i,end=' ')

if __name__ == '__main__':

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
