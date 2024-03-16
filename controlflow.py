def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    final_price = price * (1 - discount_percent / 100)
    return final_price
  else:
    return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (as a percentage): "))

# Calculate the final price after applying the discount
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price == price:
  print("No discount was applied. The original price is: ", price)
else:
  print("The final price after applying the discount is: ", final_price)