import requests
import os

from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv(
    "SERPAPI_KEY"
)

# -----------------------------------
# SerpAPI Request
# -----------------------------------

def serpapi_search(query):

    url = (
        "https://serpapi.com/search.json"
    )

    params = {

        "engine":
        "google_shopping",

        "q":
        query,

        "api_key":
        SERPAPI_KEY,

        "gl":
        "in",

        "hl":
        "en"
    }

    response = requests.get(

        url,

        params=params
    )

    return response.json()