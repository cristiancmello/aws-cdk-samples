import os

from aws_cdk import (
    CfnOutput,
    Stack,
    aws_lambda,
    aws_apigateway
)
from constructs import Construct

class InitialStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        code_location=os.path.join(os.path.dirname(__file__), "../src/initial_api")
        lambda_runtime=aws_lambda.Runtime.PYTHON_3_12
        default_concurrent_executions = 5

        self.get_product= aws_lambda.Function(self, "GetProduct",
            runtime=lambda_runtime,
            handler="get_product.handler",
            code=aws_lambda.Code.from_asset(code_location),
            reserved_concurrent_executions = default_concurrent_executions
        )

        self.query_products= aws_lambda.Function(self, "QueryProducts",
            runtime=lambda_runtime,
            handler="query_products.handler",
            code=aws_lambda.Code.from_asset(code_location),
            reserved_concurrent_executions = default_concurrent_executions
        )

        self.insert_product= aws_lambda.Function(self, "InsertProduct",
            runtime=lambda_runtime,
            handler="insert_product.handler",
            code=aws_lambda.Code.from_asset(code_location),
            reserved_concurrent_executions = default_concurrent_executions
        )

        self.delete_product= aws_lambda.Function(self, "DeleteProduct",
            runtime=lambda_runtime,
            handler="delete_product.handler",
            code=aws_lambda.Code.from_asset(code_location),
            reserved_concurrent_executions = default_concurrent_executions
        )

        self.update_product= aws_lambda.Function(self, "UpdateProduct",
            runtime=lambda_runtime,
            handler="update_product.handler",
            code=aws_lambda.Code.from_asset(code_location),
            reserved_concurrent_executions = default_concurrent_executions
        )

        api = aws_apigateway.RestApi(
            self, "ProductsAPI",
            rest_api_name="ProductsApi",
            description="Amazon API Gateway for ProductsAPI.",
            deploy_options=aws_apigateway.StageOptions(
                stage_name="dev",
                logging_level=aws_apigateway.MethodLoggingLevel.INFO,
            )
        )
        
        products_resource = api.root.add_resource("products")
        products_resource.add_method("GET", aws_apigateway.LambdaIntegration(self.query_products))
        products_resource.add_method("POST", aws_apigateway.LambdaIntegration(self.insert_product))

        product_resource_id = products_resource.add_resource("{id}")
        product_resource_id.add_method("GET", aws_apigateway.LambdaIntegration(self.get_product))
        product_resource_id.add_method("DELETE", aws_apigateway.LambdaIntegration(self.delete_product))
        product_resource_id.add_method("PUT", aws_apigateway.LambdaIntegration(self.update_product))

        self.api=api
        CfnOutput(self, "ProductsApiUrl", value=f'{api.url}products')