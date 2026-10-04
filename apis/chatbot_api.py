from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

# Initialize the chat model
model = init_chat_model(
    "apodex/apodex-1.1-mini:free",
    model_provider="openrouter",
    temperature=0.7
)

# Standard LangChain invoke syntax
# response = model.invoke("Explain Quantum Computing in one short sentence.")
# print(response.content)


app = FastAPI(
    title="Chatbot API",
    description="A simple API for interacting with a chatbot model.",
    version="1.0.0",
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat/{message}")
async def chat(message: str):
    try:
        response = model.invoke(message)
        return {"response": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)