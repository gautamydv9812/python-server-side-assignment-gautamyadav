import json

# Load the JSON file
with open('products.json', 'r') as file:
    products = json.load(file)

# Display header
print(f"{'Name':<15} {'Price':<10} {'Quantity':<10}")
print("-" * 35)

# Display each product
for product in products:
    print(f"{product['name']:<15} {product['price']:<10} {product['quantity']:<10}")
