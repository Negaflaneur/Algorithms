import random


def quicksort(arr):
    if len(arr) < 2:
        return arr
    elif len(arr) == 2:
        if arr[1] < arr[0]:
            arr[0] = arr[1]
        return arr
    elif len(arr) > 2:
        pivot = arr[0]
        left_sub_array = [el for el in arr[1:] if el <= pivot]
        right_sub_array = [el for el in arr[1:] if el >= pivot]
        return quicksort(left_sub_array) + [pivot] + quicksort(right_sub_array)


unsorted_list = []
for i in range(0,5):
    unsorted_list.append(random.randint(1,100))
print('The initial list is ', str(unsorted_list))
sorted_list = quicksort(unsorted_list)
print('The sorted list is ', str(sorted_list))