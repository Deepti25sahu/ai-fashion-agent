def outfit_agent(user_query):
    
    query = user_query.lower()

    # --------------------------------
    # Farewell
    # --------------------------------

    if "farewell" in query:

        return [

            "dress",

            "heels",

            "handbags",

            "jewellery"
        ]

    # --------------------------------
    # Streetwear
    # --------------------------------

    elif (
        "streetwear" in query
        or
        "genz" in query
    ):

        return [

            "hoodies",

            "cargo pants",

            "sneakers",

            "chains"
        ]

    # --------------------------------
    # Party
    # --------------------------------

    elif "party" in query:

        return [

            "party tops",

            "leather pants",

            "heels",

            "bracelets"
        ]

    # --------------------------------
    # Wedding
    # --------------------------------

    elif "wedding" in query:

        return [

            "lehenga",

            "heels",

            "clutch bags",

            "jewellery"
        ]

    # --------------------------------
    # College
    # --------------------------------

    elif "college" in query:

        return [

            "oversized tshirts",

            "baggy jeans",

            "sneakers",

            "backpacks"
        ]

    # --------------------------------
    # Default
    # --------------------------------

    return [

        "tshirts",

        "jeans",

        "sneakers"
    ]