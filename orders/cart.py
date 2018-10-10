from django.conf import settings

class Cart(object):
    """
    A cart which lives in a session
    """
    def __init__(self, session, session_key=None):
        self._items_dict = {}
        self.session = session
        self.session_key = session_key # or get session key from settings

    def __contains__(self, product):
        """
        Checks if product is in the cart.
        """
        return product in self.products

    def add(self, product, price= None, quantity= 1):
        if quantity < 1:
            raise ValueError('Quantity must be at least 1 when adding to cart.')
        else:
            if price == None:
                raise ValueError('Missing price for item being added to cart.')
            self._items_dict[product.pk] = CartItem(product, quantity, price)
        self.update_session()