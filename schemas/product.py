def productEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'price': item['price'],
        'quantity': item['quantity']
    }

def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]