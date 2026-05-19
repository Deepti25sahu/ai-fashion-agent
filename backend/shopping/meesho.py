from agents.fetch_agent import fetch_products


def get_meesho_products(query):

    search_query = f"""
    Meesho {query}
    """

    return fetch_products(search_query)