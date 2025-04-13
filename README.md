# Discount Calculation Service

A simple FastAPI backend that replicates discount logic previously implemented in a SQL stored procedure.

## Endpoints

### POST `/calculate-discount`

**Request JSON:**
```json
{
  "customer_type": "Gold",
  "order_amount": 100,
  "order_date": "2025-12-01"
}
```

**Response JSON:**
```json
{
  "final_discount": 20.0
}
```

## Running Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Running with Docker

```bash
docker build -t discount-service .
docker run -p 8000:8000 discount-service
```

## Running Tests

```bash
pytest test_main.py
```