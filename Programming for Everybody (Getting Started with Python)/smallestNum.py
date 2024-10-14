smallest_so_far = None
print("Before: ", smallest_so_far)
for num in [9, 41, 23,67, 3, 90, 23, 6, ]:
    if smallest_so_far is None:
        smallest_so_far = num
    elif num < smallest_so_far:
        smallest_so_far = num
    print("smallest_so_far: ", smallest_so_far)
print("After: ", smallest_so_far)
