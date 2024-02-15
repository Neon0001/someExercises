def lonelyinteger(a):
    unique = 0
    for numbers in a:
        if a.count(numbers) == 1:
            unique = numbers
    return unique

print(lonelyinteger([1,2,3,4,3,2,1]))