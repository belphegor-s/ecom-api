def orderItemEntity(item) -> dict:
    return {
        'productId': item['productId'],
        'boughtQuantity': item['boughtQuantity']
    }

def orderItemsEntity(entity) -> list:
    return [orderItemEntity(item) for item in entity]

def orderEntity(order) -> dict:
    return {
        'timestamp': order['timestamp'],
        'items': orderItemsEntity(order['items']),
        'totalAmount': order['totalAmount'],
        'userAddress': {
            'city': order['userAddress']['city'],
            'country': order['userAddress']['country'],
            'zip_code': order['userAddress']['zip_code']
        }
    }

def ordersEntity(entity) -> list:
    return [orderEntity(order) for order in entity]
