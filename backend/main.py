from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from pydantic import BaseModel

# -----------------------------------
# Agents
# -----------------------------------

from agents.intent_agent import (
    intent_agent
)

from agents.search_agent import (
    search_agent
)

from agents.recommendation_agent import (
    recommendation_agent
)

from agents.ranking_agent import (
    ranking_agent
)

from agents.outfit_agent import (
    outfit_agent
)

# -----------------------------------
# Shopping Aggregator
# -----------------------------------

from shopping.aggregator import (
    aggregate_products
)

# -----------------------------------
# FastAPI App
# -----------------------------------

app = FastAPI()

# -----------------------------------
# CORS
# -----------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# -----------------------------------
# Request Model
# -----------------------------------

class ChatRequest(BaseModel):

    message: str

# -----------------------------------
# Root Route
# -----------------------------------

@app.get("/")
def root():

    return {

        "message":
        "AI Fashion Shopping Agent Running"
    }

# -----------------------------------
# Chat Route
# -----------------------------------

@app.post("/chat")
async def chat(req: ChatRequest):

    user_message = req.message

    # Intent Detection

    intent = intent_agent(
        user_message
    )

    # Search Query

    search_query = search_agent(
        intent
    )

    # Outfit Buttons Keywords

    outfit_keywords = [

        "hoodies",
        "cargo pants",
        "sneakers",
        "chains",
        "dress",
        "heels",
        "handbags",
        "jewellery",
        "party tops",
        "bracelets",
        "tshirts",
        "jeans"
    ]

    # Product Fetch

    if (
        user_message.lower()
        in outfit_keywords
    ):

        products = aggregate_products(
            user_message
        )

    else:

        products = aggregate_products(
            search_query
        )

    # Outfit Suggestions

    outfit = outfit_agent(
        user_message
    )

    # Recommendation

    products = recommendation_agent(
        products
    )

    # Ranking

    products = ranking_agent(
        products
    )

    # Final Response

    return {

        "reply": f"""
        Here are stylish recommendations for:
        {user_message}
        """,

        "products": products,

        "outfit": outfit
    }