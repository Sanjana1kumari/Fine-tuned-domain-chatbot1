from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Loading model...")

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded successfully!")
print("Model:", model_name)