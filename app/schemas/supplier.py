"""
This module defines Pydantic models for creating and returning 'Supplier' records
via FastAPI.

Schemas for Supplier API endpoints:
Defines input ('SupplierCreate') and output ('SupplierOut') models used by
FastAPI routes. Includes phone number validation.
"""
from pydantic import BaseModel, EmailStr, constr, field_validator

class SupplierCreate(BaseModel):
	"""
	Schema for supplier creation.
	Enforces:
	- Non-empty name
	- Valid email address
	- Phone number with basic pattern and min digit count
	"""
	name: constr(strip_whitespace=True, min_length=1)
	email: EmailStr
	phone: constr(strip_whitespace=True, min_length=7, max_length=15, pattern=r'^\+?[0-9\-]+$')
	
	@field_validator("phone")
	@classmethod
	def validate_phone(cls,v):
		"""
		Validates that the phone number has at least 7 digits.
		Allows for '+' and '-' formatting and ensures sufficient digits.
		"""
		digits = [c for c in v if c.isdigit()]
		if len(digits) < 7:
			raise ValueError("Phone number must have at least 7 digits.")
		return v


class SupplierOut(BaseModel):
	"""
	Schema for returning supplier data in responses.
	"""
	id: int
	name: str
	email: EmailStr
	phone: str

	class Config:
		# Allows FastAPI to populate this model from ORM instances.
		from_attributes = True
