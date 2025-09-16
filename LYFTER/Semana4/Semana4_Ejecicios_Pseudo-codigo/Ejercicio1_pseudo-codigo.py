
price = float(input("Enter the product price: "))

if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10

final_price = price - discount

print(f"This is your price with discount: {final_price:.2f}")