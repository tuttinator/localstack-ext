from localstack.runtime import hooks
from localstack_ext.bootstrap.licensing import api_key_configured
@hooks.on_infra_start(should_load=api_key_configured)
def add_aws_request_logger():from localstack.aws import handlers as A;from .aws_request_logger import RequestLoggerHandler as B;A.count_service_request=B()