"""
Defines the data validation & serialization schemas for 'PurchaseOrder' ops using
Pydantic. These schemas are used for request validation ('PurchaseOrderCreate') &
response formatting ('PurchaseOrderOut').
"""

from pydantic import BaseModel
from typing import Optional

class PurchaseOrderCreate(BaseModel):
	"""
	Schema for creating new PO.
	Attributes:
		supplier_id (int): Foreign key referencing the supplier.
		item (str): Name or description of item ordered.
		quantity (int): Number of items being ordered.
	"""
	supplier_id: int
	item: str
	quantity: int

class PurchaseOrderOut(BaseModel):
	"""
	Schema for returning PO data in API response.
	Attributes:
		id (int): Unique ID of the PO.
		supplier_id (int): ID of the supplier associated with the order.
		item (str): Name or description of the item.
		quantity (int): Number of items being ordered.
	"""
	id: int
	supplier_id: int
	item: str
	quantity: int

	class Config:
	# Ensures Pydantic can read data from ORM objects
		from_attributes = True
