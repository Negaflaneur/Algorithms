import random

def binary_search(lis, item):
    print("The item you are looking for is ", item)
    binary_list = lis
    low = 0
    high = len(binary_list) -1
    mid = (low + high) //2
    guess_num = binary_list[mid]

    while guess_num != item:
        if guess_num > item:
            high = mid
            mid = (low + high) // 2
            guess_num = binary_list[mid]
        elif mid < item:
            low = mid
            mid = (low + high) //2
            guess_num = binary_list[mid]
        else:
            return None
    print("We have found item ", guess_num)

lis = []
for el in range(8):
    lis.append(random.randint(1, 100))

sorted_lis = sorted(lis)


print("You list is ", sorted_lis)
required_item = lis[random.randint(0, len(sorted_lis)-1)]

print("The element we are looking for is ", required_item)

binary_search(sorted_lis, required_item)
