"""class for testing the regsiter_order method"""
import unittest
import os
import json
from pathlib import Path
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""

    def test_something(self):
        """dummy test"""
        self.assertEqual(True, True)

    @freeze_time("2023-03-24")
    def test_all_correct(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR",
                                        "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("caf7eace516dced5512b338105303c83", str(value))

    def test_EAN13notString(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order(12, "REGULAR",
                                            "C/LISBOA, 4, MADRID, SPAIN", "123456789","28005")
        self.assertEqual("EAN13 not string", invalido.exception.message)

    def test_EAN13notNumber(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("codigoean13", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Error. Contiene caracteres no numéricos", invalido.exception.message)

    def test_EAN13Corto(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("842169142322", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("EAN13 menor a 13 cifras", invalido.exception.message)

    def test_EAN13Largo(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("84216914232256", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("EAN13 mayor a 13 cifras", invalido.exception.message)

    def test_notCheckSum(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423229", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("No cumple el checksum", invalido.exception.message)

    def test_VL1(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("84216914232256", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("EAN13 mayor a 13 cifras", invalido.exception.message)

    @freeze_time("2023-03-24")
    def test_VL2(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("caf7eace516dced5512b338105303c83", str(value))

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

    @freeze_time("2023-03-24")
    def test_order_REGULAR(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("caf7eace516dced5512b338105303c83", str(value))

    @freeze_time("2023-03-24")
    def test_order_PREMIUM(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("5eb1585d426fdc862df27075c9d34d93", str(value))

    def test_orderNoCorrecto(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "INVALIDO", "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Order_type no es REGULAR o PREMIUM", invalido.exception.message)

    def test_address_str(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "REGULAR", 789, "123456789", "28005")
        self.assertEqual("Address not string", invalido.exception.message)

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

    @freeze_time("2023-03-24")
    def test_VL5(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/VALENCIA, 4, MADRID", "123456789", "28005")
        self.assertEqual("1833da081e1e79e808f8c2e8377cbc49", str(value))

    @freeze_time("2023-03-24")
    def test_VL6(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/ALICANTE, 4, MADRID", "123456789", "28005")
        self.assertEqual("7678fd535c44f8aaf78f47c9effb4c0b", str(value))

    @freeze_time("2023-03-24")
    def test_VL7(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR",
                                        "AVENIDA VILLAVICIOSA DEL OBISPO DE GUADALAJARA,102, TORDESILLAS, VALLADOLID, CASTILLA Y LEÓN, SPAIN",
                                        "123456789", "28005")
        self.assertEqual("44707b5308285f825f0bbd8264973221", str(value))

    @freeze_time("2023-03-24")
    def test_VL8(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR",
                                        "AVENIDA VILLAVICIOSA DEL OBISPO DE GUADALAJARA,102, TORDESILLAS, VALLADOLID, CASTILLA Y LEÓN, SPAIN",
                                        "123456789", "28005")
        self.assertEqual("44707b5308285f825f0bbd8264973221", str(value))

    def test_VL9(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM",
                                            "AVENIDA VILLANUEVA DEL ARZOBISPO DE GUADALAJARA,102, TORDESILLAS, VALLADOLID, CASTILLA Y LEÓN, ESPAÑA",
                                            "123456789", "28005")
        self.assertEqual("Dirección más larga de lo habitual", invalido.exception.message)

    def test_phone_not_str(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN", 123456789,
                                            "28005")
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

    def test_VL10(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "1234567890", "28005")
        self.assertEqual("Phone_number más largo de 9 cifras", invalido.exception.message)

    @freeze_time("2023-03-24")
    def test_VL11(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("caf7eace516dced5512b338105303c83", str(value))

    def test_VL12(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "12345678", "28005")
        self.assertEqual("Phone_number más corto de 9 cifras", invalido.exception.message)

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

    @freeze_time("2023-03-24")
    def test_VL14(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        print(value)
        self.assertEqual("caf7eace516dced5512b338105303c83", str(value))

    def test_VL15(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "280050")
        self.assertEqual("Zip_code más largo de 5 cifras", invalido.exception.message)

    @freeze_time("2023-03-24")
    def test_Salida_MDL5(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA, 4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("caf7eace516dced5512b338105303c83", str(value))

    def test_exception_EAN13(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("842169142322", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "28005")
        self.assertNotEqual(True, invalido.exception.message, "Exception. Product_id not valid")

    def test_exception_order_id(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PR", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "28005")
        self.assertNotEqual(True, invalido.exception.message, "Exception. Order_type not valid")

    def test_exception_address(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID",
                                            "123456789", "28005")
        self.assertNotEqual(True, invalido.exception.message, "Exception. Address wrong")

    def test_exception_phone_number(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "12345678", "28005")
        self.assertNotEqual(True, invalido.exception.message, "Exception. Phone number wrong")

    def test_exception_zip_code(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA, 4, MADRID, SPAIN",
                                            "123456789", "280050")
        self.assertNotEqual(True, invalido.exception.message, "Exception. Phone number wrong")
"""
    @freeze_time("2023-03-24")
    def test_file_created(self):
        datos = {"product_id": "8421691423220", "order-id": "REGULAR", "address": "C/LISBOA, 4, MADRID, SPAIN",
                 "phone_number": "123456789", "zip_code": "28005"}
        datos["_OrderRequest__order_id"] = OrderManager.register_order("8421691423220", "REGULAR",
                                                                       "C/LISBOA, 4, MADRID, SPAIN", "123456789",
                                                                       "28005")
        dir = "C:/Users/jaime/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles"
        file_name = "f1.json"
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(datos, file)
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = JSON_FILES_PATH + file_name
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        if data_list["_OrderRequest__order_id"] == "caf7eace516dced5512b338105303c83":
            found = True
        self.assertTrue(found)
"""



if __name__ == '__main__':
    unittest.main()

