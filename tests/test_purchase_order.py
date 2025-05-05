from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_purchase_order():
	supplier_response = client.post("/supplier", json={
		"name": "PO Test Supplier",
		"email": "po@example.com",
		"phone": "+1234567891"
	})
	assert supplier_response.status_code in (200, 201)
	supplier_id = supplier_response.json()["id"]

	po_response = client.post("/purchase_order", json={
		"supplier_id": supplier_id,
		"item": "Test item",
		"quantity": 125678
	})
	assert po_response.status_code in (200, 201)
	data = po_response.json()
	assert data["item"] == "Test item"
	assert data["quantity"] == 125678
	assert data["supplier_id"] == supplier_id

def test_get_purchase_order():
	response = client.get("/purchase_order/1")
	assert response.status_code == 200
	data = response.json()
	assert "item" in data
	assert "quantity" in data
