def binarySearch(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
    



arr=input("Enter list of elements: ").split()
arr=[int(i) for i in arr]
key=int(input("Enter a key to search: "))
index=binarySearch(arr,key)
if index!=-1:
    print("key is found at",index)
else:
    print("key not found!")