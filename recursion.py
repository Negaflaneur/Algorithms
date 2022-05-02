def countdown(i):
    if i < 0: #base case
        return
    else: #recursive case
        print(i)
        countdown(i-1)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x* factorial(x-1)

countdown(3)
print(factorial(5))

