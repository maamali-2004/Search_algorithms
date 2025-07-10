def Binary_Search(arr, target, low, high):
    if  low <= high :
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return Binary_Search(arr, target, low, mid - 1)
        else:
            return Binary_Search(arr, target, mid + 1, high)
    else:
        return -1
arr = list(map(int, input().split()))
target = int(input())
result = Binary_Search(sorted(arr), target, 0, len(arr) - 1)
if result != -1 :
    print(f'Element found at index : {result}')
else:
    print('Element not found')