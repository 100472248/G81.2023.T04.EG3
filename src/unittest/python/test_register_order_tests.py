"""class for testing the regsiter_order method"""
import unittest
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderRequest
from uc3m_logistics import OrderManagementException

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def test_something( self ):
        """dummy test"""
        self.assertEqual(True, True)

    def Test_EAN13(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID", "123456789", "28005")
        self.assertEqual(frase, str(value))
    def Test_EAN13notNumber(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("842169142322A", "REGULAR", "C/LISBOA, 4, MADRID", "123456789", "28005")
        self.assertEqual("Error. Contiene caracteres no numéricos", invalido.exception.message)





if __name__ == '__main__':
    unittest.main()
