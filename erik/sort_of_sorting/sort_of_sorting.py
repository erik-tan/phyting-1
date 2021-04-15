import sys

n = int(sys.stdin.readline())
while n != 0:
    arr = []
    for _ in range(n):
        arr.append((sys.stdin.readline().rstrip('\n')))
    arr = sorted(arr, key=lambda x:x[:2])        
    for item in arr:
        print(item, "\n")
    n = int(sys.stdin.readline())
