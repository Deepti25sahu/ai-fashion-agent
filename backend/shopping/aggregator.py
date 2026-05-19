from shopping.flipkart import get_flipkart_products
from shopping.myntra import get_myntra_products
from shopping.amazon import get_amazon_products
from shopping.meesho import get_meesho_products


def aggregate_products(query):

    products = []

    try:
        products.extend(
            get_flipkart_products(query)
        )
    except:
        pass

    try:
        products.extend(
            get_myntra_products(query)
        )
    except:
        pass

    try:
        products.extend(
            get_amazon_products(query)
        )
    except:
        pass

    try:
        products.extend(
            get_meesho_products(query)
        )
    except:
        pass

    return products