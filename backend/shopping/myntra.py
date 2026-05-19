from agents.fetch_agent import fetch_products


def get_myntra_products(query):

    search_query = f"""
    Myntra {query}
    """

    return fetch_products(search_query)