"""Module """
from uc3m_logistics.order_request import OrderRequest
from uc3m_logistics.order_management_exception import OrderManagementException

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """Este método devuelve (bool) si un string almacena un código EAN13"""
        if ean13_code is not str:
            raise OrderManagementException("EAN13 not string")
        lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for n in range(0, len(ean13_code)):
            if ean13_code[n] not in lista:
                raise OrderManagementException("Error. Contiene caracteres no numéricos")
        # Si la longitud del código no es 13, entonces no es de tipo EAN13
        if len(ean13_code) > 13:
            raise OrderManagementException("EAN13 menor a 13 cifras")
        if len(ean13_code) < 13:
            raise OrderManagementException("EAN13 mayor a 13 cifras")
        # Sumamos los números de las posiciones pares (menos la número 13)
        pares = 0
        for number in range(0, 6):
            pares += int(ean13_code[2 * number])
        # Lo mismo pero ahora con todos los de las impares
        impares = 0
        for number in range(0, 6):
            impares += int(ean13_code[2 * number + 1])
        # Sumamos los pares con los impares multiplicados por 3 (ponderados)
        impares = impares * 3
        suma = pares + impares
        # Tenemos que comprobar que la diferencia del multiplo de 10 más
        # cercano a suma por arriba y suma sea igual que el ultimo digito
        # de ean13
        # Comprobemos el caso de que esa diferencia sea 0
        modulo = suma % 10
        if modulo == 0:
            return int(ean13_code[12]) == modulo
        # Veamos si es distinto de 0
        num = 10 - modulo
        if num != int(ean13_code[12]):
            return False
        return True

    @staticmethod
    def validate_address(address):
        if address is not str:
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
        if phone_number is not str:
            raise OrderManagementException("Phone_number not str")
        lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for n in range(0, len(phone_number)):
            if phone_number[n] not in lista:
                raise OrderManagementException("Error. Contiene caracteres no numéricos")
        if len(phone_number) < 9:
            raise OrderManagementException("Phone_number más corto de 9 cifras")
        if len(phone_number) > 9:
            raise OrderManagementException("Phone_number más largo de 9 cifras")
        return True

    @staticmethod
    def validate_order_type(order_type):
        if order_type is not str:
            raise OrderManagementException("Order_type not str")
        if order_type != "REGULAR" and order_type != "PREMIUM":
            raise OrderManagementException("Order_type no es REGULAR o PREMIUM")
        return True

    @staticmethod
    def validate_zip_code(zip_code):
        if zip_code is not str:
            raise OrderManagementException("Zip_code not str")
        lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for n in range(0, len(zip_code)):
            if zip_code[n] not in lista:
                raise OrderManagementException("Error. Contiene caracteres no numéricos")
        if len(zip_code) < 5:
            raise OrderManagementException("Zip-code más corto de 5 cifras")
        if len(zip_code) > 5:
            raise OrderManagementException("Zip_code más largo de 5 cifras")
        cifras = int(zip_code[0:2])
        if 0 == cifras or cifras > 52:
            raise OrderManagementException("Las dos cifras iniciales deben estar entre 01 y 52")
        return True

    def register_order(self, product_id, order_type, address, phone, zip_code):
        self.validate_ean13(product_id)
        self.validate_order_type(order_type)
        self.validate_phone_number(phone)
        self.validate_address(address)
        self.validate_zip_code(zip_code)
        my_order = OrderRequest(product_id, order_type, address, phone, zip_code)
        return str(my_order)

