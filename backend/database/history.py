history_db = []

# -----------------------------------
# Add History
# -----------------------------------

def add_history(query):

    history_db.append(query)

# -----------------------------------
# Get History
# -----------------------------------

def get_history():

    return history_db[-20:]