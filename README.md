# Source-to-Pay (S2P) API

Source-to-Pay (S2P) API is a secure, containerized backend for managing supplier relationships and purchase workflows. 
Built with FastAPI and PostgreSQL, it supports full CRUD operations, schema migrations, and test coverage — making it ideal for internal finance or procurement teams needing a lightweight yet scalable foundation.

## Features

- Supplier and purchase order CRUD functionality
- Input validation with Pydantic
- SQLAlchemy ORM with PostgreSQL (via Docker)
- RESTful API with FastAPI
- Alembic for schema migrations
- Dockerized for portability and local development
- Unit tests with pytest

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL (via Docker)
- Alembic (for migrations)
- Docker & Docker Compose
- pytest

## Project Structure

```
.
├── Dockerfile
├── LICENSE
├── README.md
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── dd21dda05376_initial_schema.py
├── alembic.ini
├── app
│   ├── config.py
│   ├── db
│   │   ├── __init__.py
│   │   └── session.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── purchase_order.py
│   │   └── supplier.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── purchase_order.py
│   │   └── supplier.py
│   └── schemas
│       ├── purchase_order.py
│       └── supplier.py
├── docker-compose.yml
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_purchase_order.py
    └── test_supplier.py
```

## Endpoints

### Supplier Routes
- `GET /supplier`: List all suppliers  
- `POST /supplier`: Create a new supplier  
- `GET /supplier/{supplier_id}`: Retrieve a supplier by ID  
- `PUT /supplier/{supplier_id}`: Update a supplier  
- `DELETE /supplier/{supplier_id}`: Delete a supplier  
- `GET /supplier/{supplier_id}/purchase_orders`: Get Purchase Orders For Supplier

### Purchase Order Routes
- `GET /purchase_order`: List all purchase orders  
- `POST /purchase_order`: Create a new purchase order  
- `GET /purchase_order/{id}`: Retrieve a purchase order by ID  
- `PUT /purchase_order/{id}`: Update a purchase order  
- `DELETE /purchase_order/{id}`: Delete a purchase order  


## Getting Started

### Running the Project with Docker

1. Start the application stack (API and PostgreSQL) using Docker Compose:

```bash
docker-compose up --build
```

2. The API will be available at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

3. To shut down the stack:

```bash
docker-compose down
```

### Database Migrations with Alembic

Alembic is used to handle database schema migrations with PostgreSQL.

1. Create a new migration after editing your SQLAlchemy models:

```bash
docker-compose exec web alembic revision --autogenerate -m "Your message here"
```

2. Apply the migration to the database:

```bash
docker-compose exec web alembic upgrade head
```

## Running Tests

To run the test suite using Docker (recommended):

```bash
docker-compose exec web pytest
```

## Future Improvements

- Add authentication and authorization (OAuth2 or JWT)
- Harden PostgreSQL setup for production (secure env vars, persistent volumes)
- Extend schema to support invoices and approvals
- Implement pagination and filtering for list endpoints
- Improve error handling and standardized API responses
- Set up CI/CD pipeline for automated testing and deployment
- Add unit and integration tests with coverage reporting

