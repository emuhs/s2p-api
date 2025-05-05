from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_supplier():
	response = client.post("/supplier", json={
		"name": "Test Supplier",
		"email": "test@example.com",
		"phone": "+123456789"
	})
	assert response.status_code == 200
	data = response.json()
	assert data["name"] == "Test Supplier"
	assert "id" in data

def test_get_supplier():
	response = client.get("/supplier/1")
	assert response.status_code == 200
	data = response.json()
	assert data["id"] == 1
