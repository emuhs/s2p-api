"""
Defines the PurchaseOrder SQLAlchemy model, representing purchase orders tied to
suppliers in the database.  Implements the 'many-to-one' relationship with the 
Supplier model.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

# Represents a purchase order placed with a supplier
class PurchaseOrder(Base):
	__tablename__ = "purchase_orders" # Table name in the database

	id = Column(Integer, primary_key=True, index=True) # Unique ID for each PO
	supplier_id = Column(Integer, ForeignKey("suppliers.id")) # Foreign Key to Supplier table
	item = Column(String) # Item description
	quantity = Column(Integer) # Item quantity

	# Defines the relationship to the Supplier model (back-populates 'orders' from suppliers)
	supplier = relationship("Supplier", back_populates="orders")
