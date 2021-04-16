import sys

n = int(sys.stdin.readline())

arr = sys.stdin.readline().split()
arr = list(map(int,arr))

# Tranverse from left to right, 2 pointers
header = min_height = arr[0]
margin = 0
for i in range(1,n):
    tail = arr[i]
    # if header < tail, change header and return margin
    if header <= tail:
        temp_margin = header - min_height
        if temp_margin > margin:
            margin = temp_margin
        min_height = tail
        header = tail
    # if header > tail: find min_height
    elif header > tail:
        if min_height > tail:
            min_height = tail

# tranverse from right to left
header = min_height = arr[n-1]
for i in range(n-2,-1,-1):
    tail = arr[i]
    # if header < tail, change header and return margin
    if header <= tail:
        temp_margin = header - min_height
        if temp_margin > margin:
            margin = temp_margin
        min_height = tail
        header = tail
    # if header > tail: find min_height
    elif header > tail:
        if min_height > tail:
            min_height = tail
print(margin)