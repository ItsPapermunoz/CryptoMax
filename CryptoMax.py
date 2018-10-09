# Imports

import pickle
import os
import appJar
import time

"""File Data"""

__file__ = "CryptoMax.py"
__author__ = "Geeky_Barista"
__license__ = "MIT"
__Version__ = "Alpha"
file_path = os.path.abspath("CryptoMax.py")
date = time.strftime("%c")

"""Variables"""

"""Function Definitions"""


def data():
    try:
        log = pickle.load(open("Log.txt", "r"))
    except FileNotFoundError:
        log = "This file was created on {}. ".format(date)
        dir_path = "Text"
        os.mkdir(dir_path)
    finally:
        return log


"""Main Code"""


data()