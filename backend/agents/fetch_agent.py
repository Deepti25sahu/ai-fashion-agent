import requests

import os

from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv(
    "SERPAPI_KEY"
)

# -----------------------------------
# Fetch Products
# -----------------------------------

def fetch_products(search_query):

    url = (
        "https://serpapi.com/search.json"
    )

    params = {

        "engine":
        "google_shopping",

        "q":
        search_query,

        "api_key":
        SERPAPI_KEY,

        "gl":
        "in",

        "hl":
        "en",

        "google_domain":
        "google.co.in"
    }

    response = requests.get(
        url,
        params=params
    )

    data = response.json()

    print(data)

    products = []

    # --------------------------------
    # Shopping Results
    # --------------------------------

    if "shopping_results" in data:

        for item in data[
            "shopping_results"
        ][:50]:

            image = ""

            # ------------------------
            # Main Thumbnail
            # ------------------------

            if "thumbnail" in item:

                image = item[
                    "thumbnail"
                ]

            # ------------------------
            # SerpAPI Thumbnails
            # ------------------------

            elif (
                "serpapi_thumbnails"
                in item
                and
                len(
                    item[
                        "serpapi_thumbnails"
                    ]
                ) > 0
            ):

                image = item[
                    "serpapi_thumbnails"
                ][0]

            # ------------------------
            # Other Thumbnails
            # ------------------------

            elif (
                "thumbnails"
                in item
                and
                len(
                    item["thumbnails"]
                ) > 0
            ):

                image = item[
                    "thumbnails"
                ][0]

            # ------------------------
            # Fallback Image
            # ------------------------

            if image == "":

                image = (
                    "https://picsum.photos/400/500"
                )

            # ------------------------
            # Product Object
            # ------------------------

            products.append({

                "name":
                item.get(
                    "title",
                    "Fashion Product"
                ),

                "price":
                item.get(
                    "price",
                    "₹N/A"
                ),

                "image":
                image,

                "link":
item.get(
    "product_link",
    item.get("link", "#")
),

                "source":
                item.get(
                    "source",
                    "Store"
                ),

                "rating":
                str(
                    item.get(
                        "rating",
                        "4.0"
                    )
                ),

                "reviews":
                str(
                    item.get(
                        "reviews",
                        "100"
                    )
                ),

                "delivery":
                "Fast Delivery",

                "reason":
                """
                Recommended based on
                your fashion preferences.
                """
            })

    print(products)

    return products