from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import json

app = FastAPI()

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

class CustomerMessage(BaseModel):
    message: str

@app.post("/order")
def process_order(data: CustomerMessage):
    response = client.chat.completions.create(
        model="llama-3.2-3b-instruct",
        messages=[
            {
                "role": "system",
                "content": "Extract the item and quantity from the customer message. Respond only with JSON in this exact format: {\"item\": \"item name\", \"quantity\": number}"
            },
            {
                "role": "user",
                "content": data.message
            }
        ]
    )
    
    raw = response.choices[0].message.content
    
    try:
        order = json.loads(raw)
        item = order["item"]
        quantity = order["quantity"]
        confirmation = f"{item.capitalize()} x{quantity} has been added to your order!"
    except:
        confirmation = "Order received but could not be fully parsed."
        order = raw

    return {
        "extracted": order,
        "confirmation": confirmation
    }