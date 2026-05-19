# -----------------------------------
# Ranking Agent
# -----------------------------------

def ranking_agent(products):

    try:

        ranked_products = sorted(

            products,

            key=lambda x: float(
                x.get("rating", 0)
            ),

            reverse=True
        )

        return ranked_products

    except Exception as e:

        print(e)

        return products