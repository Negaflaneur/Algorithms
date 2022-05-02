import random

def selection_sort(uns_list:list):
    sorted_lis = []
    max_el = uns_list[0]
    while len(uns_list) > 0:
        for i in range(len(uns_list)):
            if uns_list[i] >= max_el:
                max_el = uns_list[i]
        sorted_lis.append(max_el)
        uns_list.remove(max_el)
        if len(uns_list) >= 1:
            max_el = uns_list[0]
    return sorted_lis



unsorted_list = []
for i in range(0,20):
    unsorted_list.append(random.randint(1,100))
print('The initial list is ', unsorted_list)
sorted_list = selection_sort(unsorted_list)
print('The sorted list is ',sorted_list)