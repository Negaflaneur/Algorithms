import random

def recursive_sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

arr = []
for i in range(0,3):
    arr.append(random.randint(1,10))
print(str(arr))
print(recursive_sum(arr))

'''def count_items(lis): 
    counter = 0
    if lis == []:
        return 0
    else:
        del lis[0]
        counter += 1
        return counter + count_items(lis)

lis = []
for i in range(0,3):
    lis.append(random.randint(1,10))
print(str(lis))
print(count_items(lis))'''

'''def find_max(lis):
    if lis == []:
        return 0 
    else:
        head = lis[0]
        del lis[0]
        max_el = find_max(lis)
        if head > max_el:
            return head
        else:
            return max_el

lis = []
for i in range(0,5):
    lis.append(random.randint(1,10))
print(str(lis))
print(find_max(lis))'''
            
