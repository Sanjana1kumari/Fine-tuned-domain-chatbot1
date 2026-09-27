import json
import random
import os

random.seed(42)

input_file = "data/processed/ecommerce_chatbot_dataset.json"

train_file = "data/processed/train.json"
validation_file = "data/processed/validation.json"


# Load dataset
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)


# Shuffle dataset
random.shuffle(data)


# 80% training, 20% validation
split_index = int(len(data) * 0.8)

train_data = data[:split_index]
validation_data = data[split_index:]


# Save training dataset
with open(train_file, "w", encoding="utf-8") as file:
    json.dump(train_data, file, indent=2, ensure_ascii=False)


# Save validation dataset
with open(validation_file, "w", encoding="utf-8") as file:
    json.dump(validation_data, file, indent=2, ensure_ascii=False)


print("Dataset split successfully!")
print("Total examples:", len(data))
print("Training examples:", len(train_data))
print("Validation examples:", len(validation_data))
print("Training file:", train_file)
print("Validation file:", validation_file)