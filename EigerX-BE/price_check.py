def price_check(products, product_prices, product_sold, sold_price):
    """
    This function receives 2 lists of products and their prices, and 2 lists of actual products sold and their prices.
    Returns the number of errors in selling prices.
    """
    errors = 0
    product_dict = {}

    for i in range(len(products)):
        product_dict[products[i]] = product_prices[i]

    for i in range(len(product_sold)):
        if sold_price[i] != product_dict[product_sold[i]]:
            errors += 1

    return errors


if __name__ == '__main__':
    print(price_check(
        products=['rice', 'sugar', 'wheat', 'cheese'],
        product_prices=[16.89, 56.92, 20.89, 345.99],
        product_sold=['rice', 'cheese', 'wheat', 'cheese', 'sugar'],
        sold_price=[16.89, 400.89, 1, 345.99, 56.92]
    ))
