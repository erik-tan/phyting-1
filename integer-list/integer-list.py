import sys
from collections import deque
# import ast
testcase_count = int(sys.stdin.readline())
counter = 1
while counter <= testcase_count:
    isReverse = False
    isError = False
    
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()
    arr = [] if n==0 else list(map(int, arr[1:-2].split(',')))
    queue = deque(arr)
    
    for letter in command:
        # if not queue:
        #     break
        # elif letter == "R":
        #     isReverse = not isReverse
        # elif letter == "D":
        #     if not isReverse:
        #         queue.popleft()
        #     else:
        #         queue.pop()
        # OK BYEE        
        if letter == "R":
            isReverse = not isReverse
        elif letter == "D" and queue:
            if not isReverse:
                queue.popleft()
            else:
                queue.pop()
        else:
            isError = True
            break
        
    if isError:
        print("error")
    elif isReverse:
        ret = str(list(reversed(queue)))
        print(ret.replace(' ',''))
    else:
        ret = str(list(queue))
        print(ret.replace(' ',''))

    counter +=1