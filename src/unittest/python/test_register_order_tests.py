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
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
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

    def test_VL1(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("84216914232256", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("EAN13 mayor a 13 cifras", invalido.exception.message)


    def test_VL2(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual(frase, str(value))

    def test_VL3(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("842169142322", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("EAN13 menor a 13 cifras", invalido.exception.message)

    def test_order_str(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", 23, "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Order_type not str", invalido.exception.message)

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

    def test_address_str(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "REGULAR", 789, "123456789","28005")
        self.assertEqual("Address not string", invalido.exception.message)

    def test_address_correct(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual(frase, str(value))

    def test_address_too_long(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM",
                                            "AVENIDA VILLANUEVA DEL ARZOBISPO DE GUADALAJARA,102, TORDESILLAS, VALLADOLID, CASTILLA Y LEÓN, ESPAÑA",
                                            "123456789", "28005")
        self.assertEqual("Dirección más larga de lo habitual", invalido.exception.message)

    def test_address_too_short(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LOGROÑO,4, MADRID", "123456789", "28005")
        self.assertEqual("Dirección más corta de lo habitual", invalido.exception.message)

    def test_spaces(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4,MADRID", "123456789", "28005")
        self.assertEqual("Dirección más corta de lo habitual", invalido.exception.message)

    def VL4(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LOGROÑO,4, MADRID", "123456789", "28005")
        self.assertEqual("Dirección más corta de lo habitual", invalido.exception.message)

    def test_VL5(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/VALENCIA, 4, MADRID", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/VALENCIA, 4, MADRID", "123456789","28005")
        self.assertEqual(frase, str(value))

    def test_VL6(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/ALICANTE, 4, MADRID", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/ALICANTE, 4, MADRID", "123456789","28005")
        self.assertEqual(frase, str(value))

    def test_VL7(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR",
                                        "AVENIDA VILLAVICIOSA DEL OBISPO DE GUADALAJARA,102, TORDESILLAS, VALLADOLID, CASTILLA Y LEÓN, SPAIN",
                                        "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR",
                                            "AVENIDA VILLAVICIOSA DEL OBISPO DE GUADALAJARA,102, TORDESILLAS, VALLADOLID, CASTILLA Y LEÓN, SPAIN",
                                            "123456789","28005")
        self.assertEqual(frase, str(value))

    def test_VL8(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR",
                                        "AVENIDA VILLAVICIOSA DEL OBISPO DE GUADALAJARA,102, TORDESILLAS, VALLADOLID, CASTILLA Y LEÓN, SPAIN",
                                        "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR",
                                            "AVENIDA VILLAVICIOSA DEL OBISPO DE GUADALAJARA,102, TORDESILLAS, VALLADOLID, CASTILLA Y LEÓN, SPAIN",
                                            "123456789","28005")
        self.assertEqual(frase, str(value))

    def test_VL9(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM",
                                            "AVENIDA VILLANUEVA DEL ARZOBISPO DE GUADALAJARA,102, TORDESILLAS, VALLADOLID, CASTILLA Y LEÓN, ESPAÑA",
                                            "123456789", "28005")
        self.assertEqual("Dirección más larga de lo habitual", invalido.exception.message)

    def test_phone_valid(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual(frase, str(value))

    def test_phone_not_str(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN", 123456789, "28005")
        self.assertEqual("Phone_number not str", invalido.exception.message)

    def test_phone_numbers(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "12345678A", "28005")
        self.assertEqual("Error. Contiene caracteres no numéricos", invalido.exception.message)

    def test_phone_too_long(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "1234567890", "28005")
        self.assertEqual("Phone_number más largo de 9 cifras", invalido.exception.message)

    def test_phone_too_short(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "12345678", "28005")
        self.assertEqual("Phone_number más corto de 9 cifras", invalido.exception.message)

    def test_phone_too_long(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "1234567890", "28005")
        self.assertEqual("Phone_number más largo de 9 cifras", invalido.exception.message)

    def test_VL10(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "1234567890", "28005")
        self.assertEqual("Phone_number más largo de 9 cifras", invalido.exception.message)

    def test_VL11(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual(frase, str(value))

    def test_VL12(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "12345678", "28005")
        self.assertEqual("Phone_number más corto de 9 cifras", invalido.exception.message)

    def test_valid_zip(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual(frase, str(value))

    def test_zip_not_number(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", 28005)
        self.assertEqual("Zip_code not str", invalido.exception.message)

    def test_zip_numbers(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "2800C")
        self.assertEqual("Error. Contiene caracteres no numéricos", invalido.exception.message)

    def test_zip_short(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "2800")
        self.assertEqual("Zip_code más corto de 5 cifras", invalido.exception.message)

    def test_zip_long(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "280050")
        self.assertEqual("Zip_code más largo de 5 cifras", invalido.exception.message)

    def test_zip_initials(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "60005")
        self.assertEqual("Las dos cifras iniciales deben estar entre 01 y 52", invalido.exception.message)

    def test_VL13(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "2800")
        self.assertEqual("Zip_code más corto de 5 cifras", invalido.exception.message)

    def test_VL14(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        frase = OrderManager.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual(frase, str(value))

    def test_VL15(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "280050")
        self.assertEqual("Zip_code más largo de 5 cifras", invalido.exception.message)













if __name__ == '__main__':
    unittest.main()
