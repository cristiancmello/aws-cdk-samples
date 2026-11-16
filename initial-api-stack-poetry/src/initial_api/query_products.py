from products_db import get_products_by_category, get_all_products
from response_utils import create_error_response, create_success_response


def handler(event, context):
    path_parameters = event.get("pathParameters") or {}

    try:
        query_parameters = event.get("queryStringParameters") or {}
        category = query_parameters.get("category")

        if category:
            products = get_products_by_category(category)
        else:
            products = get_all_products()
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return create_error_response(500, f"Internal Server Error: {str(e)}")
    return create_success_response(200, products)