import json
from decimal import Decimal

access_control_headers= {
    'Access-Control-Allow-Origin': '*', 
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS', 
    'Access-Control-Allow-Headers': 'Content-Type, Authorization'
}
headers={**access_control_headers, 'Content-Type': 'application/json'}
options_headers={**access_control_headers, 'Access-Control-Max-Age': '86400'}

def create_error_response(status_code, message):
    """Create standardized error response for API Gateway"""
    return {
        'statusCode': status_code,
        'body': message,
        'headers': headers
    }

def create_success_response(status_code, data):
    """Create standardized success response for API Gateway"""
    return {
        'statusCode': status_code,
        'headers': headers,
        'body': json.dumps(data, default=decimal_serializer)
    }

def decimal_serializer(obj):
    """Handle Decimal objects in JSON serialization"""
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")