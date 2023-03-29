"""Module """
import json
import os
from pathlib import Path
from datetime import datetime, date
from uc3m_logistics.order_request import OrderRequest
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.order_shipping import OrderShipping

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """Este método devuelve (bool) si un string almacena un código EAN13"""
        if type(ean13_code) is not str:
            raise OrderManagementException("EAN13 not string")
        lista = "0123456789"
        for n in range(len(ean13_code)):
            if ean13_code[n] not in lista:
                raise OrderManagementException("Error. Contiene caracteres no numéricos")
        # Si la longitud del código no es 13, entonces no es de tipo EAN13
        if len(ean13_code) > 13:
            raise OrderManagementException("EAN13 mayor a 13 cifras")
        if len(ean13_code) < 13:
            raise OrderManagementException("EAN13 menor a 13 cifras")
        # Sumamos los números de las posiciones pares (menos la número 13)
        pares = 0
        for number in range(0, 6):
            pares += int(ean13_code[2 * number])
        # Lo mismo pero ahora con todos los de las impares
        impares = 0
        for number in range(0, 6):
            impares += int(ean13_code[2 * number + 1])
        # Sumamos los pares con los impares multiplicados por 3 (ponderados)
        suma = pares + impares*3
        # Tenemos que comprobar que la diferencia del multiplo de 10 más
        # cercano a suma por arriba y suma sea igual que el ultimo digito
        # de ean13
        # Comprobemos el caso de que esa diferencia sea 0
        modulo = suma % 10
        if modulo == 0:
            num = modulo
        else:
            num = 10 - modulo
        if num == int(ean13_code[12]):
            return True
        else:
            raise OrderManagementException("No cumple el checksum")

    @staticmethod
    def validate_address(address):
        if type(address) is not str:
            raise OrderManagementException("Address not string")
        if len(address) > 100:
            raise OrderManagementException("Dirección más larga de lo habitual")
        if len(address) < 20:
            raise OrderManagementException("Dirección más corta de lo habitual")
        num_espacios = 0
        for n in range(0, len(address)):
            if address[n] == " ":
                num_espacios += 1
        if num_espacios < 1:
            raise OrderManagementException("Insuficientes espacios")
        return True

    @staticmethod
    def validate_phone_number(phone_number):
        if type(phone_number) is not str:
            raise OrderManagementException("Phone_number not str")
        lista = "0123456789"
        for n in range(len(phone_number)):
            if phone_number[n] not in lista:
                raise OrderManagementException("Error. Contiene caracteres no numéricos")
        if len(phone_number) < 9:
            raise OrderManagementException("Phone_number más corto de 9 cifras")
        if len(phone_number) > 9:
            raise OrderManagementException("Phone_number más largo de 9 cifras")
        return True

    @staticmethod
    def validate_order_type(order_type):
        if type(order_type) is not str:
            raise OrderManagementException("Order_type not str")
        if order_type not in ["REGULAR", "PREMIUM"]:
            raise OrderManagementException("Order_type no es REGULAR o PREMIUM")
        return True

    @staticmethod
    def validate_zip_code(zip_code):
        if type(zip_code) is not str:
            raise OrderManagementException("Zip_code not str")
        lista = "0123456789"
        for n in range(len(zip_code)):
            if zip_code[n] not in lista:
                raise OrderManagementException("Error. Contiene caracteres no numéricos")
        if len(zip_code) < 5:
            raise OrderManagementException("Zip_code más corto de 5 cifras")
        if len(zip_code) > 5:
            raise OrderManagementException("Zip_code más largo de 5 cifras")
        cifras = int(zip_code[0:2])
        if 0 == cifras or cifras > 52:
            raise OrderManagementException("Las dos cifras iniciales deben estar entre 01 y 52")
        return True

    @staticmethod
    def register_order(product_id, order_type, address, phone, zip_code):
        OrderManager.validate_ean13(product_id)
        OrderManager.validate_order_type(order_type)
        OrderManager.validate_phone_number(phone)
        OrderManager.validate_address(address)
        OrderManager.validate_zip_code(zip_code)
        my_order = OrderRequest(product_id, order_type, address, phone, zip_code)
        order_id = my_order.order_id
        OrderManager.crear_pedido(product_id, order_type, address, phone, zip_code, order_id)
        OrderManager.almacenar_pedido(product_id, order_type, address, phone, zip_code, order_id)
        return order_id

    @staticmethod
    def crear_pedido(product_id, order_type, address, phone, zip_code, order_id):
        order = {"product_id": product_id, "order_type": order_type, "address": address, "phone": phone,
                 "zip_code": zip_code, "OrderID": order_id}
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "pedido.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        with open(file_store, mode="w", encoding="UTF-8") as file:
            json.dump(order, file, indent=4)

    @staticmethod
    def almacenar_pedido(product_id, order_type, address, phone, zip_code, order_id):
        order = {"product_id": product_id, "order_type": order_type, "address": address, "phone": phone,
                 "zip_code": zip_code, "OrderID": order_id}
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "storage.json"
        if os.path.isfile(file_store) is False:
            with open(file_store, mode="w", encoding="UTF-8") as file:
                listorder = [order]
                json.dump(listorder, file, indent=4)
        else:
            with open(file_store, mode="r", encoding = "UTF-8") as file:
                data_file = json.load(file)
                for item in data_file:
                    if item["OrderID"] == order["OrderID"]:
                        raise OrderManagementException("Producto ya existente en el almacén.")
                data_file.append(order)
            os.remove(file_store)
            with open(file_store, mode="w", encoding = "UTF-8") as file:
                json.dump(data_file, file, indent=4)

    @staticmethod
    def validate_json(input_file):
        try:
            with open(input_file, mode ='r', encoding="UTF-8") as file:
                datos = json.load(file)
                print(datos)
                # Para comprobar si el formato de las claves es correcto
                claves = list(datos.keys())
                if claves != ["OrderID", "ContactEmail"]:
                    raise OrderManagementException("Estructura del fichero incorrecta")
                # Para comprobar si el formato de order_id es correcto
                order_id = datos["OrderID"]
                if len(order_id) != 32:
                    raise OrderManagementException("OrderID invalido")
                caracteres_hex = "0123456789abcdef"
                for i in range(len(order_id)):
                    if order_id[i] not in caracteres_hex:
                        raise OrderManagementException("OrderID invalido")
                # Para comprobar si el formato de ContactEmail es correcto
                email = datos["ContactEmail"]
                # Comprobamos si tiene @ y si el formato entre el inicio del mail
                # y esta es correcto
                caracteres_validos = "qwertyuiopasdfghjklñzxcvbnm0123456789"
                caracteres_validos_ext = "qwertyuiopasdfghjklñzxcvbnm"
                tiene_at = False
                posicion_at = 0
                for i in range(len(email)):
                    if email[i] == "@":
                        tiene_at = True
                        posicion_at = i
                        break
                if tiene_at:
                    email_bef_at = email[0:posicion_at]
                    if len(email_bef_at) == 0:
                        raise OrderManagementException("ContactEmail invalido")
                    for i in range(len(email_bef_at)):
                        if email_bef_at[i] not in caracteres_validos:
                            raise OrderManagementException("ContactEmail invalido")
                else:
                    raise OrderManagementException("ContactEmail invalido")
                # Comprobamos si tiene punto despues del arroba y si el formato entre
                # el @ y el punto es correcto
                # email_aft_at = email[posicion_at + 1:]
                tiene_punto = False
                posicion_punto = 0
                for i in range(len(email)):
                    if email[i] == ".":
                        posicion_punto = i
                        tiene_punto = True
                        break
                if tiene_punto:
                    email_bef_p = email[posicion_at + 1:posicion_punto]
                    if len(email_bef_p) == 0:
                        raise OrderManagementException("ContactEmail invalido")
                    for i in range(len(email_bef_p)):
                        if email_bef_p[i] not in caracteres_validos:
                            raise OrderManagementException("ContactEmail invalido")
                else:
                    raise OrderManagementException("ContactEmail invalido")
                # Comprobamos si la extension tiene el formato correcto
                email_aft_p = email[posicion_punto + 1:]
                if len(email_aft_p) > 3:
                    raise OrderManagementException("ContactEmail invalido")
                for i in range(len(email_aft_p)):
                    if email_aft_p[i] not in caracteres_validos_ext:
                        raise OrderManagementException("ContactEmail invalido")
        except FileNotFoundError as ex:
            raise OrderManagementException("Archivo no encontrado") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - El archivo no tiene formato JSON") from ex

    @staticmethod
    def comprobar_pedido(input_file, storage_file) -> list:
        # Como ya se ha validado el fichero podemos abrirlo sin
        # realizar comprobaciones del mismo
        with open(input_file, mode ='r', encoding="UTF-8") as file:
            datos = json.load(file)
            order_id = datos["OrderID"]
        with open(storage_file, mode = 'r', encoding="UTF-8") as file:
            storage = json.load(file)
            encontrado = False
            for pedido in storage:
                if pedido["OrderID"] == order_id:
                    encontrado = True
                    break
            if encontrado:
                return [pedido["product_id"], pedido["order_type"]]
            raise OrderManagementException("Pedido no encontrado u OrderID manipulado")

    @staticmethod
    def almacenar_envio(tracking_code, delivery_day):
        order = {"tracking_code": tracking_code, "delivery_day": delivery_day}
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "shipping_storage.json"
        if os.path.isfile(file_store) is False:
            with open(file_store, mode="w", encoding="UTF-8") as file:
                listorder = [order]
                json.dump(listorder, file, indent=4)
        else:
            with open(file_store, mode="r", encoding="UTF-8") as file:
                data_file = json.load(file)
                for item in data_file:
                    if item["tracking_code"] == order["tracking_code"]:
                        raise OrderManagementException("Envío ya existente en el almacén.")
                data_file.append(order)
            os.remove(file_store)
            with open(file_store, mode="w", encoding="UTF-8") as file:
                json.dump(data_file, file, indent=4)

    @staticmethod
    def send_product(input_file):
        storage = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/" + "storage.json"
        OrderManager.validate_json(input_file)
        datos = OrderManager.comprobar_pedido(input_file, storage)
        # Para generar order_shipping
        with open(input_file, mode ='r', encoding="UTF-8") as file:
            datos = json.load(file)
            order_id = datos["OrderID"]
            delivery_email = datos["ContactEmail"]
        product_id = datos[0]
        order_type = datos[1]
        my_order_shipping = OrderShipping(product_id, order_id, delivery_email, order_type)
        tracking_code = my_order_shipping.tracking_code
        delivery_day = my_order_shipping.delivery_day
        OrderManager.almacenar_envio(tracking_code, delivery_day)
        return tracking_code

    @staticmethod
    def comprobar_envio(tracking_code, storage):
        try:
            # Primero comprobamos que existe el tracking_code
            with open(storage, mode='r', encoding="UTF-8") as file:
                datos = json.load(file)
                encontrado = False
                for envio in datos:
                    if envio["tracking_code"] == tracking_code:
                        encontrado = True
                        break
                if not encontrado:
                    # No se ha encontrado el tracking_code (es decir, el envio) en el almacén
                    raise OrderManagementException("Envío no encontrado en el almacén")
                # Ahora comprobamos que la fecha de envío coincide con la fecha actual
                delivery_day = envio["delivery_day"]
                delivery_day_date = datetime.fromtimestamp(delivery_day).date()
                fecha_actual = date.today()
                if fecha_actual == delivery_day_date:
                    # devolvemos el deliver_day timestamp
                    return delivery_day
                raise OrderManagementException("La fecha de entrega no es correcta")
        except FileNotFoundError as ex:
            raise OrderManagementException("El almacén esta vacío") from ex

    @staticmethod
    def almacenar_entrega(tracking_code, delivery_day):
        order = {"tracking_code": tracking_code, "delivery_day": delivery_day}
        dir = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/"
        file_store = dir + "delivery_storage.json"
        if os.path.isfile(file_store) is False:
            with open(file_store, mode="w", encoding="UTF-8") as file:
                listorder = [order]
                json.dump(listorder, file, indent=4)
        else:
            with open(file_store, mode="r", encoding="UTF-8") as file:
                data_file = json.load(file)
                for item in data_file:
                    if item["tracking_code"] == order["tracking_code"]:
                        raise OrderManagementException("Entrega ya existente en el almacén.")
                data_file.append(order)
            os.remove(file_store)
            with open(file_store, mode="w", encoding="UTF-8") as file:
                json.dump(data_file, file, indent=4)

    @staticmethod
    def deliver_product(tracking_code):
        # Comprobamos que el tracking_code tiene un formato correcto
        caracteres_hex = "0123456789abcdef"
        if type(tracking_code) is not str:
            raise OrderManagementException("Tracking_code no es un string")
        if len(tracking_code) != 64:
            raise OrderManagementException("Tracking_code no tiene la longitud adecuada")
        for i in range(len(tracking_code)):
            if tracking_code[i] not in caracteres_hex:
                raise OrderManagementException("Tracking_code contiene caracteres no hexadecimales")
        # Comprobamos mediante una funcion si el envío está en el almacen y la fecha es correcta y si es asi
        # se devolvera la fecha de entrega
        storage = str(Path.home()) + "/PycharmProjects/G81.2023.T04.EG3/src/Jsonfiles/" + "shipping_storage.json"
        delivery_day = OrderManager.comprobar_envio(tracking_code, storage)
        OrderManager.almacenar_entrega(tracking_code, delivery_day)



