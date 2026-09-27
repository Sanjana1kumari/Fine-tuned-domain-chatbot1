from fastapi import FastAPI
from pydantic import BaseModel

import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

from peft import PeftModel


# ==========================================
# Create FastAPI application
# ==========================================

app = FastAPI(
    title="E-Commerce Customer Support Chatbot",
    description="Fine-tuned LoRA chatbot API",
    version="1.0"
)


# ==========================================
# Model paths
# ==========================================

BASE_MODEL = "google/flan-t5-small"

FINE_TUNED_MODEL = "./models/ecommerce-chatbot"


# ==========================================
# Load tokenizer
# ==========================================

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    FINE_TUNED_MODEL
)


# ==========================================
# Load base model
# ==========================================

print("Loading base model...")

model = AutoModelForSeq2SeqLM.from_pretrained(
    BASE_MODEL
)


# ==========================================
# Load LoRA adapter
# ==========================================

print("Loading LoRA adapter...")

model = PeftModel.from_pretrained(
    model,
    FINE_TUNED_MODEL
)

model.eval()

print("Model loaded successfully!")


# ==========================================
# Request structure
# ==========================================

class ChatRequest(BaseModel):

    message: str


# ==========================================
# Health check
# ==========================================

@app.get("/")
def home():

    return {
        "message": "E-Commerce Chatbot API is running!"
    }


# ==========================================
# Chat endpoint
# ==========================================

@app.post("/chat")
def chat(request: ChatRequest):

    prompt = (
        "You are an e-commerce customer support assistant. "
        "Answer the customer's question clearly and politely.\n\n"
        "Customer: " + request.message + "\n"
        "Answer:"
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=128,
        truncation=True
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_length=128,
            num_beams=4,
            early_stopping=True
        )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return {
        "question": request.message,
        "answer": response
    }