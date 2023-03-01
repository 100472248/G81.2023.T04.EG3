"""Module """
from uc3m_logistics.order_request import OrderRequest

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        return True

    def register_order(self, product_id, order_type, address, phone, zip_code):
        my_order = OrderRequest(product_id, order_type, address, phone, zip_code)
        return True

