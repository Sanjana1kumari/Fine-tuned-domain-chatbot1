import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel

BASE_MODEL = "google/flan-t5-small"
FINE_TUNED_MODEL = "./models/ecommerce-chatbot"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(FINE_TUNED_MODEL)

print("Loading base model...")
model = AutoModelForSeq2SeqLM.from_pretrained(BASE_MODEL)

print("Loading LoRA adapter...")
model = PeftModel.from_pretrained(model, FINE_TUNED_MODEL)

model.eval()

print("\nModel loaded successfully!\n")


test_questions = [
    "Where can I track my order?",
    "I want to return a product I purchased.",
    "When will I receive my refund?",
    "Can I cancel my order?",
    "My package has not arrived yet.",
    "I received a damaged product.",
    "I received the wrong product.",
    "My payment was deducted but the order failed.",
    "How can I update my account information?",
    "The website is not working properly."
]


def generate_response(question):

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
            early_stopping=True
        )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return response


print("=" * 60)
print("CHATBOT EVALUATION")
print("=" * 60)

for i, question in enumerate(test_questions, start=1):

    response = generate_response(question)

    print(f"\nTest {i}")
    print("Customer:", question)
    print("Bot:", response)

print("\n" + "=" * 60)
print("Evaluation completed!")
print("=" * 60)