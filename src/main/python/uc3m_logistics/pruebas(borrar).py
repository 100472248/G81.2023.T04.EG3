import os
import json
from pathlib import Path
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time

my_order = OrderManager()
my_order.validate_json(r"C:\Users\diazu\PycharmProjects\G81.2023.T04.EG3\src\Jsonfiles\pruebas.json")