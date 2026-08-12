def calculate_checkout(cart_total, shipping_speed):
    shipping_cost = 0
    cart_total = (input("how much are you spending?: "))  
    if shipping_speed == "express":
        shipping_cost = 20
    elif shipping_speed == "overnight":
        shipping_cost = 35
    elif shipping_speed == "standard":
        if cart_total >= 100:
            shipping_cost = 0
        elif cart_total < 100:
            shipping_cost = 10
    else:
        print("You can't do that.")
    return shipping_cost + cart_total

print(calculate_checkout(10000,"express"))