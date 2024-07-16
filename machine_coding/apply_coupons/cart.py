class ShoppingCart:
    def __init__(self):
        self.products = []
        self.coupons = []

    def add_product(self, product):
        self.products.append(product)

    def add_coupon(self, coupon):
        self.coupons.append(coupon)

    def calculate_total(self):
        total = 0
        for product in self.products:
            price = product.get_price()
            for coupon in self.coupons:
                price = coupon.apply(product)
            total += price
        return total
