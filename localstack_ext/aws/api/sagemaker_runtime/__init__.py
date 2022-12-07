import sys
from typing import IO, Iterable, Optional, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

CustomAttributesHeader = str
EnableExplanationsHeader = str
EndpointName = str
Header = str
InferenceId = str
InputLocationHeader = str
LogStreamArn = str
Message = str
RequestTTLSecondsHeader = int
StatusCode = int
TargetContainerHostnameHeader = str
TargetModelHeader = str
TargetVariantHeader = str


class InternalDependencyException(ServiceException):
    """Your request caused an exception with an internal dependency. Contact
    customer support.
    """

    code: str = "InternalDependencyException"
    sender_fault: bool = False
    status_code: int = 530


class InternalFailure(ServiceException):
    """An internal failure occurred."""

    code: str = "InternalFailure"
    sender_fault: bool = False
    status_code: int = 500


class ModelError(ServiceException):
    """Model (owned by the customer in the container) returned 4xx or 5xx error
    code.
    """

    code: str = "ModelError"
    sender_fault: bool = False
    status_code: int = 424
    OriginalStatusCode: Optional[StatusCode]
    OriginalMessage: Optional[Message]
    LogStreamArn: Optional[LogStreamArn]


class ModelNotReadyException(ServiceException):
    """Either a serverless endpoint variant's resources are still being
    provisioned, or a multi-model endpoint is still downloading or loading
    the target model. Wait and try your request again.
    """

    code: str = "ModelNotReadyException"
    sender_fault: bool = False
    status_code: int = 429


class ServiceUnavailable(ServiceException):
    """The service is unavailable. Try your call again."""

    code: str = "ServiceUnavailable"
    sender_fault: bool = False
    status_code: int = 503


class ValidationError(ServiceException):
    """Inspect your request and try again."""

    code: str = "ValidationError"
    sender_fault: bool = False
    status_code: int = 400


BodyBlob = bytes


class InvokeEndpointAsyncInput(ServiceRequest):
    EndpointName: EndpointName
    ContentType: Optional[Header]
    Accept: Optional[Header]
    CustomAttributes: Optional[CustomAttributesHeader]
    InferenceId: Optional[InferenceId]
    InputLocation: InputLocationHeader
    RequestTTLSeconds: Optional[RequestTTLSecondsHeader]


class InvokeEndpointAsyncOutput(TypedDict, total=False):
    InferenceId: Optional[Header]
    OutputLocation: Optional[Header]


class InvokeEndpointInput(ServiceRequest):
    Body: IO[BodyBlob]
    EndpointName: EndpointName
    ContentType: Optional[Header]
    Accept: Optional[Header]
    CustomAttributes: Optional[CustomAttributesHeader]
    TargetModel: Optional[TargetModelHeader]
    TargetVariant: Optional[TargetVariantHeader]
    TargetContainerHostname: Optional[TargetContainerHostnameHeader]
    InferenceId: Optional[InferenceId]
    EnableExplanations: Optional[EnableExplanationsHeader]


class InvokeEndpointOutput(TypedDict, total=False):
    Body: Union[BodyBlob, IO[BodyBlob], Iterable[BodyBlob]]
    ContentType: Optional[Header]
    InvokedProductionVariant: Optional[Header]
    CustomAttributes: Optional[CustomAttributesHeader]


class SagemakerRuntimeApi:

    service = "sagemaker-runtime"
    version = "2017-05-13"

    @handler("InvokeEndpoint")
    def invoke_endpoint(
        self,
        context: RequestContext,
        endpoint_name: EndpointName,
        body: IO[BodyBlob],
        content_type: Header = None,
        accept: Header = None,
        custom_attributes: CustomAttributesHeader = None,
        target_model: TargetModelHeader = None,
        target_variant: TargetVariantHeader = None,
        target_container_hostname: TargetContainerHostnameHeader = None,
        inference_id: InferenceId = None,
        enable_explanations: EnableExplanationsHeader = None,
    ) -> InvokeEndpointOutput:
        """After you deploy a model into production using Amazon SageMaker hosting
        services, your client applications use this API to get inferences from
        the model hosted at the specified endpoint.

        For an overview of Amazon SageMaker, see `How It
        Works <https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__.

        Amazon SageMaker strips all POST headers except those supported by the
        API. Amazon SageMaker might add additional headers. You should not rely
        on the behavior of headers outside those enumerated in the request
        syntax.

        Calls to ``InvokeEndpoint`` are authenticated by using Amazon Web
        Services Signature Version 4. For information, see `Authenticating
        Requests (Amazon Web Services Signature Version
        4) <https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html>`__
        in the *Amazon S3 API Reference*.

        A customer's model containers must respond to requests within 60
        seconds. The model itself can have a maximum processing time of 60
        seconds before responding to invocations. If your model is going to take
        50-60 seconds of processing time, the SDK socket timeout should be set
        to be 70 seconds.

        Endpoints are scoped to an individual account, and are not public. The
        URL does not contain the account ID, but Amazon SageMaker determines the
        account ID from the authentication token that is supplied by the caller.

        :param endpoint_name: The name of the endpoint that you specified when you created the
        endpoint using the
        `CreateEndpoint <https://docs.
        :param body: Provides input data, in the format specified in the ``ContentType``
        request header.
        :param content_type: The MIME type of the input data in the request body.
        :param accept: The desired MIME type of the inference in the response.
        :param custom_attributes: Provides additional information about a request for an inference
        submitted to a model hosted at an Amazon SageMaker endpoint.
        :param target_model: The model to request for inference when invoking a multi-model endpoint.
        :param target_variant: Specify the production variant to send the inference request to when
        invoking an endpoint that is running two or more variants.
        :param target_container_hostname: If the endpoint hosts multiple containers and is configured to use
        direct invocation, this parameter specifies the host name of the
        container to invoke.
        :param inference_id: If you provide a value, it is added to the captured data when you enable
        data capture on the endpoint.
        :param enable_explanations: An optional JMESPath expression used to override the
        ``EnableExplanations`` parameter of the ``ClarifyExplainerConfig`` API.
        :returns: InvokeEndpointOutput
        :raises InternalFailure:
        :raises ServiceUnavailable:
        :raises ValidationError:
        :raises ModelError:
        :raises InternalDependencyException:
        :raises ModelNotReadyException:
        """
        raise NotImplementedError

    @handler("InvokeEndpointAsync")
    def invoke_endpoint_async(
        self,
        context: RequestContext,
        endpoint_name: EndpointName,
        input_location: InputLocationHeader,
        content_type: Header = None,
        accept: Header = None,
        custom_attributes: CustomAttributesHeader = None,
        inference_id: InferenceId = None,
        request_ttl_seconds: RequestTTLSecondsHeader = None,
    ) -> InvokeEndpointAsyncOutput:
        """After you deploy a model into production using Amazon SageMaker hosting
        services, your client applications use this API to get inferences from
        the model hosted at the specified endpoint in an asynchronous manner.

        Inference requests sent to this API are enqueued for asynchronous
        processing. The processing of the inference request may or may not
        complete before the you receive a response from this API. The response
        from this API will not contain the result of the inference request but
        contain information about where you can locate it.

        Amazon SageMaker strips all ``POST`` headers except those supported by
        the API. Amazon SageMaker might add additional headers. You should not
        rely on the behavior of headers outside those enumerated in the request
        syntax.

        Calls to ``InvokeEndpointAsync`` are authenticated by using Amazon Web
        Services Signature Version 4. For information, see `Authenticating
        Requests (Amazon Web Services Signature Version
        4) <https://docs.aws.amazon.com/https:/docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html>`__
        in the *Amazon S3 API Reference*.

        :param endpoint_name: The name of the endpoint that you specified when you created the
        endpoint using the
        ```CreateEndpoint`` <https://docs.
        :param input_location: The Amazon S3 URI where the inference request payload is stored.
        :param content_type: The MIME type of the input data in the request body.
        :param accept: The desired MIME type of the inference in the response.
        :param custom_attributes: Provides additional information about a request for an inference
        submitted to a model hosted at an Amazon SageMaker endpoint.
        :param inference_id: The identifier for the inference request.
        :param request_ttl_seconds: Maximum age in seconds a request can be in the queue before it is marked
        as expired.
        :returns: InvokeEndpointAsyncOutput
        :raises InternalFailure:
        :raises ServiceUnavailable:
        :raises ValidationError:
        """
        raise NotImplementedError
