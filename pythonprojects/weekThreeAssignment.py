def calculate_discount(price, discount_percent):
#Applies discount if 20% or higher; otherwise, returns original price.
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    return price

# input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate 
final_price = calculate_discount(price, discount_percent)

# Display 
if discount_percent >= 20:
    print(f"Final price after applying {discount_percent}% discount: {final_price}")
else:
    print(f"No discount applied. Price remains: {price}")