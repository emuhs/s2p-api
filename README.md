# Source-to-Pay (S2P) API

This is a lightweight Source-to-Pay (S2P) backend built with FastAPI. 
It supports CRUD operations for managing suppliers and their purchase orders. 
The project is containerized using Docker and includes test coverage with pytest.

## Features

- Supplier and purchase order CRUD functionality
- Input validation with Pydantic
- SQLAlchemy ORM with SQLite (precursor db ahead of dev into PostgreSQL)
- RESTful API with FastAPI
- Auto-generated Swagger and ReDoc documentation
- Dockerized for portability
- Unit tests with pytest

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (default)
- Docker
- Uvicorn
- pytest

## Project Structure

```
s2p_project
├── Dockerfile.dev
├── README.md
├── app
│   ├── db.py
│   ├── main.py
│   ├── models
│   ├── routes
│   └── schemas
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_purchase_order.py
    └── test_supplier.py
```

## Getting Started

### Local Development

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/s2p-api.git
    cd s2p-api
    ```

2. Set up and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the development server:

    ```bash
    uvicorn app.main:app --reload
    ```

5. Access the API documentation at:

    - Swagger UI: http://localhost:8000/docs
    - ReDoc: http://localhost:8000/redoc

### Running with Docker

1. Build the image:

    ```bash
    docker build -f Dockerfile.dev -t s2p-api .
    ```

2. Run the container:

    ```bash
    docker run -p 8000:8000 s2p-api
    ```

## Running Tests

To run the test suite using pytest:

```bash
pytest
```

## Future Improvements

- Add authentication and authorization (OAuth2 or JWT)
- Integrate PostgreSQL in a production Docker environment
- Extend schema to support invoices and approvals
- Add pagination and filtering to list endpoints
- CI/CD pipeline and deployment via Railway, Render, or Fly.io
