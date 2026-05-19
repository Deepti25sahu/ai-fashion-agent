# -----------------------------------
# Clean Price
# -----------------------------------

def clean_price(price):

    numbers = "".join(

        filter(str.isdigit, str(price))
    )

    if numbers == "":

        return 0

    return int(numbers)

# -----------------------------------
# Safe Rating
# -----------------------------------

def safe_rating(rating):

    try:

        return float(rating)

    except:

        return 0