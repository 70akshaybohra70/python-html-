from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_regular_customer_high_order():
    response = client.post("/calculate-discount", json={
        "customer_type": "Regular",
        "order_amount": 600,
        "order_date": "2025-04-12"
    })
    assert response.status_code == 200
    assert response.json()["final_discount"] == 5.0

def test_gold_customer_december():
    response = client.post("/calculate-discount", json={
        "customer_type": "Gold",
        "order_amount": 100,
        "order_date": "2025-12-01"
    })
    assert response.status_code == 200
    assert response.json()["final_discount"] == 20.0

def test_invalid_customer_type():
    response = client.post("/calculate-discount", json={
        "customer_type": "Silver",
        "order_amount": 100,
        "order_date": "2025-04-12"
    })
    assert response.status_code == 422