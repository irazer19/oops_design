from product import Product
from cart import Cart


def run():
    """
    We use Decorator design pattern to apply coupons sequentially.
    """
    iphone = Product(product_name="iPhone 14", price=1400)
    chair = Product(product_name="Chair", price=300)

    cart = Cart([])
    cart.add_product(iphone, prod_type="Phone")
    cart.add_product(chair, prod_type="Furniture")
    print(cart.get_total_price())

    pass


if __name__ == "__main__":
    run()
