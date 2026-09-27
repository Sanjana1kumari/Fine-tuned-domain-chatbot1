import json
import os
import random

random.seed(42)

categories = {
    "order_tracking": [
        "Where is my order?",
        "How can I track my order?",
        "Can I track my package?",
        "Where is my package right now?",
        "What is the status of my order?",
        "How do I check my shipment?",
        "My order has not arrived yet.",
        "Can you tell me where my package is?",
        "I want to see my order status.",
        "How can I find my tracking details?"
    ],

    "return": [
        "How can I return a product?",
        "I want to return my order.",
        "Can I return an item?",
        "How do I send an item back?",
        "I need to return something I purchased.",
        "What is the return process?",
        "How can I request a return?",
        "I received the product but want to return it.",
        "Can I send this product back?",
        "Where can I start a return?"
    ],

    "refund": [
        "How do I get a refund?",
        "Where is my refund?",
        "When will I receive my refund?",
        "How long does a refund take?",
        "My refund has not arrived.",
        "Can I get my money back?",
        "What is the refund process?",
        "When will my refund be processed?",
        "I am waiting for my refund.",
        "How can I check my refund status?"
    ],

    "cancellation": [
        "Can I cancel my order?",
        "I want to cancel my purchase.",
        "How do I cancel my order?",
        "Can I stop my order?",
        "I placed an order by mistake.",
        "I don't want my order anymore.",
        "Please cancel my order.",
        "Is order cancellation possible?",
        "How can I cancel a purchase?",
        "Can I cancel before shipping?"
    ],

    "delivery": [
        "How long does delivery take?",
        "When will my order arrive?",
        "My delivery is delayed.",
        "When can I expect my package?",
        "What is the delivery time?",
        "Why is my delivery late?",
        "When will my package be delivered?",
        "How can I check the estimated delivery date?",
        "My order has not been delivered.",
        "What is the expected arrival date?"
    ],

    "damaged_product": [
        "My product arrived damaged.",
        "I received a damaged item.",
        "The product is broken.",
        "My package contains a damaged product.",
        "The item was damaged during delivery.",
        "What should I do if my product is damaged?",
        "I received a broken item.",
        "The product arrived in bad condition.",
        "My item is damaged.",
        "How can I report a damaged product?"
    ],

    "wrong_product": [
        "I received the wrong product.",
        "The item I received is incorrect.",
        "I got a different product.",
        "My order contains the wrong item.",
        "The product delivered is not what I ordered.",
        "I received an incorrect item.",
        "Why did I receive a different product?",
        "The wrong item was delivered.",
        "This is not the product I purchased.",
        "How can I report a wrong product?"
    ],

    "payment": [
        "What payment methods are available?",
        "Can I pay using a card?",
        "Do you accept credit cards?",
        "Can I pay online?",
        "What payment options do you support?",
        "Can I use a debit card?",
        "How can I pay for my order?",
        "Is online payment available?",
        "What payment methods can I use?",
        "Can I pay with my card?"
    ],

    "account": [
        "How do I create an account?",
        "How can I change my password?",
        "I forgot my password.",
        "How do I update my account details?",
        "Can I change my email address?",
        "How can I update my phone number?",
        "I cannot log into my account.",
        "How do I reset my password?",
        "How can I access my account?",
        "I need help with my account."
    ],

    "product_information": [
        "How can I get more information about a product?",
        "Where can I see product details?",
        "What are the product specifications?",
        "Can I see the product features?",
        "Where can I find product information?",
        "How do I check the product specifications?",
        "Tell me more about this product.",
        "Where are the product details listed?",
        "Can I see product features?",
        "How can I learn more about an item?"
    ],

    "technical_issue": [
        "The website is not working.",
        "I cannot place my order.",
        "The app is not working.",
        "The checkout page is not loading.",
        "I am having trouble placing an order.",
        "The website keeps showing an error.",
        "Why is the checkout not working?",
        "I cannot complete my purchase.",
        "There is an error on the website.",
        "The app keeps crashing."
    ]
}


responses = {
    "order_tracking":
        "You can check your order status and tracking information from the order details section.",

    "return":
        "You can request a return for an eligible product through your order details. Select the return option and follow the instructions.",

    "refund":
        "Once an eligible return is approved and processed, the refund will be issued according to the applicable refund policy.",

    "cancellation":
        "You can cancel an order if it has not been shipped yet. Open your order details and select the cancellation option.",

    "delivery":
        "Delivery time depends on the product, seller, and delivery location. You can check the estimated delivery date in your order details.",

    "damaged_product":
        "If your product arrived damaged, report the issue through the order support section and provide details about the damage.",

    "wrong_product":
        "If you received the wrong product, report the issue through the order support section and provide your order details.",

    "payment":
        "Available payment methods are displayed during checkout.",

    "account":
        "You can manage your account information, password, and contact details from your account settings.",

    "product_information":
        "You can find product specifications, features, and other information on the product details page.",

    "technical_issue":
        "Please try refreshing the page or restarting the application. If the problem continues, contact customer support."
}


data = []

# Generate variations
for category, questions in categories.items():

    for question in questions:

        variations = [
            question,
            question.lower(),
            question.replace("?", ""),
            "Please help me. " + question,
            "I need help with this. " + question,
            "Can you help me? " + question,
            "I have a question: " + question,
            "Could you please tell me, " + question.lower(),
            "I would like to know, " + question.lower(),
            "Please tell me " + question.lower().replace("?", "")
        ]

        for variation in variations:

            data.append({
                "instruction": variation,
                "input": "",
                "output": responses[category],
                "category": category
            })


# Shuffle dataset
random.shuffle(data)

# Remove duplicate instructions
unique_data = []
seen = set()

for item in data:

    instruction = item["instruction"].strip().lower()

    if instruction not in seen:
        seen.add(instruction)
        unique_data.append(item)


# Create folders
os.makedirs("data/processed", exist_ok=True)


# Save dataset
output_file = "data/processed/ecommerce_chatbot_dataset.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(
        unique_data,
        file,
        indent=2,
        ensure_ascii=False
    )


print("Dataset created successfully!")
print("Number of examples:", len(unique_data))
print("Categories:", len(categories))
print("Saved to:", output_file)