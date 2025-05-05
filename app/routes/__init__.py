"""
This file initializes the 'routes' package. It imports the supplier & purchase_order
modules so they can be accessed when importing from 'app.routes'. This makes the 
route registration in 'main.py' cleaner.
"""

from . import supplier, purchase_order
