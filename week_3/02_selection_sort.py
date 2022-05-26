input = [4, 6, 2, 9, 1]

# [4,6,2,9,1]
#  - - - - -
# [1,6,2,9,4]
#    - - - -
# [1,2,6,9,4]
#      - - -
# [1,2,4,9,6]
#        - -


def selection_sort(array):
    n = len(array)

    for i in range(n - 1):  # i = 0
        min_index = i
        for j in range(n - i):  # j = 1
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!