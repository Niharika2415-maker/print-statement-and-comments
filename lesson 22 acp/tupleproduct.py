# Given tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 88, 3, 2, 9)
def tuple_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product
prod1 = tuple_product(tup1)
prod2 = tuple_product(tup2)
print("Product of tup1:", prod1)
print("Product of tup2:", prod2)
