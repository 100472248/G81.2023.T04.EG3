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

    def test_EAN13(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual(frase, str(value))

    def test_EAN13notString(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order(12, "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("EAN13 not string", invalido.exception.message)

    def test_EAN13notNumber(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("codigoean13", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Error. Contiene caracteres no numéricos", invalido.exception.message)

    def test_Corto(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("842169142322", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("EAN13 menor a 13 cifras", invalido.exception.message)

    def test_Largo(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("84216914232256", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("EAN13 mayor a 13 cifras", invalido.exception.message)

    def test_notCorrect(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423228", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Código no EAN13", invalido.exception.message)

    def test_order_REGULAR(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual(frase, str(value))

    def test_order_PRIVATE(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual(frase, str(value))

    def test_orderNoCorrecto(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "INVALIDO", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Order_type no es REGULAR o PREMIUM", invalido.exception.message)







if __name__ == '__main__':
    unittest.main()
