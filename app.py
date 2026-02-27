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