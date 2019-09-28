import bisect

A = [-14,-10,2,108,108, 243,285,285,285,401]

#bisect_left fn finds left most index of the target element
print(bisect.bisect_left(A, 285))

#index poaition to the right of the target
print(bisect.bisect_right(A, 285))
print(bisect.bisect_right(A, -14))

#inserting values into a list
bisect.insort_left(A, 108)
print(A)