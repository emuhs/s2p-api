"""
app/routes/supplier.py
This module defines the API endpoints for managing Supplier resources.
Includes endpoints for creating, retreiving, updating, and deleting suppliers,
as well as retreiving POs associated with a specific supplier.
"""

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.supplier import SupplierCreate, SupplierOut
from app.schemas.purchase_order import PurchaseOrderOut
from app.models.supplier import Supplier
from app.models.purchase_order import PurchaseOrder
from app.db import SessionLocal, get_db
from typing import List

# Initialize the router for the Supplier endpoint.
router = APIRouter()

@router.post("/", response_model=SupplierOut)
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
	"""
	Creates a new supplier record in the database.
	Args:
		supplier (SupplierCreate): Supplier input data.
		db (Session): SQLAlchemy db session.
	Returns:
		SupplierOut: Newly created supplier.
	Raises:
		HTTPException: If a supplier with the same email already exists
	"""
	# Check if supplier w/ same email exists
	existing = db.query(Supplier).filter(Supplier.email == supplier.email).first()
	if existing:
		raise HTTPException(status_code=400, detail="Supplier with this email already exists.")
	new_supplier = Supplier(
		name=supplier.name,
		email=supplier.email,
		phone=supplier.phone
	)
	db.add(new_supplier)
	db.commit()
	db.refresh(new_supplier)
	return new_supplier

@router.get("/all", response_model=List[SupplierOut])
def get_suppliers(db: Session = Depends(get_db)):
	"""
	Retreive all suppliers from the db.
	Args:
		db (Session): SQLAlchemy db session.
	Returns:
		List[SupplierOut]: List of all suppliers.
	"""
	return db.query(Supplier).all()

@router.get("/{supplier_id}",response_model=SupplierOut)
def get_supplier_by_id(supplier_id: int, db: Session = Depends(get_db)):
	"""
	Retrieve a single supplier by ID.
	Args:
		supplier_id (int): ID of the supplier.
		db (Session): SQLAlchemy db session.
	Returns SupplierOut: The matching supplier (if found).
	Raises:
		HTTPException: If the supplier is not found
	"""
	supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
	if not supplier:
		raise HTTPException(status_code=404, detail = "Supplier not found.")
	return supplier

@router.put("/{supplier_id}", response_model=SupplierOut)
def update_supplier(supplier_id: int, supplier_update: SupplierCreate, 	db: Session = Depends(get_db)
):
	"""
	Update an existing supplier.
	Args:
		supplier_id (int): ID of the supplier to update.
		supplier_update (SupplierCreate): Updated supplier data.
		db (Session): SQLAlchemy db session.
	Returns:
		SupplierOut: The updated supplier.
	Raises:
		HTTPException: If the supplier is not found or if supplier email
		already exists.
	"""
	supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
	if not supplier:
		raise HTTPException(status_code=404, detail="Supplier not found.")

	supplier.name = supplier_update.name
	supplier.email = supplier_update.email
	supplier.phone = supplier_update.phone
	
	try:
		db.commit()
	except IntegrityError:
		db.rollback()
		raise HTTPException(status_code=400, detail="Email already exists.")

	db.refresh(supplier)
	return supplier

@router.delete("/{supplier_id}", status_code = 204)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
	"""
	Delete a supplier by ID.
	Args:
		supplier_id (int): ID of the supplier.
		db (Session): SQLAlchemy db session.
	Returns:
		None
	Raises:
		HTTPException: If the supplier is not found.
	"""
	supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
	if not supplier:
		raise HTTPException(status_code=404, detail="Supplier not found.")

	db.delete(supplier)
	db.commit()
	return

@router.get("/{supplier_id}/purchase_orders", response_model=List[PurchaseOrderOut])
def get_purchase_orders_for_supplier(supplier_id: int, db: Session = Depends(get_db)):
	"""
	Retrieve all POs from a supplier by supplier ID.
	Args:
		supplier_id (int): ID of the supplier.
		db (Session): SQLAlchemy db session.
	Returns:
		List[PurchaseOrderOut]: A list of current POs for the given supplier ID.
	"""
	return db.query(PurchaseOrder).filter(PurchaseOrder.supplier_id == supplier_id).all()
