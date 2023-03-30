from datetime import datetime
import hashlib
import unittest
from uc3m_logistics import OrderManager
from pathlib import Path
import os
import json
from uc3m_logistics import OrderManagementException
from uc3m_logistics import OrderShipping
from freezegun import freeze_time


class MyTestRF3(unittest.TestCase):

    def test_tracking_code_not_str(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.deliver_product(123456789)
        self.assertEqual("Tracking_code no es un string", invalido.exception.message)

    def test_tracking_code_len_wrong(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.deliver_product("2a6b789e76f99988b")
        self.assertEqual("Tracking_code no tiene la longitud adecuada", invalido.exception.message)

    def test_tracking_code_not_hex(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.deliver_product("872d9d44c%c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d")
        self.assertEqual("Tracking_code no es un hex", invalido.exception.message)

    def test_empty_storage(self):
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "shipping_storage.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.deliver_product("872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d")
        self.assertEqual("El almacén esta vacío", invalido.exception.message)

    def test_shipping_not_found(self):
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "shipping_storage.json"
        if os.path.isfile(file_store):
            with open(file_store, mode='r+') as file:
                datos = json.load(file)
                for envio in datos:
                    if envio["tracking_code"] == "872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d":
                        datos.remove(envio)
        else:
            with open(file_store, mode='w') as file:
                json.dump([{"tracking_code": "", "delivery_day": ""}],file)
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.deliver_product("872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d")
        self.assertEqual("Envío no encontrado en el almacén", invalido.exception.message)

    def test_delivery_day_wrong(self):
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "shipping_storage.json"
        shipping = [{"tracking_code": "872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d",
                     "delivery_day": 12345}]
        if os.path.isfile(file_store):
            os.remove(file_store)
        with open(file_store, mode="w", encoding="UTF-8") as file:
            json.dump(shipping, file, indent=4)
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as invalido:
            value = my_order.deliver_product("872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d")
        self.assertEqual("La fecha de entrega no es correcta", invalido.exception.message)

    def test_valid_no_register(self):
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "shipping_storage.json"
        shipping = [{"tracking_code": "872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d",
                     "delivery_day": datetime.timestamp(datetime.utcnow())}]
        if os.path.isfile(file_store):
            os.remove(file_store)
        with open(file_store, mode="w", encoding="UTF-8") as file:
            json.dump(shipping, file, indent=4)
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "delivery_storage.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        my_order = OrderManager()
        value = my_order.deliver_product("872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d")
        self.assertEqual(True, value)

    def test_valid_with_register(self):
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "shipping_storage.json"
        shipping = [{"tracking_code": "872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d",
                     "delivery_day": datetime.timestamp(datetime.utcnow())}]
        if os.path.isfile(file_store):
            os.remove(file_store)
        with open(file_store, mode="w", encoding="UTF-8") as file:
            json.dump(shipping, file, indent=4)
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "delivery_storage.json"
        if os.path.isfile(file_store) is False:
            with open(file_store, mode="w", encoding="UTF-8") as file:
                listorder = [{}]
                json.dump(listorder, file, indent=4)
        my_order = OrderManager()
        value = my_order.deliver_product("872d9d44c0c2f6fe7f67a8009de436417b8780861e3184e73d8795b9faa6af8d")
        self.assertEqual(True, value)


if __name__ == '__main__':
    unittest.main()
