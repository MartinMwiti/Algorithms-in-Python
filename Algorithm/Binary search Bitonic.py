A = [1,2,3,4,5,4,3,2,1]
len(A)
#Find peak element
def find_peak_element(A):
    for i in range(len(A)):
        if A[i-1]>A[i]:
            return A[i-1]
        

print(find_peak_element(A))


def find_highest_element(A):
    low = 0
    high =len(A)-1

    #require at least 3 elements for a valid bitonic sequence
    if len(A)< 3:
        return None
    while low <= high:
        mid = (low+high)//2

        #element immediate side of the mid point
        mid_left = A[mid-1] if mid-1>0 else float('-inf')
        mid_right = A[mid+1] if mid+1 <len(A) else float('inf')

        if mid_left< A[mid] and mid_right>A[mid]:
            low = mid+1
        elif mid_left>A[mid] and mid_right<A[mid]:
            high = mid-1
        elif mid_left < A[mid] and mid_right<A[mid]:
            return A[mid]

#peak is 5
A = [1,2,3,4,5,4,3,2,1]

#peak is 4
#A = [1,2,3,4,1]

#peak is 6
#A = [1,6,5,4,3,2,1]

print(find_highest_element(A))

