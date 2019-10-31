#write a fn that takes a non-negative integer and returns the largest integr whose square is less than or equal to the integer given.

k = 300

def integer_square_root(k):
    low =0
    high = k

    while low<=high:
        mid = (low+high)//2
        mid_squared = mid*mid

        if mid_squared<=k:
            low = mid+1
        else:
            high = mid-1
    return low-1

print(integer_square_root(k))