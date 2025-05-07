"""
main.py
Entry point for the Source-to-Pay (S2P) FastAPI application.
This file initializes the FastAPI app, sets up middleware, registers route 
modules, and ensures database tables are created at startup.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import Base, engine 
from app import models		
from app.routes import supplier, purchase_order  #API route modules

# Initialize FastAPI application w/ metadata
app = FastAPI(
	title="Source-to-Pay API",
	description="Manage suppliers and their purchase orders.",
	version="1.0.0"
)

# Enable Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins (possibly restrict in prod)
    allow_credentials=True,
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"]  # Allow all headers
)

# Register routers with specific path prefixes and Swagger tags
app.include_router(supplier.router, prefix="/supplier", tags=["Suppliers"])
app.include_router(purchase_order.router, prefix="/purchase_order", tags=["Purchase Orders"])

# Root route for basic health check or welcome message
@app.get("/")
def root():
    return {"message": "S2P System is Live"}

# Automatically create tables based on SQLAlchemy models
Base.metadata.create_all(bind=engine)
