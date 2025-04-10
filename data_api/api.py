from typing import Union
import polars as pl
from fastapi import FastAPI
from os.path import join

app = FastAPI()

orders = pl.read_csv(join("data_api", "data", "orders.csv"))
order_items = pl.read_csv(join("data_api", "data", "order_items.csv"))
customers = pl.read_csv(join("data_api", "data", "customers.csv"))

print("CSV-sti læst OK")

@app.get("/orders")
def read_orders():
    return orders.to_dicts()

@app.get("/order_items")
def read_order_items():
    return order_items.to_dicts()

@app.get("/customers")
def read_customers():
    return customers.to_dicts()
