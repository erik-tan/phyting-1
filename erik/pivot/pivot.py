import sys

if __name__ == "__main__":
    n = sys.stdin.readline()

    arr = sys.stdin.readline().split()
    arr = list(map(int,arr))

    max_list = []
    max_list.append(arr[0])
    for i in range(1,(len(arr))):
        max_list.append(max(max_list[i-1],arr[i]))

    min_list = [float('inf')]*(int(n))
    min_list[-1] = arr[-1]
    for i in range(len(min_list)-2,-1,-1):
        min_list[i] = min(min_list[i+1],arr[i])

    counter = 0
    for i in range(len(max_list)):
        if max_list[i] == min_list[i]:
            counter +=1

    print(counter)


# len(arr)/(max_list)/(min_list) == n 