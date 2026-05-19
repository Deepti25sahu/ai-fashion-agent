from agents.fetch_agent import fetch_products


def get_amazon_products(query):

    search_query = f"""
    Amazon {query}
    """

    return fetch_products(search_query)