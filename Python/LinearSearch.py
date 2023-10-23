def linearSearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1

arr=input("Enter list of elements: ").split()
arr=[int(i) for i in arr]
key=int(input("Enter a key to search: "))
index=linearSearch(arr,key)
if index!=-1:
    print("key is found at",index)
else:
    print("key not found!")