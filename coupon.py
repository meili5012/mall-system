def calculate_discount(price, discount):
    if price < 0:
        return 0
    if discount < 0 or discount > 100:
        return price
    return price * (1 - discount / 100)
