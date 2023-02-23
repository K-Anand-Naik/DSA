def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        c_value = A[i]
        position = i
        while position > 0 and A[position-1] > c_value:
            A[position] = A[position-1]
            postion = position-1
        A[position] = c_value


A = [3, 5, 8, 9, 6, 2]
print("Original Array: ", A)
insertion_sort(A)
print("Sorted Array: ", A)
