search_history = []

# -----------------------------------
# Save Search
# -----------------------------------

def save_search(query):

    global search_history

    search_history.append(query)

    # Keep only latest 10

    search_history = (
        search_history[-10:]
    )

# -----------------------------------
# Get Search History
# -----------------------------------

def get_history():

    return search_history