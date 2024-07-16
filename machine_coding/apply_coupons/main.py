from product import Product
from coupon import *
from cart import ShoppingCart

# Create products
product1 = Product("Laptop", 1000, "Electronics")
product2 = Product("Chair", 200, "Furniture")

# Create coupons
coupon1 = PercentageOffCoupon(10)  # 10% off
coupon2 = FixedAmountOffCoupon(50)  # $50 off

# Create shopping cart and add products and coupons
cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_coupon(coupon1)
cart.add_coupon(coupon2)

# Calculate total price after applying coupons
total_price = cart.calculate_total()
print(f"Total price after applying coupons: ${total_price}")
