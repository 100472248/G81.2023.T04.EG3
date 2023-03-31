"""..."""
import unittest
import os
from pathlib import Path
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time


class MyTestRF2(unittest.TestCase):
    """Tests del ejercicio f2"""

    @classmethod
    def setUpClass(cls) -> None:
        direction = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = direction + "shipping_storage.json"
        if os.path.isfile(file_store):
            os.remove(file_store)


    @freeze_time("2023-03-24")
    def test_node1_valid(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node1_valid.json"
        my_order = OrderManager()
        value = my_order.send_product(path_test)
        self.assertEqual("872d9d44c0c2f6fe7f67a8009de43641"
                         "7b8780861e3184e73d8795b9faa6af8d", str(value))

    def test_node1_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node1_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node1_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node1_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node2_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node2_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node2_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node2_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node3_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node3_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node3_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node3_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("Estructura del fichero incorrecta", invalido.exception.message)

    def test_node4_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node4_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node4_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node4_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node5_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src" \
                                       "/Jsonfiles/tests_rf2/" + "node5_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node6_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node6_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node6_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node6_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node7_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node7_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node7_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node7_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node9_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node9_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node10_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node10_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node10_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node10_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node11_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node11_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node11_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node11_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node12_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node12_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node12_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node12_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node13_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node13_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node17_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node17_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node17_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node17_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node18_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node18_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("Estructura del fichero incorrecta", invalido.exception.message)

    def test_node18_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node18_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("Estructura del fichero incorrecta", invalido.exception.message)

    def test_node20_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node20_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node22_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node22_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("OrderID invalido", invalido.exception.message)

    def test_node22_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node22_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("OrderID invalido", invalido.exception.message)

    def test_node25_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node25_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("Estructura del fichero incorrecta", invalido.exception.message)

    def test_node25_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node25_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("Estructura del fichero incorrecta", invalido.exception.message)

    def test_node29_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node29_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node29_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node29_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node31_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node31_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - "
                         "El archivo no tiene formato JSON", invalido.exception.message)

    def test_node32_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node32_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("Estructura del fichero incorrecta", invalido.exception.message)

    def test_node35_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node35_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("OrderID invalido", invalido.exception.message)

    def test_node38_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node38_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("Estructura del fichero incorrecta", invalido.exception.message)

    def test_node41_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node41_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node42_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node42_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node42_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node42_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node43_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node43_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node44_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node44_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node44_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node44_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node45_dup(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node45_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node45_del(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node45_del.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node46_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node46_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node47_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node47_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node48_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node48_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node49_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node49_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_node50_mod(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "node50_mod.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("ContactEmail invalido", invalido.exception.message)

    def test_orderid_notstring(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "nv3.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("OrderID invalido", invalido.exception.message)

    def test_orderid_vl1(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "vl1.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("OrderID invalido", invalido.exception.message)

    def test_orderid_vl3(self):
        """..."""
        path_test = str(Path.home()) + "/PycharmProjects/" \
                                       "G81.2023.T04.EG3/src/" \
                                       "Jsonfiles/tests_rf2/" + "vl3.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            my_order.send_product(path_test)
        self.assertEqual("OrderID invalido", invalido.exception.message)


if __name__ == '__main__':
    unittest.main()
