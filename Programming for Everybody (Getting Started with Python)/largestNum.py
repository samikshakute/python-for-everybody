largest_so_far = -1
print("Before: ", largest_so_far)
for num in [9, 41, 23,67, 56, 90, 23, 839, 198]:
    if num > largest_so_far:
        largest_so_far = num
    print("largest_so_far: ", largest_so_far)
print("After: ", largest_so_far)
