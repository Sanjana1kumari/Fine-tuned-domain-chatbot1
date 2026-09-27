import json
import os

# Training examples
data = [
    {
        "instruction": "Where is my order?",
        "input": "",
        "output": "You can check your order status and tracking information from the order details section.",
        "category": "order_tracking"
    },
    {
        "instruction": "How can I track my order?",
        "input": "",
        "output": "You can check your order status and tracking information from the order details section.",
        "category": "order_tracking"
    },
    {
        "instruction": "Can I track my package?",
        "input": "",
        "output": "Yes. Open your order details to view the latest tracking information.",
        "category": "order_tracking"
    },
    {
        "instruction": "My order has not arrived yet.",
        "input": "",
        "output": "Please check the estimated delivery date and tracking information in your order details.",
        "category": "order_tracking"
    },

    {
        "instruction": "How can I return a product?",
        "input": "",
        "output": "You can request a return for an eligible product through your order details. Select the return option and follow the instructions.",
        "category": "return"
    },
    {
        "instruction": "I want to return my order.",
        "input": "",
        "output": "You can request a return for an eligible product through your order details. Select the return option and follow the instructions.",
        "category": "return"
    },
    {
        "instruction": "Can I return an item?",
        "input": "",
        "output": "Eligible products can be returned through the return option in your order details.",
        "category": "return"
    },

    {
        "instruction": "How do I get a refund?",
        "input": "",
        "output": "Once an eligible return is approved and processed, the refund will be issued according to the applicable refund policy.",
        "category": "refund"
    },
    {
        "instruction": "Where is my refund?",
        "input": "",
        "output": "Please check your refund status in your order details. Processing time depends on the applicable refund policy.",
        "category": "refund"
    },
    {
        "instruction": "When will I receive my refund?",
        "input": "",
        "output": "Refund processing time depends on the payment method and applicable refund policy.",
        "category": "refund"
    },

    {
        "instruction": "Can I cancel my order?",
        "input": "",
        "output": "You can cancel an order if it has not been shipped yet. Open your order details and select the cancellation option.",
        "category": "cancellation"
    },
    {
        "instruction": "I want to cancel my purchase.",
        "input": "",
        "output": "You can cancel an order if it has not been shipped yet through your order details.",
        "category": "cancellation"
    },

    {
        "instruction": "How long does delivery take?",
        "input": "",
        "output": "Delivery time depends on the product, seller, and delivery location. You can check the estimated delivery date in your order details.",
        "category": "delivery"
    },
    {
        "instruction": "When will my order arrive?",
        "input": "",
        "output": "You can find the estimated delivery date in your order details.",
        "category": "delivery"
    },
    {
        "instruction": "My delivery is delayed.",
        "input": "",
        "output": "Please check your order tracking information for the latest delivery status and estimated arrival date.",
        "category": "delivery"
    },

    {
        "instruction": "My product arrived damaged.",
        "input": "",
        "output": "If your product arrived damaged, report the issue through the order support section and provide details about the damage.",
        "category": "damaged_product"
    },
    {
        "instruction": "I received a damaged item.",
        "input": "",
        "output": "Please report the damaged product through the order support section and provide details about the damage.",
        "category": "damaged_product"
    },

    {
        "instruction": "I received the wrong product.",
        "input": "",
        "output": "If you received the wrong product, report the issue through the order support section and provide your order details.",
        "category": "wrong_product"
    },
    {
        "instruction": "The item I received is incorrect.",
        "input": "",
        "output": "Please report the incorrect product through the order support section and provide your order details.",
        "category": "wrong_product"
    },

    {
        "instruction": "What payment methods are available?",
        "input": "",
        "output": "Available payment methods depend on the platform and order. You can view the available payment options during checkout.",
        "category": "payment"
    },
    {
        "instruction": "Can I pay using a card?",
        "input": "",
        "output": "You can use a card if card payment is available for your order during checkout.",
        "category": "payment"
    },
    {
        "instruction": "Do you accept credit cards?",
        "input": "",
        "output": "Available payment methods are displayed during checkout.",
        "category": "payment"
    }
]


# Create output directory if it does not exist
os.makedirs("data/processed", exist_ok=True)

# Save dataset
output_file = "data/processed/ecommerce_chatbot_dataset.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("Dataset created successfully!")
print("Number of examples:", len(data))
print("Saved to:", output_file)