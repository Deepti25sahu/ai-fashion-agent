def intent_agent(user_query):
    
    query = user_query.lower()

    intent = {
        "product": "",
        "color": "",
        "budget": "",
        "occasion": "",
        "gender": ""
    }

    # -------------------------
    # Gender Detection
    # -------------------------

    if "women" in query or "girl" in query or "female" in query:
        intent["gender"] = "women"

    elif "men" in query or "boy" in query or "male" in query:
        intent["gender"] = "men"

    else:
        intent["gender"] = "fashion"

    # -------------------------
    # Occasion Detection
    # -------------------------

    if "farewell" in query:
        intent["occasion"] = "farewell"

        if intent["gender"] == "women":
            intent["product"] = "elegant black dress"

        else:
            intent["product"] = "formal blazer outfit"

    elif "wedding" in query:
        intent["occasion"] = "wedding"

        if intent["gender"] == "women":
            intent["product"] = "ethnic saree"

        else:
            intent["product"] = "wedding sherwani"

    elif "party" in query:
        intent["occasion"] = "party"
        intent["product"] = "party wear outfit"

    elif "college" in query:
        intent["occasion"] = "college"
        intent["product"] = "casual college outfit"

    elif "office" in query:
        intent["occasion"] = "office"
        intent["product"] = "formal office wear"

    # -------------------------
    # Product Detection
    # -------------------------

    if "sneaker" in query:
        intent["product"] = "sneakers"

    elif "hoodie" in query:
        intent["product"] = "hoodie"

    elif "jacket" in query:
        intent["product"] = "jacket"

    elif "dress" in query:
        intent["product"] = "dress"

    elif "heels" in query:
        intent["product"] = "heels"

    elif "kurti" in query:
        intent["product"] = "kurti"

    elif "shirt" in query:
        intent["product"] = "shirt"

    elif "jeans" in query:
        intent["product"] = "jeans"

    # -------------------------
    # Color Detection
    # -------------------------

    colors = [
        "black",
        "white",
        "blue",
        "red",
        "pink",
        "green",
        "yellow",
        "purple",
        "brown",
        "grey"
    ]

    for color in colors:
        if color in query:
            intent["color"] = color
            break

    # -------------------------
    # Budget Detection
    # -------------------------

    words = query.replace("₹", "").split()

    for word in words:
        if word.isdigit():
            intent["budget"] = word
            break

    # -------------------------
    # Default Product
    # -------------------------

    if intent["product"] == "":
        intent["product"] = "fashion outfit"

    return intent