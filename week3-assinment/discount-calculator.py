# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price  # No discount if less than 20%

# Prompt user for inputs
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    if discount_percent >= 20:
        print(f"The final price after {discount_percent}% discount is: {final_price}")
    else:
        print(f"No discount applied. The price remains: {final_price}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
