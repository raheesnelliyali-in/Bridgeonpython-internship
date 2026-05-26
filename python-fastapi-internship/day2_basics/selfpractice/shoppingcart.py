print("      SHOPPING CART")
cart = [("Shirt", 550),("Jeans", 800),("Shoes", 950),("shocks", 100)]
total = sum(price for item, price in cart)
print(f"Total Amount   : ₹{total}")
discount = 0
if total > 500:
    discount=total* 0.10
final_amount=total - discount
print(f"Discount (10%) : ₹{discount}")
for item, price in cart:
    print(f"{item:<10} : ₹{price}")
print(f"Payable Amount : ₹{final_amount}")