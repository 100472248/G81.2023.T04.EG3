import unittest
from uc3m_logistics import OrderManager
from pathlib import Path
import os
import json
from uc3m_logistics import OrderManagementException
from uc3m_logistics import OrderShipping
from freezegun import freeze_time

class MyTestRF2(unittest.TestCase):

    @freeze_time("2023-03-24")
    def test_node1_valid(self):
        path_test = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/tests_rf2/" + "node1_valid.json"
        my_order = OrderManager()
        value = my_order.send_product(path_test)
        self.assertEqual("872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d", str(value))

    def test_node1_dup(self):
        path_test = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/tests_rf2/" + "node1_dup.json"
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.send_product(path_test)
        self.assertEqual("JSON Decode Error - El archivo no tiene formato JSON", invalido.exception.message)





if __name__ == '__main__':
    unittest.main()