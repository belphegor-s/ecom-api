from fastapi import APIRouter

from db import connection
from schemas.product import productsEntity, productEntity
from bson import ObjectId

product = APIRouter()

@product.get('/products')
async def get_all_products():
    return productsEntity(connection.ecom.products.find())

@product.put('/update-product/{id}')
async def update_product_qty(id, product_qty: int):
    productEntity(connection.ecom.products.find_one_and_update({'_id': ObjectId(id)}, {
        '$set': { 'quantity': product_qty }
    }))
    return productEntity(connection.ecom.products.find_one({'_id': ObjectId(id)}))
