"""
This file defines the SQLAlchemy model for the Supplier entity, which maps to the
'suppliers' table in the db. It includes fields for identifying and contact a 
supplier, as well as establishes a one-to-many relationship with purchase orders.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

# Supplier model represents a vendor or entity from which goods/services are purchased.
class Supplier(Base):
	__tablename__ = "suppliers" # Name of the table in db

	id = Column(Integer, primary_key=True, index=True) # Unique ID for each supplier
	name = Column(String, index=True) 		   # Name of supplier
	email = Column(String, unique=True, index=True)	   # Supplier email (must be unique)
	phone = Column(String)				   # Contact phone number

	# Establishes one-to-many relationship w/ PurchaseOrder
	orders = relationship("PurchaseOrder", back_populates="supplier")
