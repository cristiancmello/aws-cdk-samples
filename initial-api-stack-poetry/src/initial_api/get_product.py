
from __future__ import annotations
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent
    from aws_lambda_powertools.utilities.typing import LambdaContext

import products_db

from response_utils import create_error_response, create_success_response

def handler(event: APIGatewayProxyEvent, context: LambdaContext):
    try:
        path_parameters = event.get("pathParameters") or {}
        product_id = path_parameters.get("id")

        if not product_id:
            return create_error_response(400, "Product id is required")
        
        product = products_db.get_product(product_id)
        if not product:
            return create_error_response(404, f"Product with id {product_id} not found")
        
        return create_success_response(200, product)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return create_error_response(500, f"Internal Server Error: {str(e)}")