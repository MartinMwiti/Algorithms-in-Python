A = [-14, -10, 2, 108, 108, 243,285,285,285,401]
target = -14

#my way
def find_target(A, target):
    for i in range(len(A)):
        if i>=0 and i<len(A):
            if A[i]==target:
                return i
    return None

print (find_target(A, target))

#alternative (binary search)
def find(A, target):
    low = 0
    high = len(A) - 1
    while low<=high:
        mid = (low + high)//2
        if A[mid]<target:
            low =mid+1
        elif A[mid]>target:
            high=mid-1
        else:
            if mid-1 < 0:
                return mid
            if A[mid-1] !=target:
                return mid
            high =mid -1
    return None


A = [-14, -10, 2, 108, 108, 243,285,285,285,401]
target = 108
print (find_target(A, target))