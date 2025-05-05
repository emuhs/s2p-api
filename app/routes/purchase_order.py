"""
purchase_order.py - FastAPI router for handing purchase order endpoints.

This module defines routes for creating, retreiving, updating, and deleting 
purchase orders within the application. It uses SQLAlchemy for database 
interactions and Pydantic for request/response validation.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.schemas.purchase_order import PurchaseOrderCreate, PurchaseOrderOut
from app.models.purchase_order import PurchaseOrder

# Initialize router for purchase order endpoints
router = APIRouter()

@router.post("/", response_model=PurchaseOrderOut)
def create_purchase_order(order: PurchaseOrderCreate, db: Session = Depends(get_db)):
	"""
	Create a new PO.
	Args:
		order (PurchaseOrderCreate): PO input data.
		db (Session): SQLAlchemy database session.
	Returns:
		PurchaseOrderOut: The newly created PO.
	"""
	db_order = PurchaseOrder(**order.model_dump())
	db.add(db_order)
	db.commit()
	db.refresh(db_order)
	return db_order

@router.get("/all", response_model=List[PurchaseOrderOut])
def get_purchase_orders(db: Session = Depends(get_db)):
	"""
	Retrieve all POs from the db.
	Args:
		db (Session): SQLAlchemy db session.
	Returns:
		List[PurchaseOrderOut]: List of all POs.
	"""
	return db.query(PurchaseOrder).all()

@router.get("/{order_id}", response_model=PurchaseOrderOut)
def get_purchase_order(order_id: int, db: Session = Depends(get_db)):
	"""
	Retrieve a single PO by ID.
	Args:
		order_id (int): ID of the PO.
		db (Session): SQLAlchemy db session.
	Returns:
		PurchaseOrderOut: The matching PO (if found).
	Raises:
		HTTPException: If the order is not found.
	"""
	order = db.query(PurchaseOrder).filter(PurchaseOrder.id == order_id).first()
	if not order:
		raise HTTPException(status_code=404, detail="Purchase order not found.")
	return order

@router.put("/{order_id}", response_model=PurchaseOrderOut)
def update_purchase_order(order_id: int, order_update: PurchaseOrderCreate, db: Session = Depends(get_db)):
	"""
	Update an existing PO.
	Args:
		order_id (int): ID of the PO to update.	
		order_update (PurchaseOrderCreate): Updated PO data.
		db (Session): SQLAlchemy db session.
	Returns:
		PurchaseOrderOut: The updated PO.
	Raises:
		HTTPException: If the order is not found.
	"""
	order = db.query(PurchaseOrder).filter(PurchaseOrder.id == order_id).first()
	if not order:
		raise HTTPException(status_code=404, detail="Purchase order not found.")
	order.supplier_id = order_update.supplier_id
	order.item = order_update.item
	order.quantity = order_update.quantity
	db.commit()
	db.refresh(order)
	return order

@router.delete("/{order_id}", status_code=204)
def delete_purchase_order(order_id: int, db: Session = Depends(get_db)):
	"""
	Delete a PO by its ID.
	Args:
		order_id (int): ID of the PO to delete.
		db (Session): SQLAlchemy db session.
	Returns:
		None
	Raises:
		HTTPException: If the order is not found.
	"""
	order = db.query(PurchaseOrder).filter(PurchaseOrder.id == order_id).first()
	if not order:
		raise HTTPException(status_code=404, detail="Purchase order not found.")
	db.delete(order)
	db.commit()
	return
