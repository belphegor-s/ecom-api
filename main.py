from fastapi import FastAPI
from routes.product import product
from routes.order import order

app = FastAPI()
app.include_router(product)
app.include_router(order)

@app.get('/')
def index():
    return {'msg':'Server is live 🍵'}