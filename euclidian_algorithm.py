def Euclidian_algorithm(a,b):
    diff= 0
    if a > b:
        diff = a -b
    elif a < b:
        diff = b - a
    elif a - b == 0:
        diff = a
        return diff
    return Euclidian_algorithm(diff, min(a,b))

a = int(input("First number "))
b = int(input("Second number "))
result = Euclidian_algorithm(a,b)
print(result)
