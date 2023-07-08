from fastapi import APIRouter, Query

from models.order import Order 
from db import connection
from schemas.order import ordersEntity, orderEntity
from bson import ObjectId

order = APIRouter()

@order.get('/orders')
async def get_all_orders(limit: int = Query(5, gt=0), offset: int = Query(0, ge=0)):
    # limit - max number of docs to return (default is 5)
    # offset - number of docs to skip from beginning (default is 0)
    total = connection.ecom.orders.count_documents({})
    orders = list(connection.ecom.orders.find().skip(offset).limit(limit))

    return {
        'total': total,
        'orders': ordersEntity(orders)
    }

@order.get('/order/{id}')
async def get_order_by_id(id):
    return orderEntity(connection.ecom.orders.find_one({'_id': ObjectId(id)}))

@order.post('/create-order')
async def create_order(order: Order):
    order_dict = dict(order)
    order_dict['items'] = [dict(item) for item in order_dict['items']]
    order_dict['userAddress'] = dict(order_dict['userAddress'])
    connection.ecom.orders.insert_one(order_dict)
    return {'msg':'Order created successfully'}
