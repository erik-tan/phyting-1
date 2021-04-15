import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    arr = sys.stdin.readline().split()
    arr = list(map(int,arr))

    refer_arr = [0]*(n+1)

    count = 0
    for item in arr:
        if refer_arr[item] == 0:
            count +=1
        else:
            refer_arr[item] -=1
        refer_arr[item-1] +=1        
    print(count)