"""..."""
from unittest import TestCase
from uc3m_logistics.order_manager import OrderManager
from freezegun import freeze_time


class TestOrderManager(TestCase):
    """..."""

    @freeze_time("2023-03-01")
    def test_register_oder(self):
        """..."""
        my_manager = OrderManager()
        value = my_manager.register_order(product_id="3662168005326",
                                          order_type="regular", address="calle Leganés",
                                          phone="123456789", zip_code="28918")
        self.assertEqual("holas", value)
        self.fail()

    def test_product_id(self, ean13_code):
        """..."""
        my_manager = OrderManager
        value = my_manager.validate_ean13(ean13_code)
        self.assertEqual(True, value)
