#function decalring
def add_order(n, orders=None):
    #functioin defnation
    #which accepts an order and stores orders id across function calls
    if orders is None:
        orders = []
    orders.append(n)
    return orders
#printing oder list correctly wich is stored
print(add_order(101))
print(add_order(102))
print(add_order(103))
print(add_order(104))
print(add_order(105))
print(add_order(106))
print(add_order(107))

