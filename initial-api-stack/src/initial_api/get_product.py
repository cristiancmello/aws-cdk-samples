from json import dumps

products = {
    "prod_123": {"id": "prod_123", "name": "Wireless Headphones", "price": 199.99},
    "prod_456": {"id": "prod_456", "name": "USB-C Cable", "price": 12.99}
}

def handler(event, context):
    path_parameters = event.get("pathParameters", {}) or {}
    product_id = event.get("pathParameters", {}).get("id")
    
    if not product_id:
        return {"statusCode": 400, "body": dumps({"error": "Product ID is required"})}
    
    print(event)
    print(path_parameters)
    
    product = products.get(product_id)
    if not product:
        return {"statusCode": 404, "body": dumps({"error": "Product not found"})}

    return {
        "statusCode": 200,
        "body": dumps(product)
    }