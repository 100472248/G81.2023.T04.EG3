from uc3m_logistics import OrderManager
from pathlib import Path
import os
import json
from uc3m_logistics import OrderManagementException
from uc3m_logistics import OrderShipping
from freezegun import freeze_time

lista_ficheros = ["node1_valid.json", "node1_dup.json", "node1_del.json", "node2_dup.json", "node2_del.json",
                  "node3_dup.json", "node3_del.json", "node4_dup.json", "node4_del.json", "node5_mod.json",
                  "node6_dup.json", "node6_del.json", "node7_dup.json", "node7_del.json", "node9_mod.json",
                  "node10_dup.json", "node10_del.json", "node11_dup.json", "node11_del.json", "node12_dup.json",
                  "node12_del.json", "node13_mod.json", "node17_dup.json", "node17_del.json", "node18_dup.json",
                  "node18_del.json", "node20_mod.json", "node22_dup.json", "node22_del.json", "node25_dup.json",
                  "node25_del.json", "node29_dup.json", "node29_del.json", "node31_mod.json", "node32_mod.json",
                  "node35_mod.json", "node38_mod.json", "node41_del.json", "node42_dup.json", "node42_del.json",
                  "node43_del.json", "node44_dup.json", "node44_del.json", "node45_dup.json", "node45_del.json",
                  "node46_mod.json", "node47_mod.json", "node48_mod.json", "node49_mod.json", "node50_mod.json"]


