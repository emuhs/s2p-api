"""
app/models/__init__.py
Import key SQLAlchemy models into the package namespace.
This allows cleaner imports elsewhere in the app:
i.e. from app.models import Supplier, PurchaseOrder
"""
from .supplier import Supplier
from .purchase_order import PurchaseOrder
