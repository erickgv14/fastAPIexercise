# FastAPI Order Processing API

A Python API built with FastAPI that receives customer food orders through a POST endpoint and uses a local language model to extract the item and quantity from the message. Returns a confirmation once the order is processed.

## Prerequisites

- Python 3.10 or higher — download at python.org
- LM Studio — download at lmstudio.ai
- Llama 3.2 3B model downloaded inside LM Studio
- Postman or any API testing tool — download at postman.com

## Setup Instructions

**1. Clone the repository**
```bash
git clone https://github.com/erickgv14/fastAPIexercise.git
cd fastAPIexercise
```

**2. Install dependencies**
```bash
pip install fastapi uvicorn openai
```
If you get a "not recognized" error, try:
```bash
python -m pip install fastapi uvicorn openai
```

**3. Set up LM Studio**
- Open LM Studio and download the following model: `llama-3.2-3b-instruct`
- Go to the Developer tab
- Start the server — confirm it says "Reachable at http://127.0.0.1:1234"

**4. Run the API**
```bash
uvicorn main:app --reload
```

**5. Test the endpoint**
Open Postman or any API testing tool and send a POST request to:
`http://localhost:8000/order`

With this JSON body:
```json
{
    "message": "I want 2 coffees"
}
```