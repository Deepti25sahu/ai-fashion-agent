from agents.fetch_agent import fetch_products


def get_flipkart_products(query):

    search_query = f"""
    Flipkart {query}
    """

    return fetch_products(search_query)