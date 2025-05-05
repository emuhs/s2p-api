"""
db.py
This module configures the SQLAlchemy database engine and session for the app.
It also defines a reusable database session dependency for request handling.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./s2p.db"

# Create the database engine
# 'check_same_thread=False' is required for SQLite to allow multiple threads.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session factory bound to the engine
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for all ORM models to inherit from.
Base = declarative_base()

def get_db():
	"""
	Dependency that provides a SQLAlchemy db session - closes after use."""
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
