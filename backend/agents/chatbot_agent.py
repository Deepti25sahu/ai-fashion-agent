import requests
import os

from dotenv import load_dotenv

load_dotenv()

# -----------------------------------
# TOKEN
# -----------------------------------

HF_TOKEN = os.getenv("HF_TOKEN")

print("HF TOKEN:")
print(HF_TOKEN)

# -----------------------------------
# MODEL
# -----------------------------------

API_URL = (
    "https://api-inference.huggingface.co/models/"
    "microsoft/DialoGPT-medium"
)

# -----------------------------------
# HEADERS
# -----------------------------------

headers = {

    "Authorization":
    f"Bearer {HF_TOKEN}"
}

# -----------------------------------
# CHATBOT
# -----------------------------------

def chatbot_agent(user_query):

    try:

        payload = {

            "inputs": user_query
        }

        response = requests.post(

            API_URL,

            headers=headers,

            json=payload,

            timeout=120
        )

        print("STATUS:")
        print(response.status_code)

        print("TEXT:")
        print(response.text)

        data = response.json()

        print("JSON:")
        print(data)

        # --------------------------------
        # SUCCESS
        # --------------------------------

        if (
            isinstance(data, list)
            and
            len(data) > 0
        ):

            if (
                "generated_text"
                in data[0]
            ):

                return data[0][
                    "generated_text"
                ]

        # --------------------------------
        # ERROR
        # --------------------------------

        if (
            isinstance(data, dict)
            and
            "error" in data
        ):

            return f"""
            HuggingFace Error:

            {data['error']}
            """

        return """
        AI stylist unavailable.
        """

    except Exception as e:

        print("ERROR:")
        print(e)

        return f"""
        Error:

        {str(e)}
        """