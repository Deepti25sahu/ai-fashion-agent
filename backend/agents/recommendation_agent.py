def recommendation_agent(products):
    
    recommended = sorted(
        products,
        key=lambda x: float(x["rating"]),
        reverse=True
    )

    return recommended