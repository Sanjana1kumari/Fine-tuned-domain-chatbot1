import json
import torch

from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    TrainingArguments,
    Trainer
)

from peft import LoraConfig, get_peft_model


# ==========================================
# 1. MODEL
# ==========================================

model_name = "google/flan-t5-small"

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Loading model...")

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded successfully!")


# ==========================================
# 2. LOAD DATASETS
# ==========================================

print("Loading datasets...")

with open(
    "data/processed/train.json",
    "r",
    encoding="utf-8"
) as file:
    train_data = json.load(file)

with open(
    "data/processed/validation.json",
    "r",
    encoding="utf-8"
) as file:
    validation_data = json.load(file)


train_dataset = Dataset.from_list(train_data)

validation_dataset = Dataset.from_list(validation_data)

print("Training examples:", len(train_dataset))
print("Validation examples:", len(validation_dataset))


# ==========================================
# 3. PREPARE INPUT FORMAT
# ==========================================

def preprocess_function(examples):

    inputs = []

    for instruction in examples["instruction"]:

        text = (
            "You are an e-commerce customer support assistant. "
            "Answer the customer's question clearly and politely.\n\n"
            "Customer: " + instruction + "\n"
            "Answer:"
        )

        inputs.append(text)

    # Tokenize input
    model_inputs = tokenizer(
        inputs,
        max_length=128,
        truncation=True,
        padding="max_length"
    )

    # Tokenize output
    labels = tokenizer(
        examples["output"],
        max_length=128,
        truncation=True,
        padding="max_length"
    )

    model_inputs["labels"] = labels["input_ids"]

    return model_inputs


print("Tokenizing training dataset...")

train_dataset = train_dataset.map(
    preprocess_function,
    batched=True
)

print("Tokenizing validation dataset...")

validation_dataset = validation_dataset.map(
    preprocess_function,
    batched=True
)

print("Tokenization completed!")


# ==========================================
# 4. CONFIGURE LoRA
# ==========================================

print("Configuring LoRA...")

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q", "v"],
    lora_dropout=0.05,
    bias="none",
    task_type="SEQ_2_SEQ_LM"
)

model = get_peft_model(
    model,
    lora_config
)

print("LoRA configured!")

model.print_trainable_parameters()


# ==========================================
# 5. TRAINING CONFIGURATION
# ==========================================

training_args = TrainingArguments(
    output_dir="./models/ecommerce-chatbot",

    num_train_epochs=2,

    per_device_train_batch_size=2,

    per_device_eval_batch_size=2,

    learning_rate=2e-4,

    logging_steps=10,

    save_strategy="epoch",

    eval_strategy="epoch",

    report_to="none"
)


# ==========================================
# 6. TRAINER
# ==========================================

trainer = Trainer(
    model=model,

    args=training_args,

    train_dataset=train_dataset,

    eval_dataset=validation_dataset
)


# ==========================================
# 7. START TRAINING
# ==========================================

print("Starting LoRA fine-tuning...")

trainer.train()


# ==========================================
# 8. SAVE MODEL
# ==========================================

print("Saving fine-tuned model...")

model.save_pretrained(
    "./models/ecommerce-chatbot"
)

tokenizer.save_pretrained(
    "./models/ecommerce-chatbot"
)

print("Training completed successfully!")

print("Model saved to:")
print("./models/ecommerce-chatbot")