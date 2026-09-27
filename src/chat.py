import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

from peft import PeftModel


# ==========================================
# 1. Model paths
# ==========================================

base_model = "google/flan-t5-small"

fine_tuned_model = "./models/ecommerce-chatbot"


# ==========================================
# 2. Load tokenizer
# ==========================================

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    fine_tuned_model
)


# ==========================================
# 3. Load base model
# ==========================================

print("Loading base model...")

model = AutoModelForSeq2SeqLM.from_pretrained(
    base_model
)


# ==========================================
# 4. Load LoRA adapter
# ==========================================

print("Loading fine-tuned LoRA model...")

model = PeftModel.from_pretrained(
    model,
    fine_tuned_model
)


# ==========================================
# 5. Set evaluation mode
# ==========================================

model.eval()


print("\n====================================")
print("E-Commerce Customer Support Chatbot")
print("====================================")
print("Type 'exit' to stop.\n")


# ==========================================
# 6. Chat loop
# ==========================================

while True:

    question = input("Customer: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    prompt = (
        "You are an e-commerce customer support assistant. "
        "Answer the customer's question clearly and politely.\n\n"
        "Customer: " + question + "\n"
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
            temperature=0.7,
            early_stopping=True
        )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    print("Bot:", response)
    print()