from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
from datetime import date

app = FastAPI()

class DiscountRequest(BaseModel):
    customer_type: str
    order_amount: float
    order_date: date

    @validator("customer_type")
    def validate_customer_type(cls, value):
        allowed = {"Regular", "Premium", "Gold"}
        if value not in allowed:
            raise ValueError(f"Invalid customer type. Allowed: {allowed}")
        return value

@app.post("/calculate-discount")
def calculate_discount(data: DiscountRequest):
    discount = 0.0

    if data.customer_type == 'Regular' and data.order_amount > 500:
        discount = 5.0
    elif data.customer_type == 'Premium' and data.order_amount > 300:
        discount = 10.0
    elif data.customer_type == 'Gold':
        discount = 15.0

    if data.order_date.month == 12:
        discount += 5.0

    return {"final_discount": discount}