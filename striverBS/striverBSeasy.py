def binarySearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1




arr=[3, 4, 6, 7, 9, 12, 16, 17]
print(binarySearch(arr,6))