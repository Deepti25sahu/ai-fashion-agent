# -----------------------------------
# Fashion Stylist Agent
# -----------------------------------

def stylist_agent(product_name):

    product = product_name.lower()

    if "dress" in product:

        return """
        Pair with silver heels
        and minimal jewellery
        for an elegant look.
        """

    elif "hoodie" in product:

        return """
        Style with cargo pants
        and chunky sneakers
        for GenZ streetwear vibes.
        """

    elif "jeans" in product:

        return """
        Oversized tshirts
        look great with baggy jeans.
        """

    elif "heels" in product:

        return """
        Neutral handbags pair
        beautifully with heels.
        """

    return """
    Match with trendy accessories
    for a complete outfit.
    """