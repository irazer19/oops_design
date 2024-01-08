from coupon import PercentageCoupon, TypeCoupon


class Cart:
    def __init__(self, products):
        self.products = products

    def add_product(self, product, prod_type):
        prod = TypeCoupon(
            prod_type=prod_type,
            product=PercentageCoupon(percentage=10, product=product),
        )

        self.products.append(prod)

    def get_total_price(self):
        total_price = 0

        for product in self.products:
            total_price += product.get_price()
        return total_price
