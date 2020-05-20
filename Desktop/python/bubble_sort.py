'''
def bubble_sort(arr):
    def swap(i,j):
        arr[i],arr[j]=arr[j],arr[i]

    n=len(arr)
    swapped=True

    x=-1
    while swapped:
        swapped=False
        x=x+1
        for i in range(1,n-x):
            if arr[i-1]>arr[i]:
                swap(i-1,i)
                swapped=True
    return arr
    

arr=[6,5,3,1,8,7,2,4]
print(arr)
'''
mylist=[5,3,7,2,8,4]

n=len(mylist)
for i in range(n):
    for j in range(1,n-i):
        if mylist[j-1]>mylist[j]:
            mylist[j-1],mylist[j]=mylist[j],mylist[j-1]
print(mylist)
