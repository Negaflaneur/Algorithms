## bubble sort is similar to the selection sort, but every time you swap elements O(n) runtime
import random

def bubble_sort(unsorted_lis):
    for i in range(len(unsorted_lis)):
        swapped = False
        for j in range(0, len(unsorted_lis) - 1 - i):
            if unsorted_lis[j] > unsorted_lis[j + 1]:
                unsorted_lis[j+1], unsorted_lis[j] = unsorted_lis[j], unsorted_lis[j+1]
                swapped = True
        if not(swapped):
            break
    return unsorted_lis


unsorted_list = [random.randint(1,100) for i in range(10)]
print(f'Unsorted list is {unsorted_list}')
sorted_list = bubble_sort(unsorted_list)
print(f'The sorted list is ', sorted_list)
