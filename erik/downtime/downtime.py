import sys
from queue import Queue
import math

if __name__ == "__main__":
    n, k = map(int,sys.stdin.readline().split())

    arr = []
    max_len = 0

    for _ in range(n):
        t = int(sys.stdin.readline())
        if not arr:
            arr.append(t)

        else:
            arr.append(t)
            while t-1000 >= arr[0]:
                arr.pop(0)
                
        if len(arr) > max_len:
            max_len = len(arr)

    print(math.ceil(max_len/k))