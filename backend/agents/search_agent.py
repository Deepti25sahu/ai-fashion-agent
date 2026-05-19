def search_agent(intent):
    
    product = intent["product"]
    color = intent["color"]
    budget = intent["budget"]
    gender = intent["gender"]
    occasion = intent["occasion"]

    search_query = ""

    if color:
        search_query += f"{color} "

    if gender and gender != "fashion":
        search_query += f"{gender} "

    search_query += product

    if occasion:
        search_query += f" for {occasion}"

    if budget:
        search_query += f" under {budget}"

    return search_query