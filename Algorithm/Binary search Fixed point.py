
#fixed pint is 3
A=[-10,-5,0,3,7]
#fixed point is 0
#A=[0,2,5,8,17]
#Fixed point is None
#A=[-10,-5,3,4,7,9]

def fixed_point_linear(A):
    for i in range(len(A)):
        if A[i]==i:
            return A[i]
    return None

print(fixed_point_linear(A))

