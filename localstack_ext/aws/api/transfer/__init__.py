import sys
from datetime import datetime
from typing import List, Optional

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AddressAllocationId = str
AgreementId = str
Arn = str
As2Id = str
CallbackToken = str
CertSerial = str
Certificate = str
CertificateBodyType = str
CertificateChainType = str
CertificateId = str
ConnectorId = str
CustomStepTarget = str
CustomStepTimeoutSeconds = int
Description = str
DirectoryId = str
EfsFileSystemId = str
EfsPath = str
ExecutionErrorMessage = str
ExecutionId = str
ExternalId = str
FilePath = str
Fips = bool
Function = str
HomeDirectory = str
HostKey = str
HostKeyDescription = str
HostKeyFingerprint = str
HostKeyId = str
HostKeyType = str
LogGroupName = str
MapEntry = str
MapTarget = str
MaxResults = int
Message = str
MessageSubject = str
NextToken = str
NullableRole = str
PassiveIp = str
Policy = str
PostAuthenticationLoginBanner = str
PreAuthenticationLoginBanner = str
PrivateKeyType = str
ProfileId = str
Resource = str
ResourceType = str
Response = str
RetryAfterSeconds = str
Role = str
S3Bucket = str
S3Etag = str
S3Key = str
S3TagKey = str
S3TagValue = str
S3VersionId = str
SecurityGroupId = str
SecurityPolicyName = str
SecurityPolicyOption = str
ServerId = str
ServiceErrorMessage = str
SessionId = str
SourceFileLocation = str
SourceIp = str
SshPublicKeyBody = str
SshPublicKeyCount = int
SshPublicKeyId = str
StatusCode = int
StepResultOutputsJson = str
SubnetId = str
TagKey = str
TagValue = str
TransferId = str
Url = str
UserCount = int
UserName = str
UserPassword = str
VpcEndpointId = str
VpcId = str
WorkflowDescription = str
WorkflowId = str
WorkflowStepName = str


class AgreementStatusType(str):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class As2Transport(str):
    HTTP = "HTTP"


class CertificateStatusType(str):
    ACTIVE = "ACTIVE"
    PENDING_ROTATION = "PENDING_ROTATION"
    INACTIVE = "INACTIVE"


class CertificateType(str):
    CERTIFICATE = "CERTIFICATE"
    CERTIFICATE_WITH_PRIVATE_KEY = "CERTIFICATE_WITH_PRIVATE_KEY"


class CertificateUsageType(str):
    SIGNING = "SIGNING"
    ENCRYPTION = "ENCRYPTION"


class CompressionEnum(str):
    ZLIB = "ZLIB"
    DISABLED = "DISABLED"


class CustomStepStatus(str):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class Domain(str):
    S3 = "S3"
    EFS = "EFS"


class EncryptionAlg(str):
    AES128_CBC = "AES128_CBC"
    AES192_CBC = "AES192_CBC"
    AES256_CBC = "AES256_CBC"
    NONE = "NONE"


class EndpointType(str):
    PUBLIC = "PUBLIC"
    VPC = "VPC"
    VPC_ENDPOINT = "VPC_ENDPOINT"


class ExecutionErrorType(str):
    PERMISSION_DENIED = "PERMISSION_DENIED"
    CUSTOM_STEP_FAILED = "CUSTOM_STEP_FAILED"
    THROTTLED = "THROTTLED"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    NOT_FOUND = "NOT_FOUND"
    BAD_REQUEST = "BAD_REQUEST"
    TIMEOUT = "TIMEOUT"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"


class ExecutionStatus(str):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    EXCEPTION = "EXCEPTION"
    HANDLING_EXCEPTION = "HANDLING_EXCEPTION"


class HomeDirectoryType(str):
    PATH = "PATH"
    LOGICAL = "LOGICAL"


class IdentityProviderType(str):
    SERVICE_MANAGED = "SERVICE_MANAGED"
    API_GATEWAY = "API_GATEWAY"
    AWS_DIRECTORY_SERVICE = "AWS_DIRECTORY_SERVICE"
    AWS_LAMBDA = "AWS_LAMBDA"


class MdnResponse(str):
    SYNC = "SYNC"
    NONE = "NONE"


class MdnSigningAlg(str):
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"
    SHA1 = "SHA1"
    NONE = "NONE"
    DEFAULT = "DEFAULT"


class OverwriteExisting(str):
    TRUE = "TRUE"
    FALSE = "FALSE"


class ProfileType(str):
    LOCAL = "LOCAL"
    PARTNER = "PARTNER"


class Protocol(str):
    SFTP = "SFTP"
    FTP = "FTP"
    FTPS = "FTPS"
    AS2 = "AS2"


class SetStatOption(str):
    DEFAULT = "DEFAULT"
    ENABLE_NO_OP = "ENABLE_NO_OP"


class SigningAlg(str):
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"
    SHA1 = "SHA1"
    NONE = "NONE"


class State(str):
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    START_FAILED = "START_FAILED"
    STOP_FAILED = "STOP_FAILED"


class TlsSessionResumptionMode(str):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    ENFORCED = "ENFORCED"


class WorkflowStepType(str):
    COPY = "COPY"
    CUSTOM = "CUSTOM"
    TAG = "TAG"
    DELETE = "DELETE"


class AccessDeniedException(ServiceException):
    """You do not have sufficient access to perform this action."""

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 400


class ConflictException(ServiceException):
    """This exception is thrown when the ``UpdateServer`` is called for a file
    transfer protocol-enabled server that has VPC as the endpoint type and
    the server's ``VpcEndpointID`` is not in the available state.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400


class InternalServiceError(ServiceException):
    """This exception is thrown when an error occurs in the Amazon Web
    ServicesTransfer Family service.
    """

    code: str = "InternalServiceError"
    sender_fault: bool = False
    status_code: int = 400


class InvalidNextTokenException(ServiceException):
    """The ``NextToken`` parameter that was passed is invalid."""

    code: str = "InvalidNextTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidRequestException(ServiceException):
    """This exception is thrown when the client submits a malformed request."""

    code: str = "InvalidRequestException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceExistsException(ServiceException):
    """The requested resource does not exist."""

    code: str = "ResourceExistsException"
    sender_fault: bool = False
    status_code: int = 400
    Resource: Resource
    ResourceType: ResourceType


class ResourceNotFoundException(ServiceException):
    """This exception is thrown when a resource is not found by the Amazon Web
    ServicesTransfer Family service.
    """

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400
    Resource: Resource
    ResourceType: ResourceType


class ServiceUnavailableException(ServiceException):
    """The request has failed because the Amazon Web ServicesTransfer Family
    service is not available.
    """

    code: str = "ServiceUnavailableException"
    sender_fault: bool = False
    status_code: int = 400


class ThrottlingException(ServiceException):
    """The request was denied due to request throttling."""

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 400
    RetryAfterSeconds: Optional[RetryAfterSeconds]


AddressAllocationIds = List[AddressAllocationId]


class As2ConnectorConfig(TypedDict, total=False):
    """Contains the details for a connector object. The connector object is
    used for AS2 outbound processes, to connect the Transfer Family customer
    with the trading partner.
    """

    LocalProfileId: Optional[ProfileId]
    PartnerProfileId: Optional[ProfileId]
    MessageSubject: Optional[MessageSubject]
    Compression: Optional[CompressionEnum]
    EncryptionAlgorithm: Optional[EncryptionAlg]
    SigningAlgorithm: Optional[SigningAlg]
    MdnSigningAlgorithm: Optional[MdnSigningAlg]
    MdnResponse: Optional[MdnResponse]


As2Transports = List[As2Transport]
CertDate = datetime
CertificateIds = List[CertificateId]


class EfsFileLocation(TypedDict, total=False):
    """Reserved for future use."""

    FileSystemId: Optional[EfsFileSystemId]
    Path: Optional[EfsPath]


class S3InputFileLocation(TypedDict, total=False):
    """Specifies the customer input S3 file location. If it is used inside
    ``copyStepDetails.DestinationFileLocation``, it should be the S3 copy
    destination.

    You need to provide the bucket and key. The key can represent either a
    path or a file. This is determined by whether or not you end the key
    value with the forward slash (/) character. If the final character is
    "/", then your file is copied to the folder, and its name does not
    change. If, rather, the final character is alphanumeric, your uploaded
    file is renamed to the path value. In this case, if a file with that
    name already exists, it is overwritten.

    For example, if your path is ``shared-files/bob/``, your uploaded files
    are copied to the ``shared-files/bob/``, folder. If your path is
    ``shared-files/today``, each uploaded file is copied to the
    ``shared-files`` folder and named ``today``: each upload overwrites the
    previous version of the *bob* file.
    """

    Bucket: Optional[S3Bucket]
    Key: Optional[S3Key]


class InputFileLocation(TypedDict, total=False):
    """Specifies the location for the file being copied. Only applicable for
    the Copy type of workflow steps.
    """

    S3FileLocation: Optional[S3InputFileLocation]
    EfsFileLocation: Optional[EfsFileLocation]


class CopyStepDetails(TypedDict, total=False):
    """Each step type has its own ``StepDetails`` structure."""

    Name: Optional[WorkflowStepName]
    DestinationFileLocation: Optional[InputFileLocation]
    OverwriteExisting: Optional[OverwriteExisting]
    SourceFileLocation: Optional[SourceFileLocation]


PosixId = int
SecondaryGids = List[PosixId]


class PosixProfile(TypedDict, total=False):
    """The full POSIX identity, including user ID (``Uid``), group ID
    (``Gid``), and any secondary groups IDs (``SecondaryGids``), that
    controls your users' access to your Amazon EFS file systems. The POSIX
    permissions that are set on files and directories in your file system
    determine the level of access your users get when transferring files
    into and out of your Amazon EFS file systems.
    """

    Uid: PosixId
    Gid: PosixId
    SecondaryGids: Optional[SecondaryGids]


class HomeDirectoryMapEntry(TypedDict, total=False):
    """Represents an object that contains entries and targets for
    ``HomeDirectoryMappings``.

    The following is an ``Entry`` and ``Target`` pair example for
    ``chroot``.

    ``[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]``
    """

    Entry: MapEntry
    Target: MapTarget


HomeDirectoryMappings = List[HomeDirectoryMapEntry]


class CreateAccessRequest(ServiceRequest):
    HomeDirectory: Optional[HomeDirectory]
    HomeDirectoryType: Optional[HomeDirectoryType]
    HomeDirectoryMappings: Optional[HomeDirectoryMappings]
    Policy: Optional[Policy]
    PosixProfile: Optional[PosixProfile]
    Role: Role
    ServerId: ServerId
    ExternalId: ExternalId


class CreateAccessResponse(TypedDict, total=False):
    ServerId: ServerId
    ExternalId: ExternalId


class Tag(TypedDict, total=False):
    """Creates a key-value pair for a specific resource. Tags are metadata that
    you can use to search for and group a resource for various purposes. You
    can apply tags to servers, users, and roles. A tag key can take more
    than one value. For example, to group servers for accounting purposes,
    you might create a tag called ``Group`` and assign the values
    ``Research`` and ``Accounting`` to that group.
    """

    Key: TagKey
    Value: TagValue


Tags = List[Tag]


class CreateAgreementRequest(ServiceRequest):
    Description: Optional[Description]
    ServerId: ServerId
    LocalProfileId: ProfileId
    PartnerProfileId: ProfileId
    BaseDirectory: HomeDirectory
    AccessRole: Role
    Status: Optional[AgreementStatusType]
    Tags: Optional[Tags]


class CreateAgreementResponse(TypedDict, total=False):
    AgreementId: AgreementId


class CreateConnectorRequest(ServiceRequest):
    Url: Url
    As2Config: As2ConnectorConfig
    AccessRole: Role
    LoggingRole: Optional[Role]
    Tags: Optional[Tags]


class CreateConnectorResponse(TypedDict, total=False):
    ConnectorId: ConnectorId


class CreateProfileRequest(ServiceRequest):
    As2Id: As2Id
    ProfileType: ProfileType
    CertificateIds: Optional[CertificateIds]
    Tags: Optional[Tags]


class CreateProfileResponse(TypedDict, total=False):
    ProfileId: ProfileId


class WorkflowDetail(TypedDict, total=False):
    """Specifies the workflow ID for the workflow to assign and the execution
    role that's used for executing the workflow.

    In addition to a workflow to execute when a file is uploaded completely,
    ``WorkflowDetails`` can also contain a workflow ID (and execution role)
    for a workflow to execute on partial upload. A partial upload occurs
    when a file is open when the session disconnects.
    """

    WorkflowId: WorkflowId
    ExecutionRole: Role


OnPartialUploadWorkflowDetails = List[WorkflowDetail]
OnUploadWorkflowDetails = List[WorkflowDetail]


class WorkflowDetails(TypedDict, total=False):
    """Container for the ``WorkflowDetail`` data type. It is used by actions
    that trigger a workflow to begin execution.
    """

    OnUpload: Optional[OnUploadWorkflowDetails]
    OnPartialUpload: Optional[OnPartialUploadWorkflowDetails]


class ProtocolDetails(TypedDict, total=False):
    """The protocol settings that are configured for your server."""

    PassiveIp: Optional[PassiveIp]
    TlsSessionResumptionMode: Optional[TlsSessionResumptionMode]
    SetStatOption: Optional[SetStatOption]
    As2Transports: Optional[As2Transports]


Protocols = List[Protocol]


class IdentityProviderDetails(TypedDict, total=False):
    """Returns information related to the type of user authentication that is
    in use for a file transfer protocol-enabled server's users. A server can
    have only one method of authentication.
    """

    Url: Optional[Url]
    InvocationRole: Optional[Role]
    DirectoryId: Optional[DirectoryId]
    Function: Optional[Function]


SecurityGroupIds = List[SecurityGroupId]
SubnetIds = List[SubnetId]


class EndpointDetails(TypedDict, total=False):
    """The virtual private cloud (VPC) endpoint settings that are configured
    for your file transfer protocol-enabled server. With a VPC endpoint, you
    can restrict access to your server and resources only within your VPC.
    To control incoming internet traffic, invoke the ``UpdateServer`` API
    and attach an Elastic IP address to your server's endpoint.

    After May 19, 2021, you won't be able to create a server using
    ``EndpointType=VPC_ENDPOINT`` in your Amazon Web Servicesaccount if your
    account hasn't already done so before May 19, 2021. If you have already
    created servers with ``EndpointType=VPC_ENDPOINT`` in your Amazon Web
    Servicesaccount on or before May 19, 2021, you will not be affected.
    After this date, use ``EndpointType`` = ``VPC``.

    For more information, see
    https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.
    """

    AddressAllocationIds: Optional[AddressAllocationIds]
    SubnetIds: Optional[SubnetIds]
    VpcEndpointId: Optional[VpcEndpointId]
    VpcId: Optional[VpcId]
    SecurityGroupIds: Optional[SecurityGroupIds]


class CreateServerRequest(ServiceRequest):
    Certificate: Optional[Certificate]
    Domain: Optional[Domain]
    EndpointDetails: Optional[EndpointDetails]
    EndpointType: Optional[EndpointType]
    HostKey: Optional[HostKey]
    IdentityProviderDetails: Optional[IdentityProviderDetails]
    IdentityProviderType: Optional[IdentityProviderType]
    LoggingRole: Optional[Role]
    PostAuthenticationLoginBanner: Optional[PostAuthenticationLoginBanner]
    PreAuthenticationLoginBanner: Optional[PreAuthenticationLoginBanner]
    Protocols: Optional[Protocols]
    ProtocolDetails: Optional[ProtocolDetails]
    SecurityPolicyName: Optional[SecurityPolicyName]
    Tags: Optional[Tags]
    WorkflowDetails: Optional[WorkflowDetails]


class CreateServerResponse(TypedDict, total=False):
    ServerId: ServerId


class CreateUserRequest(ServiceRequest):
    HomeDirectory: Optional[HomeDirectory]
    HomeDirectoryType: Optional[HomeDirectoryType]
    HomeDirectoryMappings: Optional[HomeDirectoryMappings]
    Policy: Optional[Policy]
    PosixProfile: Optional[PosixProfile]
    Role: Role
    ServerId: ServerId
    SshPublicKeyBody: Optional[SshPublicKeyBody]
    Tags: Optional[Tags]
    UserName: UserName


class CreateUserResponse(TypedDict, total=False):
    ServerId: ServerId
    UserName: UserName


class S3Tag(TypedDict, total=False):
    """Specifies the key-value pair that are assigned to a file during the
    execution of a Tagging step.
    """

    Key: S3TagKey
    Value: S3TagValue


S3Tags = List[S3Tag]


class TagStepDetails(TypedDict, total=False):
    """Each step type has its own ``StepDetails`` structure.

    The key/value pairs used to tag a file during the execution of a
    workflow step.
    """

    Name: Optional[WorkflowStepName]
    Tags: Optional[S3Tags]
    SourceFileLocation: Optional[SourceFileLocation]


class DeleteStepDetails(TypedDict, total=False):
    """The name of the step, used to identify the delete step."""

    Name: Optional[WorkflowStepName]
    SourceFileLocation: Optional[SourceFileLocation]


class CustomStepDetails(TypedDict, total=False):
    """Each step type has its own ``StepDetails`` structure."""

    Name: Optional[WorkflowStepName]
    Target: Optional[CustomStepTarget]
    TimeoutSeconds: Optional[CustomStepTimeoutSeconds]
    SourceFileLocation: Optional[SourceFileLocation]


class WorkflowStep(TypedDict, total=False):
    """The basic building block of a workflow."""

    Type: Optional[WorkflowStepType]
    CopyStepDetails: Optional[CopyStepDetails]
    CustomStepDetails: Optional[CustomStepDetails]
    DeleteStepDetails: Optional[DeleteStepDetails]
    TagStepDetails: Optional[TagStepDetails]


WorkflowSteps = List[WorkflowStep]


class CreateWorkflowRequest(ServiceRequest):
    Description: Optional[WorkflowDescription]
    Steps: WorkflowSteps
    OnExceptionSteps: Optional[WorkflowSteps]
    Tags: Optional[Tags]


class CreateWorkflowResponse(TypedDict, total=False):
    WorkflowId: WorkflowId


DateImported = datetime


class DeleteAccessRequest(ServiceRequest):
    ServerId: ServerId
    ExternalId: ExternalId


class DeleteAgreementRequest(ServiceRequest):
    AgreementId: AgreementId
    ServerId: ServerId


class DeleteCertificateRequest(ServiceRequest):
    CertificateId: CertificateId


class DeleteConnectorRequest(ServiceRequest):
    ConnectorId: ConnectorId


class DeleteHostKeyRequest(ServiceRequest):
    ServerId: ServerId
    HostKeyId: HostKeyId


class DeleteProfileRequest(ServiceRequest):
    ProfileId: ProfileId


class DeleteServerRequest(ServiceRequest):
    ServerId: ServerId


class DeleteSshPublicKeyRequest(ServiceRequest):
    ServerId: ServerId
    SshPublicKeyId: SshPublicKeyId
    UserName: UserName


class DeleteUserRequest(ServiceRequest):
    ServerId: ServerId
    UserName: UserName


class DeleteWorkflowRequest(ServiceRequest):
    WorkflowId: WorkflowId


class DescribeAccessRequest(ServiceRequest):
    ServerId: ServerId
    ExternalId: ExternalId


class DescribedAccess(TypedDict, total=False):
    """Describes the properties of the access that was specified."""

    HomeDirectory: Optional[HomeDirectory]
    HomeDirectoryMappings: Optional[HomeDirectoryMappings]
    HomeDirectoryType: Optional[HomeDirectoryType]
    Policy: Optional[Policy]
    PosixProfile: Optional[PosixProfile]
    Role: Optional[Role]
    ExternalId: Optional[ExternalId]


class DescribeAccessResponse(TypedDict, total=False):
    ServerId: ServerId
    Access: DescribedAccess


class DescribeAgreementRequest(ServiceRequest):
    AgreementId: AgreementId
    ServerId: ServerId


class DescribedAgreement(TypedDict, total=False):
    """Describes the properties of an agreement."""

    Arn: Arn
    AgreementId: Optional[AgreementId]
    Description: Optional[Description]
    Status: Optional[AgreementStatusType]
    ServerId: Optional[ServerId]
    LocalProfileId: Optional[ProfileId]
    PartnerProfileId: Optional[ProfileId]
    BaseDirectory: Optional[HomeDirectory]
    AccessRole: Optional[Role]
    Tags: Optional[Tags]


class DescribeAgreementResponse(TypedDict, total=False):
    Agreement: DescribedAgreement


class DescribeCertificateRequest(ServiceRequest):
    CertificateId: CertificateId


class DescribedCertificate(TypedDict, total=False):
    """Describes the properties of a certificate."""

    Arn: Arn
    CertificateId: Optional[CertificateId]
    Usage: Optional[CertificateUsageType]
    Status: Optional[CertificateStatusType]
    Certificate: Optional[CertificateBodyType]
    CertificateChain: Optional[CertificateChainType]
    ActiveDate: Optional[CertDate]
    InactiveDate: Optional[CertDate]
    Serial: Optional[CertSerial]
    NotBeforeDate: Optional[CertDate]
    NotAfterDate: Optional[CertDate]
    Type: Optional[CertificateType]
    Description: Optional[Description]
    Tags: Optional[Tags]


class DescribeCertificateResponse(TypedDict, total=False):
    Certificate: DescribedCertificate


class DescribeConnectorRequest(ServiceRequest):
    ConnectorId: ConnectorId


class DescribedConnector(TypedDict, total=False):
    """Describes the parameters for the connector, as identified by the
    ``ConnectorId``.
    """

    Arn: Arn
    ConnectorId: Optional[ConnectorId]
    Url: Optional[Url]
    As2Config: Optional[As2ConnectorConfig]
    AccessRole: Optional[Role]
    LoggingRole: Optional[Role]
    Tags: Optional[Tags]


class DescribeConnectorResponse(TypedDict, total=False):
    Connector: DescribedConnector


class DescribeExecutionRequest(ServiceRequest):
    ExecutionId: ExecutionId
    WorkflowId: WorkflowId


class ExecutionError(TypedDict, total=False):
    """Specifies the error message and type, for an error that occurs during
    the execution of the workflow.
    """

    Type: ExecutionErrorType
    Message: ExecutionErrorMessage


class ExecutionStepResult(TypedDict, total=False):
    """Specifies the following details for the step: error (if any), outputs
    (if any), and the step type.
    """

    StepType: Optional[WorkflowStepType]
    Outputs: Optional[StepResultOutputsJson]
    Error: Optional[ExecutionError]


ExecutionStepResults = List[ExecutionStepResult]


class ExecutionResults(TypedDict, total=False):
    """Specifies the steps in the workflow, as well as the steps to execute in
    case of any errors during workflow execution.
    """

    Steps: Optional[ExecutionStepResults]
    OnExceptionSteps: Optional[ExecutionStepResults]


class LoggingConfiguration(TypedDict, total=False):
    """Consists of the logging role and the log group name."""

    LoggingRole: Optional[Role]
    LogGroupName: Optional[LogGroupName]


class UserDetails(TypedDict, total=False):
    """Specifies the user name, server ID, and session ID for a workflow."""

    UserName: UserName
    ServerId: ServerId
    SessionId: Optional[SessionId]


class ServiceMetadata(TypedDict, total=False):
    """A container object for the session details that are associated with a
    workflow.
    """

    UserDetails: UserDetails


class S3FileLocation(TypedDict, total=False):
    """Specifies the details for the file location for the file that's being
    used in the workflow. Only applicable if you are using S3 storage.
    """

    Bucket: Optional[S3Bucket]
    Key: Optional[S3Key]
    VersionId: Optional[S3VersionId]
    Etag: Optional[S3Etag]


class FileLocation(TypedDict, total=False):
    """Specifies the Amazon S3 or EFS file details to be used in the step."""

    S3FileLocation: Optional[S3FileLocation]
    EfsFileLocation: Optional[EfsFileLocation]


class DescribedExecution(TypedDict, total=False):
    """The details for an execution object."""

    ExecutionId: Optional[ExecutionId]
    InitialFileLocation: Optional[FileLocation]
    ServiceMetadata: Optional[ServiceMetadata]
    ExecutionRole: Optional[Role]
    LoggingConfiguration: Optional[LoggingConfiguration]
    PosixProfile: Optional[PosixProfile]
    Status: Optional[ExecutionStatus]
    Results: Optional[ExecutionResults]


class DescribeExecutionResponse(TypedDict, total=False):
    WorkflowId: WorkflowId
    Execution: DescribedExecution


class DescribeHostKeyRequest(ServiceRequest):
    ServerId: ServerId
    HostKeyId: HostKeyId


class DescribedHostKey(TypedDict, total=False):
    """The details for a server host key."""

    Arn: Arn
    HostKeyId: Optional[HostKeyId]
    HostKeyFingerprint: Optional[HostKeyFingerprint]
    Description: Optional[HostKeyDescription]
    Type: Optional[HostKeyType]
    DateImported: Optional[DateImported]
    Tags: Optional[Tags]


class DescribeHostKeyResponse(TypedDict, total=False):
    HostKey: DescribedHostKey


class DescribeProfileRequest(ServiceRequest):
    ProfileId: ProfileId


class DescribedProfile(TypedDict, total=False):
    """The details for a local or partner AS2 profile."""

    Arn: Arn
    ProfileId: Optional[ProfileId]
    ProfileType: Optional[ProfileType]
    As2Id: Optional[As2Id]
    CertificateIds: Optional[CertificateIds]
    Tags: Optional[Tags]


class DescribeProfileResponse(TypedDict, total=False):
    Profile: DescribedProfile


class DescribeSecurityPolicyRequest(ServiceRequest):
    SecurityPolicyName: SecurityPolicyName


SecurityPolicyOptions = List[SecurityPolicyOption]


class DescribedSecurityPolicy(TypedDict, total=False):
    """Describes the properties of a security policy that was specified. For
    more information about security policies, see `Working with security
    policies <https://docs.aws.amazon.com/transfer/latest/userguide/security-policies.html>`__.
    """

    Fips: Optional[Fips]
    SecurityPolicyName: SecurityPolicyName
    SshCiphers: Optional[SecurityPolicyOptions]
    SshKexs: Optional[SecurityPolicyOptions]
    SshMacs: Optional[SecurityPolicyOptions]
    TlsCiphers: Optional[SecurityPolicyOptions]


class DescribeSecurityPolicyResponse(TypedDict, total=False):
    SecurityPolicy: DescribedSecurityPolicy


class DescribeServerRequest(ServiceRequest):
    ServerId: ServerId


class DescribedServer(TypedDict, total=False):
    """Describes the properties of a file transfer protocol-enabled server that
    was specified.
    """

    Arn: Arn
    Certificate: Optional[Certificate]
    ProtocolDetails: Optional[ProtocolDetails]
    Domain: Optional[Domain]
    EndpointDetails: Optional[EndpointDetails]
    EndpointType: Optional[EndpointType]
    HostKeyFingerprint: Optional[HostKeyFingerprint]
    IdentityProviderDetails: Optional[IdentityProviderDetails]
    IdentityProviderType: Optional[IdentityProviderType]
    LoggingRole: Optional[Role]
    PostAuthenticationLoginBanner: Optional[PostAuthenticationLoginBanner]
    PreAuthenticationLoginBanner: Optional[PreAuthenticationLoginBanner]
    Protocols: Optional[Protocols]
    SecurityPolicyName: Optional[SecurityPolicyName]
    ServerId: Optional[ServerId]
    State: Optional[State]
    Tags: Optional[Tags]
    UserCount: Optional[UserCount]
    WorkflowDetails: Optional[WorkflowDetails]


class DescribeServerResponse(TypedDict, total=False):
    Server: DescribedServer


class DescribeUserRequest(ServiceRequest):
    ServerId: ServerId
    UserName: UserName


class SshPublicKey(TypedDict, total=False):
    """Provides information about the public Secure Shell (SSH) key that is
    associated with a user account for the specific file transfer
    protocol-enabled server (as identified by ``ServerId``). The information
    returned includes the date the key was imported, the public key
    contents, and the public key ID. A user can store more than one SSH
    public key associated with their user name on a specific server.
    """

    DateImported: DateImported
    SshPublicKeyBody: SshPublicKeyBody
    SshPublicKeyId: SshPublicKeyId


SshPublicKeys = List[SshPublicKey]


class DescribedUser(TypedDict, total=False):
    """Describes the properties of a user that was specified."""

    Arn: Arn
    HomeDirectory: Optional[HomeDirectory]
    HomeDirectoryMappings: Optional[HomeDirectoryMappings]
    HomeDirectoryType: Optional[HomeDirectoryType]
    Policy: Optional[Policy]
    PosixProfile: Optional[PosixProfile]
    Role: Optional[Role]
    SshPublicKeys: Optional[SshPublicKeys]
    Tags: Optional[Tags]
    UserName: Optional[UserName]


class DescribeUserResponse(TypedDict, total=False):
    ServerId: ServerId
    User: DescribedUser


class DescribeWorkflowRequest(ServiceRequest):
    WorkflowId: WorkflowId


class DescribedWorkflow(TypedDict, total=False):
    """Describes the properties of the specified workflow"""

    Arn: Arn
    Description: Optional[WorkflowDescription]
    Steps: Optional[WorkflowSteps]
    OnExceptionSteps: Optional[WorkflowSteps]
    WorkflowId: Optional[WorkflowId]
    Tags: Optional[Tags]


class DescribeWorkflowResponse(TypedDict, total=False):
    Workflow: DescribedWorkflow


FilePaths = List[FilePath]


class ImportCertificateRequest(ServiceRequest):
    Usage: CertificateUsageType
    Certificate: CertificateBodyType
    CertificateChain: Optional[CertificateChainType]
    PrivateKey: Optional[PrivateKeyType]
    ActiveDate: Optional[CertDate]
    InactiveDate: Optional[CertDate]
    Description: Optional[Description]
    Tags: Optional[Tags]


class ImportCertificateResponse(TypedDict, total=False):
    CertificateId: CertificateId


class ImportHostKeyRequest(ServiceRequest):
    ServerId: ServerId
    HostKeyBody: HostKey
    Description: Optional[HostKeyDescription]
    Tags: Optional[Tags]


class ImportHostKeyResponse(TypedDict, total=False):
    ServerId: ServerId
    HostKeyId: HostKeyId


class ImportSshPublicKeyRequest(ServiceRequest):
    ServerId: ServerId
    SshPublicKeyBody: SshPublicKeyBody
    UserName: UserName


class ImportSshPublicKeyResponse(TypedDict, total=False):
    """Identifies the user, the server they belong to, and the identifier of
    the SSH public key associated with that user. A user can have more than
    one key on each server that they are associated with.
    """

    ServerId: ServerId
    SshPublicKeyId: SshPublicKeyId
    UserName: UserName


class ListAccessesRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    ServerId: ServerId


class ListedAccess(TypedDict, total=False):
    """Lists the properties for one or more specified associated accesses."""

    HomeDirectory: Optional[HomeDirectory]
    HomeDirectoryType: Optional[HomeDirectoryType]
    Role: Optional[Role]
    ExternalId: Optional[ExternalId]


ListedAccesses = List[ListedAccess]


class ListAccessesResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    ServerId: ServerId
    Accesses: ListedAccesses


class ListAgreementsRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    ServerId: ServerId


class ListedAgreement(TypedDict, total=False):
    """Describes the properties of an agreement."""

    Arn: Optional[Arn]
    AgreementId: Optional[AgreementId]
    Description: Optional[Description]
    Status: Optional[AgreementStatusType]
    ServerId: Optional[ServerId]
    LocalProfileId: Optional[ProfileId]
    PartnerProfileId: Optional[ProfileId]


ListedAgreements = List[ListedAgreement]


class ListAgreementsResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    Agreements: ListedAgreements


class ListCertificatesRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListedCertificate(TypedDict, total=False):
    """Describes the properties of a certificate."""

    Arn: Optional[Arn]
    CertificateId: Optional[CertificateId]
    Usage: Optional[CertificateUsageType]
    Status: Optional[CertificateStatusType]
    ActiveDate: Optional[CertDate]
    InactiveDate: Optional[CertDate]
    Type: Optional[CertificateType]
    Description: Optional[Description]


ListedCertificates = List[ListedCertificate]


class ListCertificatesResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    Certificates: ListedCertificates


class ListConnectorsRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListedConnector(TypedDict, total=False):
    """Returns details of the connector that is specified."""

    Arn: Optional[Arn]
    ConnectorId: Optional[ConnectorId]
    Url: Optional[Url]


ListedConnectors = List[ListedConnector]


class ListConnectorsResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    Connectors: ListedConnectors


class ListExecutionsRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    WorkflowId: WorkflowId


class ListedExecution(TypedDict, total=False):
    """Returns properties of the execution that is specified."""

    ExecutionId: Optional[ExecutionId]
    InitialFileLocation: Optional[FileLocation]
    ServiceMetadata: Optional[ServiceMetadata]
    Status: Optional[ExecutionStatus]


ListedExecutions = List[ListedExecution]


class ListExecutionsResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    WorkflowId: WorkflowId
    Executions: ListedExecutions


class ListHostKeysRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    ServerId: ServerId


class ListedHostKey(TypedDict, total=False):
    """Returns properties of the host key that's specified."""

    Arn: Arn
    HostKeyId: Optional[HostKeyId]
    Fingerprint: Optional[HostKeyFingerprint]
    Description: Optional[HostKeyDescription]
    Type: Optional[HostKeyType]
    DateImported: Optional[DateImported]


ListedHostKeys = List[ListedHostKey]


class ListHostKeysResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    ServerId: ServerId
    HostKeys: ListedHostKeys


class ListProfilesRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    ProfileType: Optional[ProfileType]


class ListedProfile(TypedDict, total=False):
    """Returns the properties of the profile that was specified."""

    Arn: Optional[Arn]
    ProfileId: Optional[ProfileId]
    As2Id: Optional[As2Id]
    ProfileType: Optional[ProfileType]


ListedProfiles = List[ListedProfile]


class ListProfilesResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    Profiles: ListedProfiles


class ListSecurityPoliciesRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


SecurityPolicyNames = List[SecurityPolicyName]


class ListSecurityPoliciesResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    SecurityPolicyNames: SecurityPolicyNames


class ListServersRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListedServer(TypedDict, total=False):
    """Returns properties of a file transfer protocol-enabled server that was
    specified.
    """

    Arn: Arn
    Domain: Optional[Domain]
    IdentityProviderType: Optional[IdentityProviderType]
    EndpointType: Optional[EndpointType]
    LoggingRole: Optional[Role]
    ServerId: Optional[ServerId]
    State: Optional[State]
    UserCount: Optional[UserCount]


ListedServers = List[ListedServer]


class ListServersResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    Servers: ListedServers


class ListTagsForResourceRequest(ServiceRequest):
    Arn: Arn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListTagsForResourceResponse(TypedDict, total=False):
    Arn: Optional[Arn]
    NextToken: Optional[NextToken]
    Tags: Optional[Tags]


class ListUsersRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    ServerId: ServerId


class ListedUser(TypedDict, total=False):
    """Returns properties of the user that you specify."""

    Arn: Arn
    HomeDirectory: Optional[HomeDirectory]
    HomeDirectoryType: Optional[HomeDirectoryType]
    Role: Optional[Role]
    SshPublicKeyCount: Optional[SshPublicKeyCount]
    UserName: Optional[UserName]


ListedUsers = List[ListedUser]


class ListUsersResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    ServerId: ServerId
    Users: ListedUsers


class ListWorkflowsRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListedWorkflow(TypedDict, total=False):
    """Contains the identifier, text description, and Amazon Resource Name
    (ARN) for the workflow.
    """

    WorkflowId: Optional[WorkflowId]
    Description: Optional[WorkflowDescription]
    Arn: Optional[Arn]


ListedWorkflows = List[ListedWorkflow]


class ListWorkflowsResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    Workflows: ListedWorkflows


class SendWorkflowStepStateRequest(ServiceRequest):
    WorkflowId: WorkflowId
    ExecutionId: ExecutionId
    Token: CallbackToken
    Status: CustomStepStatus


class SendWorkflowStepStateResponse(TypedDict, total=False):
    pass


class StartFileTransferRequest(ServiceRequest):
    ConnectorId: ConnectorId
    SendFilePaths: FilePaths


class StartFileTransferResponse(TypedDict, total=False):
    TransferId: TransferId


class StartServerRequest(ServiceRequest):
    ServerId: ServerId


class StopServerRequest(ServiceRequest):
    ServerId: ServerId


TagKeys = List[TagKey]


class TagResourceRequest(ServiceRequest):
    Arn: Arn
    Tags: Tags


class TestIdentityProviderRequest(ServiceRequest):
    ServerId: ServerId
    ServerProtocol: Optional[Protocol]
    SourceIp: Optional[SourceIp]
    UserName: UserName
    UserPassword: Optional[UserPassword]


class TestIdentityProviderResponse(TypedDict, total=False):
    Response: Optional[Response]
    StatusCode: StatusCode
    Message: Optional[Message]
    Url: Url


class UntagResourceRequest(ServiceRequest):
    Arn: Arn
    TagKeys: TagKeys


class UpdateAccessRequest(ServiceRequest):
    HomeDirectory: Optional[HomeDirectory]
    HomeDirectoryType: Optional[HomeDirectoryType]
    HomeDirectoryMappings: Optional[HomeDirectoryMappings]
    Policy: Optional[Policy]
    PosixProfile: Optional[PosixProfile]
    Role: Optional[Role]
    ServerId: ServerId
    ExternalId: ExternalId


class UpdateAccessResponse(TypedDict, total=False):
    ServerId: ServerId
    ExternalId: ExternalId


class UpdateAgreementRequest(ServiceRequest):
    AgreementId: AgreementId
    ServerId: ServerId
    Description: Optional[Description]
    Status: Optional[AgreementStatusType]
    LocalProfileId: Optional[ProfileId]
    PartnerProfileId: Optional[ProfileId]
    BaseDirectory: Optional[HomeDirectory]
    AccessRole: Optional[Role]


class UpdateAgreementResponse(TypedDict, total=False):
    AgreementId: AgreementId


class UpdateCertificateRequest(ServiceRequest):
    CertificateId: CertificateId
    ActiveDate: Optional[CertDate]
    InactiveDate: Optional[CertDate]
    Description: Optional[Description]


class UpdateCertificateResponse(TypedDict, total=False):
    CertificateId: CertificateId


class UpdateConnectorRequest(ServiceRequest):
    ConnectorId: ConnectorId
    Url: Optional[Url]
    As2Config: Optional[As2ConnectorConfig]
    AccessRole: Optional[Role]
    LoggingRole: Optional[Role]


class UpdateConnectorResponse(TypedDict, total=False):
    ConnectorId: ConnectorId


class UpdateHostKeyRequest(ServiceRequest):
    ServerId: ServerId
    HostKeyId: HostKeyId
    Description: HostKeyDescription


class UpdateHostKeyResponse(TypedDict, total=False):
    ServerId: ServerId
    HostKeyId: HostKeyId


class UpdateProfileRequest(ServiceRequest):
    ProfileId: ProfileId
    CertificateIds: Optional[CertificateIds]


class UpdateProfileResponse(TypedDict, total=False):
    ProfileId: ProfileId


class UpdateServerRequest(ServiceRequest):
    Certificate: Optional[Certificate]
    ProtocolDetails: Optional[ProtocolDetails]
    EndpointDetails: Optional[EndpointDetails]
    EndpointType: Optional[EndpointType]
    HostKey: Optional[HostKey]
    IdentityProviderDetails: Optional[IdentityProviderDetails]
    LoggingRole: Optional[NullableRole]
    PostAuthenticationLoginBanner: Optional[PostAuthenticationLoginBanner]
    PreAuthenticationLoginBanner: Optional[PreAuthenticationLoginBanner]
    Protocols: Optional[Protocols]
    SecurityPolicyName: Optional[SecurityPolicyName]
    ServerId: ServerId
    WorkflowDetails: Optional[WorkflowDetails]


class UpdateServerResponse(TypedDict, total=False):
    ServerId: ServerId


class UpdateUserRequest(ServiceRequest):
    HomeDirectory: Optional[HomeDirectory]
    HomeDirectoryType: Optional[HomeDirectoryType]
    HomeDirectoryMappings: Optional[HomeDirectoryMappings]
    Policy: Optional[Policy]
    PosixProfile: Optional[PosixProfile]
    Role: Optional[Role]
    ServerId: ServerId
    UserName: UserName


class UpdateUserResponse(TypedDict, total=False):
    """``UpdateUserResponse`` returns the user name and identifier for the
    request to update a user's properties.
    """

    ServerId: ServerId
    UserName: UserName


class TransferApi:

    service = "transfer"
    version = "2018-11-05"

    @handler("CreateAccess")
    def create_access(
        self,
        context: RequestContext,
        role: Role,
        server_id: ServerId,
        external_id: ExternalId,
        home_directory: HomeDirectory = None,
        home_directory_type: HomeDirectoryType = None,
        home_directory_mappings: HomeDirectoryMappings = None,
        policy: Policy = None,
        posix_profile: PosixProfile = None,
    ) -> CreateAccessResponse:
        """Used by administrators to choose which groups in the directory should
        have access to upload and download files over the enabled protocols
        using Transfer Family. For example, a Microsoft Active Directory might
        contain 50,000 users, but only a small fraction might need the ability
        to transfer files to the server. An administrator can use
        ``CreateAccess`` to limit the access to the correct set of users who
        need this ability.

        :param role: The Amazon Resource Name (ARN) of the Identity and Access Management
        (IAM) role that controls your users' access to your Amazon S3 bucket or
        Amazon EFS file system.
        :param server_id: A system-assigned unique identifier for a server instance.
        :param external_id: A unique identifier that is required to identify specific groups within
        your directory.
        :param home_directory: The landing directory (folder) for a user when they log in to the server
        using the client.
        :param home_directory_type: The type of landing directory (folder) that you want your users' home
        directory to be when they log in to the server.
        :param home_directory_mappings: Logical directory mappings that specify what Amazon S3 or Amazon EFS
        paths and keys should be visible to your user and how you want to make
        them visible.
        :param policy: A session policy for your user so that you can use the same Identity and
        Access Management (IAM) role across multiple users.
        :param posix_profile: The full POSIX identity, including user ID (``Uid``), group ID
        (``Gid``), and any secondary groups IDs (``SecondaryGids``), that
        controls your users' access to your Amazon EFS file systems.
        :returns: CreateAccessResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("CreateAgreement")
    def create_agreement(
        self,
        context: RequestContext,
        server_id: ServerId,
        local_profile_id: ProfileId,
        partner_profile_id: ProfileId,
        base_directory: HomeDirectory,
        access_role: Role,
        description: Description = None,
        status: AgreementStatusType = None,
        tags: Tags = None,
    ) -> CreateAgreementResponse:
        """Creates an agreement. An agreement is a bilateral trading partner
        agreement, or partnership, between an Transfer Family server and an AS2
        process. The agreement defines the file and message transfer
        relationship between the server and the AS2 process. To define an
        agreement, Transfer Family combines a server, local profile, partner
        profile, certificate, and other attributes.

        The partner is identified with the ``PartnerProfileId``, and the AS2
        process is identified with the ``LocalProfileId``.

        :param server_id: A system-assigned unique identifier for a server instance.
        :param local_profile_id: A unique identifier for the AS2 local profile.
        :param partner_profile_id: A unique identifier for the partner profile used in the agreement.
        :param base_directory: The landing directory (folder) for files transferred by using the AS2
        protocol.
        :param access_role: With AS2, you can send files by calling ``StartFileTransfer`` and
        specifying the file paths in the request parameter, ``SendFilePaths``.
        :param description: A name or short description to identify the agreement.
        :param status: The status of the agreement.
        :param tags: Key-value pairs that can be used to group and search for agreements.
        :returns: CreateAgreementResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateConnector")
    def create_connector(
        self,
        context: RequestContext,
        url: Url,
        as2_config: As2ConnectorConfig,
        access_role: Role,
        logging_role: Role = None,
        tags: Tags = None,
    ) -> CreateConnectorResponse:
        """Creates the connector, which captures the parameters for an outbound
        connection for the AS2 protocol. The connector is required for sending
        files to an externally hosted AS2 server. For more details about
        connectors, see `Create AS2
        connectors <https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html#configure-as2-connector>`__.

        :param url: The URL of the partner's AS2 endpoint.
        :param as2_config: A structure that contains the parameters for a connector object.
        :param access_role: With AS2, you can send files by calling ``StartFileTransfer`` and
        specifying the file paths in the request parameter, ``SendFilePaths``.
        :param logging_role: The Amazon Resource Name (ARN) of the Identity and Access Management
        (IAM) role that allows a connector to turn on CloudWatch logging for
        Amazon S3 events.
        :param tags: Key-value pairs that can be used to group and search for connectors.
        :returns: CreateConnectorResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateProfile")
    def create_profile(
        self,
        context: RequestContext,
        as2_id: As2Id,
        profile_type: ProfileType,
        certificate_ids: CertificateIds = None,
        tags: Tags = None,
    ) -> CreateProfileResponse:
        """Creates the local or partner profile to use for AS2 transfers.

        :param as2_id: The ``As2Id`` is the *AS2-name*, as defined in the `RFC
        4130 <https://datatracker.
        :param profile_type: Determines the type of profile to create:

        -  Specify ``LOCAL`` to create a local profile.
        :param certificate_ids: An array of identifiers for the imported certificates.
        :param tags: Key-value pairs that can be used to group and search for AS2 profiles.
        :returns: CreateProfileResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateServer")
    def create_server(
        self,
        context: RequestContext,
        certificate: Certificate = None,
        domain: Domain = None,
        endpoint_details: EndpointDetails = None,
        endpoint_type: EndpointType = None,
        host_key: HostKey = None,
        identity_provider_details: IdentityProviderDetails = None,
        identity_provider_type: IdentityProviderType = None,
        logging_role: Role = None,
        post_authentication_login_banner: PostAuthenticationLoginBanner = None,
        pre_authentication_login_banner: PreAuthenticationLoginBanner = None,
        protocols: Protocols = None,
        protocol_details: ProtocolDetails = None,
        security_policy_name: SecurityPolicyName = None,
        tags: Tags = None,
        workflow_details: WorkflowDetails = None,
    ) -> CreateServerResponse:
        """Instantiates an auto-scaling virtual server based on the selected file
        transfer protocol in Amazon Web Services. When you make updates to your
        file transfer protocol-enabled server or when you work with users, use
        the service-generated ``ServerId`` property that is assigned to the
        newly created server.

        :param certificate: The Amazon Resource Name (ARN) of the Certificate Manager (ACM)
        certificate.
        :param domain: The domain of the storage system that is used for file transfers.
        :param endpoint_details: The virtual private cloud (VPC) endpoint settings that are configured
        for your server.
        :param endpoint_type: The type of endpoint that you want your server to use.
        :param host_key: The RSA, ECDSA, or ED25519 private key to use for your SFTP-enabled
        server.
        :param identity_provider_details: Required when ``IdentityProviderType`` is set to
        ``AWS_DIRECTORY_SERVICE`` or ``API_GATEWAY``.
        :param identity_provider_type: The mode of authentication for a server.
        :param logging_role: The Amazon Resource Name (ARN) of the Identity and Access Management
        (IAM) role that allows a server to turn on Amazon CloudWatch logging for
        Amazon S3 or Amazon EFSevents.
        :param post_authentication_login_banner: Specifies a string to display when users connect to a server.
        :param pre_authentication_login_banner: Specifies a string to display when users connect to a server.
        :param protocols: Specifies the file transfer protocol or protocols over which your file
        transfer protocol client can connect to your server's endpoint.
        :param protocol_details: The protocol settings that are configured for your server.
        :param security_policy_name: Specifies the name of the security policy that is attached to the
        server.
        :param tags: Key-value pairs that can be used to group and search for servers.
        :param workflow_details: Specifies the workflow ID for the workflow to assign and the execution
        role that's used for executing the workflow.
        :returns: CreateServerResponse
        :raises AccessDeniedException:
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateUser")
    def create_user(
        self,
        context: RequestContext,
        role: Role,
        server_id: ServerId,
        user_name: UserName,
        home_directory: HomeDirectory = None,
        home_directory_type: HomeDirectoryType = None,
        home_directory_mappings: HomeDirectoryMappings = None,
        policy: Policy = None,
        posix_profile: PosixProfile = None,
        ssh_public_key_body: SshPublicKeyBody = None,
        tags: Tags = None,
    ) -> CreateUserResponse:
        """Creates a user and associates them with an existing file transfer
        protocol-enabled server. You can only create and associate users with
        servers that have the ``IdentityProviderType`` set to
        ``SERVICE_MANAGED``. Using parameters for ``CreateUser``, you can
        specify the user name, set the home directory, store the user's public
        key, and assign the user's Identity and Access Management (IAM) role.
        You can also optionally add a session policy, and assign metadata with
        tags that can be used to group and search for users.

        :param role: The Amazon Resource Name (ARN) of the Identity and Access Management
        (IAM) role that controls your users' access to your Amazon S3 bucket or
        Amazon EFS file system.
        :param server_id: A system-assigned unique identifier for a server instance.
        :param user_name: A unique string that identifies a user and is associated with a
        ``ServerId``.
        :param home_directory: The landing directory (folder) for a user when they log in to the server
        using the client.
        :param home_directory_type: The type of landing directory (folder) that you want your users' home
        directory to be when they log in to the server.
        :param home_directory_mappings: Logical directory mappings that specify what Amazon S3 or Amazon EFS
        paths and keys should be visible to your user and how you want to make
        them visible.
        :param policy: A session policy for your user so that you can use the same Identity and
        Access Management (IAM) role across multiple users.
        :param posix_profile: Specifies the full POSIX identity, including user ID (``Uid``), group ID
        (``Gid``), and any secondary groups IDs (``SecondaryGids``), that
        controls your users' access to your Amazon EFS file systems.
        :param ssh_public_key_body: The public portion of the Secure Shell (SSH) key used to authenticate
        the user to the server.
        :param tags: Key-value pairs that can be used to group and search for users.
        :returns: CreateUserResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("CreateWorkflow")
    def create_workflow(
        self,
        context: RequestContext,
        steps: WorkflowSteps,
        description: WorkflowDescription = None,
        on_exception_steps: WorkflowSteps = None,
        tags: Tags = None,
    ) -> CreateWorkflowResponse:
        """Allows you to create a workflow with specified steps and step details
        the workflow invokes after file transfer completes. After creating a
        workflow, you can associate the workflow created with any transfer
        servers by specifying the ``workflow-details`` field in ``CreateServer``
        and ``UpdateServer`` operations.

        :param steps: Specifies the details for the steps that are in the specified workflow.
        :param description: A textual description for the workflow.
        :param on_exception_steps: Specifies the steps (actions) to take if errors are encountered during
        execution of the workflow.
        :param tags: Key-value pairs that can be used to group and search for workflows.
        :returns: CreateWorkflowResponse
        :raises AccessDeniedException:
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteAccess")
    def delete_access(
        self, context: RequestContext, server_id: ServerId, external_id: ExternalId
    ) -> None:
        """Allows you to delete the access specified in the ``ServerID`` and
        ``ExternalID`` parameters.

        :param server_id: A system-assigned unique identifier for a server that has this user
        assigned.
        :param external_id: A unique identifier that is required to identify specific groups within
        your directory.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteAgreement")
    def delete_agreement(
        self, context: RequestContext, agreement_id: AgreementId, server_id: ServerId
    ) -> None:
        """Delete the agreement that's specified in the provided ``AgreementId``.

        :param agreement_id: A unique identifier for the agreement.
        :param server_id: The server identifier associated with the agreement that you are
        deleting.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteCertificate")
    def delete_certificate(self, context: RequestContext, certificate_id: CertificateId) -> None:
        """Deletes the certificate that's specified in the ``CertificateId``
        parameter.

        :param certificate_id: The identifier of the certificate object that you are deleting.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteConnector")
    def delete_connector(self, context: RequestContext, connector_id: ConnectorId) -> None:
        """Deletes the agreement that's specified in the provided ``ConnectorId``.

        :param connector_id: The unique identifier for the connector.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteHostKey")
    def delete_host_key(
        self, context: RequestContext, server_id: ServerId, host_key_id: HostKeyId
    ) -> None:
        """Deletes the host key that's specified in the ``HoskKeyId`` parameter.

        :param server_id: The identifier of the server that contains the host key that you are
        deleting.
        :param host_key_id: The identifier of the host key that you are deleting.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteProfile")
    def delete_profile(self, context: RequestContext, profile_id: ProfileId) -> None:
        """Deletes the profile that's specified in the ``ProfileId`` parameter.

        :param profile_id: The identifier of the profile that you are deleting.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteServer")
    def delete_server(self, context: RequestContext, server_id: ServerId) -> None:
        """Deletes the file transfer protocol-enabled server that you specify.

        No response returns from this operation.

        :param server_id: A unique system-assigned identifier for a server instance.
        :raises AccessDeniedException:
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteSshPublicKey")
    def delete_ssh_public_key(
        self,
        context: RequestContext,
        server_id: ServerId,
        ssh_public_key_id: SshPublicKeyId,
        user_name: UserName,
    ) -> None:
        """Deletes a user's Secure Shell (SSH) public key.

        :param server_id: A system-assigned unique identifier for a file transfer protocol-enabled
        server instance that has the user assigned to it.
        :param ssh_public_key_id: A unique identifier used to reference your user's specific SSH key.
        :param user_name: A unique string that identifies a user whose public key is being
        deleted.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteUser")
    def delete_user(
        self, context: RequestContext, server_id: ServerId, user_name: UserName
    ) -> None:
        """Deletes the user belonging to a file transfer protocol-enabled server
        you specify.

        No response returns from this operation.

        When you delete a user from a server, the user's information is lost.

        :param server_id: A system-assigned unique identifier for a server instance that has the
        user assigned to it.
        :param user_name: A unique string that identifies a user that is being deleted from a
        server.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteWorkflow")
    def delete_workflow(self, context: RequestContext, workflow_id: WorkflowId) -> None:
        """Deletes the specified workflow.

        :param workflow_id: A unique identifier for the workflow.
        :raises AccessDeniedException:
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeAccess")
    def describe_access(
        self, context: RequestContext, server_id: ServerId, external_id: ExternalId
    ) -> DescribeAccessResponse:
        """Describes the access that is assigned to the specific file transfer
        protocol-enabled server, as identified by its ``ServerId`` property and
        its ``ExternalId``.

        The response from this call returns the properties of the access that is
        associated with the ``ServerId`` value that was specified.

        :param server_id: A system-assigned unique identifier for a server that has this access
        assigned.
        :param external_id: A unique identifier that is required to identify specific groups within
        your directory.
        :returns: DescribeAccessResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeAgreement")
    def describe_agreement(
        self, context: RequestContext, agreement_id: AgreementId, server_id: ServerId
    ) -> DescribeAgreementResponse:
        """Describes the agreement that's identified by the ``AgreementId``.

        :param agreement_id: A unique identifier for the agreement.
        :param server_id: The server identifier that's associated with the agreement.
        :returns: DescribeAgreementResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeCertificate")
    def describe_certificate(
        self, context: RequestContext, certificate_id: CertificateId
    ) -> DescribeCertificateResponse:
        """Describes the certificate that's identified by the ``CertificateId``.

        :param certificate_id: An array of identifiers for the imported certificates.
        :returns: DescribeCertificateResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeConnector")
    def describe_connector(
        self, context: RequestContext, connector_id: ConnectorId
    ) -> DescribeConnectorResponse:
        """Describes the connector that's identified by the ``ConnectorId.``

        :param connector_id: The unique identifier for the connector.
        :returns: DescribeConnectorResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeExecution")
    def describe_execution(
        self, context: RequestContext, execution_id: ExecutionId, workflow_id: WorkflowId
    ) -> DescribeExecutionResponse:
        """You can use ``DescribeExecution`` to check the details of the execution
        of the specified workflow.

        :param execution_id: A unique identifier for the execution of a workflow.
        :param workflow_id: A unique identifier for the workflow.
        :returns: DescribeExecutionResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeHostKey")
    def describe_host_key(
        self, context: RequestContext, server_id: ServerId, host_key_id: HostKeyId
    ) -> DescribeHostKeyResponse:
        """Returns the details of the host key that's specified by the
        ``HostKeyId`` and ``ServerId``.

        :param server_id: The identifier of the server that contains the host key that you want
        described.
        :param host_key_id: The identifier of the host key that you want described.
        :returns: DescribeHostKeyResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeProfile")
    def describe_profile(
        self, context: RequestContext, profile_id: ProfileId
    ) -> DescribeProfileResponse:
        """Returns the details of the profile that's specified by the
        ``ProfileId``.

        :param profile_id: The identifier of the profile that you want described.
        :returns: DescribeProfileResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeSecurityPolicy")
    def describe_security_policy(
        self, context: RequestContext, security_policy_name: SecurityPolicyName
    ) -> DescribeSecurityPolicyResponse:
        """Describes the security policy that is attached to your file transfer
        protocol-enabled server. The response contains a description of the
        security policy's properties. For more information about security
        policies, see `Working with security
        policies <https://docs.aws.amazon.com/transfer/latest/userguide/security-policies.html>`__.

        :param security_policy_name: Specifies the name of the security policy that is attached to the
        server.
        :returns: DescribeSecurityPolicyResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeServer")
    def describe_server(
        self, context: RequestContext, server_id: ServerId
    ) -> DescribeServerResponse:
        """Describes a file transfer protocol-enabled server that you specify by
        passing the ``ServerId`` parameter.

        The response contains a description of a server's properties. When you
        set ``EndpointType`` to VPC, the response will contain the
        ``EndpointDetails``.

        :param server_id: A system-assigned unique identifier for a server.
        :returns: DescribeServerResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeUser")
    def describe_user(
        self, context: RequestContext, server_id: ServerId, user_name: UserName
    ) -> DescribeUserResponse:
        """Describes the user assigned to the specific file transfer
        protocol-enabled server, as identified by its ``ServerId`` property.

        The response from this call returns the properties of the user
        associated with the ``ServerId`` value that was specified.

        :param server_id: A system-assigned unique identifier for a server that has this user
        assigned.
        :param user_name: The name of the user assigned to one or more servers.
        :returns: DescribeUserResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeWorkflow")
    def describe_workflow(
        self, context: RequestContext, workflow_id: WorkflowId
    ) -> DescribeWorkflowResponse:
        """Describes the specified workflow.

        :param workflow_id: A unique identifier for the workflow.
        :returns: DescribeWorkflowResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ImportCertificate")
    def import_certificate(
        self,
        context: RequestContext,
        usage: CertificateUsageType,
        certificate: CertificateBodyType,
        certificate_chain: CertificateChainType = None,
        private_key: PrivateKeyType = None,
        active_date: CertDate = None,
        inactive_date: CertDate = None,
        description: Description = None,
        tags: Tags = None,
    ) -> ImportCertificateResponse:
        """Imports the signing and encryption certificates that you need to create
        local (AS2) profiles and partner profiles.

        :param usage: Specifies whether this certificate is used for signing or encryption.
        :param certificate: The file that contains the certificate to import.
        :param certificate_chain: An optional list of certificates that make up the chain for the
        certificate that's being imported.
        :param private_key: The file that contains the private key for the certificate that's being
        imported.
        :param active_date: An optional date that specifies when the certificate becomes active.
        :param inactive_date: An optional date that specifies when the certificate becomes inactive.
        :param description: A short description that helps identify the certificate.
        :param tags: Key-value pairs that can be used to group and search for certificates.
        :returns: ImportCertificateResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ImportHostKey")
    def import_host_key(
        self,
        context: RequestContext,
        server_id: ServerId,
        host_key_body: HostKey,
        description: HostKeyDescription = None,
        tags: Tags = None,
    ) -> ImportHostKeyResponse:
        """Adds a host key to the server that's specified by the ``ServerId``
        parameter.

        :param server_id: The identifier of the server that contains the host key that you are
        importing.
        :param host_key_body: The public key portion of an SSH key pair.
        :param description: The text description that identifies this host key.
        :param tags: Key-value pairs that can be used to group and search for host keys.
        :returns: ImportHostKeyResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ImportSshPublicKey")
    def import_ssh_public_key(
        self,
        context: RequestContext,
        server_id: ServerId,
        ssh_public_key_body: SshPublicKeyBody,
        user_name: UserName,
    ) -> ImportSshPublicKeyResponse:
        """Adds a Secure Shell (SSH) public key to a user account identified by a
        ``UserName`` value assigned to the specific file transfer
        protocol-enabled server, identified by ``ServerId``.

        The response returns the ``UserName`` value, the ``ServerId`` value, and
        the name of the ``SshPublicKeyId``.

        :param server_id: A system-assigned unique identifier for a server.
        :param ssh_public_key_body: The public key portion of an SSH key pair.
        :param user_name: The name of the user account that is assigned to one or more servers.
        :returns: ImportSshPublicKeyResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListAccesses")
    def list_accesses(
        self,
        context: RequestContext,
        server_id: ServerId,
        max_results: MaxResults = None,
        next_token: NextToken = None,
    ) -> ListAccessesResponse:
        """Lists the details for all the accesses you have on your server.

        :param server_id: A system-assigned unique identifier for a server that has users assigned
        to it.
        :param max_results: Specifies the maximum number of access SIDs to return.
        :param next_token: When you can get additional results from the ``ListAccesses`` call, a
        ``NextToken`` parameter is returned in the output.
        :returns: ListAccessesResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListAgreements")
    def list_agreements(
        self,
        context: RequestContext,
        server_id: ServerId,
        max_results: MaxResults = None,
        next_token: NextToken = None,
    ) -> ListAgreementsResponse:
        """Returns a list of the agreements for the server that's identified by the
        ``ServerId`` that you supply. If you want to limit the results to a
        certain number, supply a value for the ``MaxResults`` parameter. If you
        ran the command previously and received a value for ``NextToken``, you
        can supply that value to continue listing agreements from where you left
        off.

        :param server_id: The identifier of the server for which you want a list of agreements.
        :param max_results: The maximum number of agreements to return.
        :param next_token: When you can get additional results from the ``ListAgreements`` call, a
        ``NextToken`` parameter is returned in the output.
        :returns: ListAgreementsResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListCertificates")
    def list_certificates(
        self, context: RequestContext, max_results: MaxResults = None, next_token: NextToken = None
    ) -> ListCertificatesResponse:
        """Returns a list of the current certificates that have been imported into
        Transfer Family. If you want to limit the results to a certain number,
        supply a value for the ``MaxResults`` parameter. If you ran the command
        previously and received a value for the ``NextToken`` parameter, you can
        supply that value to continue listing certificates from where you left
        off.

        :param max_results: The maximum number of certificates to return.
        :param next_token: When you can get additional results from the ``ListCertificates`` call,
        a ``NextToken`` parameter is returned in the output.
        :returns: ListCertificatesResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListConnectors")
    def list_connectors(
        self, context: RequestContext, max_results: MaxResults = None, next_token: NextToken = None
    ) -> ListConnectorsResponse:
        """Lists the connectors for the specified Region.

        :param max_results: The maximum number of connectors to return.
        :param next_token: When you can get additional results from the ``ListConnectors`` call, a
        ``NextToken`` parameter is returned in the output.
        :returns: ListConnectorsResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListExecutions")
    def list_executions(
        self,
        context: RequestContext,
        workflow_id: WorkflowId,
        max_results: MaxResults = None,
        next_token: NextToken = None,
    ) -> ListExecutionsResponse:
        """Lists all executions for the specified workflow.

        :param workflow_id: A unique identifier for the workflow.
        :param max_results: Specifies the maximum number of executions to return.
        :param next_token: ``ListExecutions`` returns the ``NextToken`` parameter in the output.
        :returns: ListExecutionsResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListHostKeys")
    def list_host_keys(
        self,
        context: RequestContext,
        server_id: ServerId,
        max_results: MaxResults = None,
        next_token: NextToken = None,
    ) -> ListHostKeysResponse:
        """Returns a list of host keys for the server that's specified by the
        ``ServerId`` parameter.

        :param server_id: The identifier of the server that contains the host keys that you want
        to view.
        :param max_results: The maximum number of host keys to return.
        :param next_token: When there are additional results that were not returned, a
        ``NextToken`` parameter is returned.
        :returns: ListHostKeysResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListProfiles")
    def list_profiles(
        self,
        context: RequestContext,
        max_results: MaxResults = None,
        next_token: NextToken = None,
        profile_type: ProfileType = None,
    ) -> ListProfilesResponse:
        """Returns a list of the profiles for your system. If you want to limit the
        results to a certain number, supply a value for the ``MaxResults``
        parameter. If you ran the command previously and received a value for
        ``NextToken``, you can supply that value to continue listing profiles
        from where you left off.

        :param max_results: The maximum number of profiles to return.
        :param next_token: When there are additional results that were not returned, a
        ``NextToken`` parameter is returned.
        :param profile_type: Indicates whether to list only ``LOCAL`` type profiles or only
        ``PARTNER`` type profiles.
        :returns: ListProfilesResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListSecurityPolicies")
    def list_security_policies(
        self, context: RequestContext, max_results: MaxResults = None, next_token: NextToken = None
    ) -> ListSecurityPoliciesResponse:
        """Lists the security policies that are attached to your file transfer
        protocol-enabled servers.

        :param max_results: Specifies the number of security policies to return as a response to the
        ``ListSecurityPolicies`` query.
        :param next_token: When additional results are obtained from the ``ListSecurityPolicies``
        command, a ``NextToken`` parameter is returned in the output.
        :returns: ListSecurityPoliciesResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("ListServers")
    def list_servers(
        self, context: RequestContext, max_results: MaxResults = None, next_token: NextToken = None
    ) -> ListServersResponse:
        """Lists the file transfer protocol-enabled servers that are associated
        with your Amazon Web Services account.

        :param max_results: Specifies the number of servers to return as a response to the
        ``ListServers`` query.
        :param next_token: When additional results are obtained from the ``ListServers`` command, a
        ``NextToken`` parameter is returned in the output.
        :returns: ListServersResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self,
        context: RequestContext,
        arn: Arn,
        max_results: MaxResults = None,
        next_token: NextToken = None,
    ) -> ListTagsForResourceResponse:
        """Lists all of the tags associated with the Amazon Resource Name (ARN)
        that you specify. The resource can be a user, server, or role.

        :param arn: Requests the tags associated with a particular Amazon Resource Name
        (ARN).
        :param max_results: Specifies the number of tags to return as a response to the
        ``ListTagsForResource`` request.
        :param next_token: When you request additional results from the ``ListTagsForResource``
        operation, a ``NextToken`` parameter is returned in the input.
        :returns: ListTagsForResourceResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("ListUsers")
    def list_users(
        self,
        context: RequestContext,
        server_id: ServerId,
        max_results: MaxResults = None,
        next_token: NextToken = None,
    ) -> ListUsersResponse:
        """Lists the users for a file transfer protocol-enabled server that you
        specify by passing the ``ServerId`` parameter.

        :param server_id: A system-assigned unique identifier for a server that has users assigned
        to it.
        :param max_results: Specifies the number of users to return as a response to the
        ``ListUsers`` request.
        :param next_token: When you can get additional results from the ``ListUsers`` call, a
        ``NextToken`` parameter is returned in the output.
        :returns: ListUsersResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListWorkflows")
    def list_workflows(
        self, context: RequestContext, max_results: MaxResults = None, next_token: NextToken = None
    ) -> ListWorkflowsResponse:
        """Lists all of your workflows.

        :param max_results: Specifies the maximum number of workflows to return.
        :param next_token: ``ListWorkflows`` returns the ``NextToken`` parameter in the output.
        :returns: ListWorkflowsResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidNextTokenException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("SendWorkflowStepState")
    def send_workflow_step_state(
        self,
        context: RequestContext,
        workflow_id: WorkflowId,
        execution_id: ExecutionId,
        token: CallbackToken,
        status: CustomStepStatus,
    ) -> SendWorkflowStepStateResponse:
        """Sends a callback for asynchronous custom steps.

        The ``ExecutionId``, ``WorkflowId``, and ``Token`` are passed to the
        target resource during execution of a custom step of a workflow. You
        must include those with their callback as well as providing a status.

        :param workflow_id: A unique identifier for the workflow.
        :param execution_id: A unique identifier for the execution of a workflow.
        :param token: Used to distinguish between multiple callbacks for multiple Lambda steps
        within the same execution.
        :param status: Indicates whether the specified step succeeded or failed.
        :returns: SendWorkflowStepStateResponse
        :raises AccessDeniedException:
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("StartFileTransfer")
    def start_file_transfer(
        self, context: RequestContext, connector_id: ConnectorId, send_file_paths: FilePaths
    ) -> StartFileTransferResponse:
        """Begins an outbound file transfer to a remote AS2 server. You specify the
        ``ConnectorId`` and the file paths for where to send the files.

        :param connector_id: The unique identifier for the connector.
        :param send_file_paths: An array of strings.
        :returns: StartFileTransferResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("StartServer")
    def start_server(self, context: RequestContext, server_id: ServerId) -> None:
        """Changes the state of a file transfer protocol-enabled server from
        ``OFFLINE`` to ``ONLINE``. It has no impact on a server that is already
        ``ONLINE``. An ``ONLINE`` server can accept and process file transfer
        jobs.

        The state of ``STARTING`` indicates that the server is in an
        intermediate state, either not fully able to respond, or not fully
        online. The values of ``START_FAILED`` can indicate an error condition.

        No response is returned from this call.

        :param server_id: A system-assigned unique identifier for a server that you start.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("StopServer")
    def stop_server(self, context: RequestContext, server_id: ServerId) -> None:
        """Changes the state of a file transfer protocol-enabled server from
        ``ONLINE`` to ``OFFLINE``. An ``OFFLINE`` server cannot accept and
        process file transfer jobs. Information tied to your server, such as
        server and user properties, are not affected by stopping your server.

        Stopping the server does not reduce or impact your file transfer
        protocol endpoint billing; you must delete the server to stop being
        billed.

        The state of ``STOPPING`` indicates that the server is in an
        intermediate state, either not fully able to respond, or not fully
        offline. The values of ``STOP_FAILED`` can indicate an error condition.

        No response is returned from this call.

        :param server_id: A system-assigned unique identifier for a server that you stopped.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(self, context: RequestContext, arn: Arn, tags: Tags) -> None:
        """Attaches a key-value pair to a resource, as identified by its Amazon
        Resource Name (ARN). Resources are users, servers, roles, and other
        entities.

        There is no response returned from this call.

        :param arn: An Amazon Resource Name (ARN) for a specific Amazon Web Services
        resource, such as a server, user, or role.
        :param tags: Key-value pairs assigned to ARNs that you can use to group and search
        for resources by type.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("TestIdentityProvider")
    def test_identity_provider(
        self,
        context: RequestContext,
        server_id: ServerId,
        user_name: UserName,
        server_protocol: Protocol = None,
        source_ip: SourceIp = None,
        user_password: UserPassword = None,
    ) -> TestIdentityProviderResponse:
        """If the ``IdentityProviderType`` of a file transfer protocol-enabled
        server is ``AWS_DIRECTORY_SERVICE`` or ``API_Gateway``, tests whether
        your identity provider is set up successfully. We highly recommend that
        you call this operation to test your authentication method as soon as
        you create your server. By doing so, you can troubleshoot issues with
        the identity provider integration to ensure that your users can
        successfully use the service.

        The ``ServerId`` and ``UserName`` parameters are required. The
        ``ServerProtocol``, ``SourceIp``, and ``UserPassword`` are all optional.

        You cannot use ``TestIdentityProvider`` if the ``IdentityProviderType``
        of your server is ``SERVICE_MANAGED``.

        -  If you provide any incorrect values for any parameters, the
           ``Response`` field is empty.

        -  If you provide a server ID for a server that uses service-managed
           users, you get an error:

           ``An error occurred (InvalidRequestException) when calling the TestIdentityProvider operation: s-server-ID not configured for external auth``

        -  If you enter a Server ID for the ``--server-id`` parameter that does
           not identify an actual Transfer server, you receive the following
           error:

           ``An error occurred (ResourceNotFoundException) when calling the TestIdentityProvider operation: Unknown server``

        :param server_id: A system-assigned identifier for a specific server.
        :param user_name: The name of the user account to be tested.
        :param server_protocol: The type of file transfer protocol to be tested.
        :param source_ip: The source IP address of the user account to be tested.
        :param user_password: The password of the user account to be tested.
        :returns: TestIdentityProviderResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(self, context: RequestContext, arn: Arn, tag_keys: TagKeys) -> None:
        """Detaches a key-value pair from a resource, as identified by its Amazon
        Resource Name (ARN). Resources are users, servers, roles, and other
        entities.

        No response is returned from this call.

        :param arn: The value of the resource that will have the tag removed.
        :param tag_keys: TagKeys are key-value pairs assigned to ARNs that can be used to group
        and search for resources by type.
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateAccess")
    def update_access(
        self,
        context: RequestContext,
        server_id: ServerId,
        external_id: ExternalId,
        home_directory: HomeDirectory = None,
        home_directory_type: HomeDirectoryType = None,
        home_directory_mappings: HomeDirectoryMappings = None,
        policy: Policy = None,
        posix_profile: PosixProfile = None,
        role: Role = None,
    ) -> UpdateAccessResponse:
        """Allows you to update parameters for the access specified in the
        ``ServerID`` and ``ExternalID`` parameters.

        :param server_id: A system-assigned unique identifier for a server instance.
        :param external_id: A unique identifier that is required to identify specific groups within
        your directory.
        :param home_directory: The landing directory (folder) for a user when they log in to the server
        using the client.
        :param home_directory_type: The type of landing directory (folder) that you want your users' home
        directory to be when they log in to the server.
        :param home_directory_mappings: Logical directory mappings that specify what Amazon S3 or Amazon EFS
        paths and keys should be visible to your user and how you want to make
        them visible.
        :param policy: A session policy for your user so that you can use the same Identity and
        Access Management (IAM) role across multiple users.
        :param posix_profile: The full POSIX identity, including user ID (``Uid``), group ID
        (``Gid``), and any secondary groups IDs (``SecondaryGids``), that
        controls your users' access to your Amazon EFS file systems.
        :param role: The Amazon Resource Name (ARN) of the Identity and Access Management
        (IAM) role that controls your users' access to your Amazon S3 bucket or
        Amazon EFS file system.
        :returns: UpdateAccessResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateAgreement")
    def update_agreement(
        self,
        context: RequestContext,
        agreement_id: AgreementId,
        server_id: ServerId,
        description: Description = None,
        status: AgreementStatusType = None,
        local_profile_id: ProfileId = None,
        partner_profile_id: ProfileId = None,
        base_directory: HomeDirectory = None,
        access_role: Role = None,
    ) -> UpdateAgreementResponse:
        """Updates some of the parameters for an existing agreement. Provide the
        ``AgreementId`` and the ``ServerId`` for the agreement that you want to
        update, along with the new values for the parameters to update.

        :param agreement_id: A unique identifier for the agreement.
        :param server_id: A system-assigned unique identifier for a server instance.
        :param description: To replace the existing description, provide a short description for the
        agreement.
        :param status: You can update the status for the agreement, either activating an
        inactive agreement or the reverse.
        :param local_profile_id: A unique identifier for the AS2 local profile.
        :param partner_profile_id: A unique identifier for the partner profile.
        :param base_directory: To change the landing directory (folder) for files that are transferred,
        provide the bucket folder that you want to use; for example,
        ``/DOC-EXAMPLE-BUCKET/home/mydirectory``.
        :param access_role: With AS2, you can send files by calling ``StartFileTransfer`` and
        specifying the file paths in the request parameter, ``SendFilePaths``.
        :returns: UpdateAgreementResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateCertificate")
    def update_certificate(
        self,
        context: RequestContext,
        certificate_id: CertificateId,
        active_date: CertDate = None,
        inactive_date: CertDate = None,
        description: Description = None,
    ) -> UpdateCertificateResponse:
        """Updates the active and inactive dates for a certificate.

        :param certificate_id: The identifier of the certificate object that you are updating.
        :param active_date: An optional date that specifies when the certificate becomes active.
        :param inactive_date: An optional date that specifies when the certificate becomes inactive.
        :param description: A short description to help identify the certificate.
        :returns: UpdateCertificateResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateConnector")
    def update_connector(
        self,
        context: RequestContext,
        connector_id: ConnectorId,
        url: Url = None,
        as2_config: As2ConnectorConfig = None,
        access_role: Role = None,
        logging_role: Role = None,
    ) -> UpdateConnectorResponse:
        """Updates some of the parameters for an existing connector. Provide the
        ``ConnectorId`` for the connector that you want to update, along with
        the new values for the parameters to update.

        :param connector_id: The unique identifier for the connector.
        :param url: The URL of the partner's AS2 endpoint.
        :param as2_config: A structure that contains the parameters for a connector object.
        :param access_role: With AS2, you can send files by calling ``StartFileTransfer`` and
        specifying the file paths in the request parameter, ``SendFilePaths``.
        :param logging_role: The Amazon Resource Name (ARN) of the Identity and Access Management
        (IAM) role that allows a connector to turn on CloudWatch logging for
        Amazon S3 events.
        :returns: UpdateConnectorResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateHostKey")
    def update_host_key(
        self,
        context: RequestContext,
        server_id: ServerId,
        host_key_id: HostKeyId,
        description: HostKeyDescription,
    ) -> UpdateHostKeyResponse:
        """Updates the description for the host key that's specified by the
        ``ServerId`` and ``HostKeyId`` parameters.

        :param server_id: The identifier of the server that contains the host key that you are
        updating.
        :param host_key_id: The identifier of the host key that you are updating.
        :param description: An updated description for the host key.
        :returns: UpdateHostKeyResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateProfile")
    def update_profile(
        self, context: RequestContext, profile_id: ProfileId, certificate_ids: CertificateIds = None
    ) -> UpdateProfileResponse:
        """Updates some of the parameters for an existing profile. Provide the
        ``ProfileId`` for the profile that you want to update, along with the
        new values for the parameters to update.

        :param profile_id: The identifier of the profile object that you are updating.
        :param certificate_ids: An array of identifiers for the imported certificates.
        :returns: UpdateProfileResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateServer")
    def update_server(
        self,
        context: RequestContext,
        server_id: ServerId,
        certificate: Certificate = None,
        protocol_details: ProtocolDetails = None,
        endpoint_details: EndpointDetails = None,
        endpoint_type: EndpointType = None,
        host_key: HostKey = None,
        identity_provider_details: IdentityProviderDetails = None,
        logging_role: NullableRole = None,
        post_authentication_login_banner: PostAuthenticationLoginBanner = None,
        pre_authentication_login_banner: PreAuthenticationLoginBanner = None,
        protocols: Protocols = None,
        security_policy_name: SecurityPolicyName = None,
        workflow_details: WorkflowDetails = None,
    ) -> UpdateServerResponse:
        """Updates the file transfer protocol-enabled server's properties after
        that server has been created.

        The ``UpdateServer`` call returns the ``ServerId`` of the server you
        updated.

        :param server_id: A system-assigned unique identifier for a server instance that the user
        account is assigned to.
        :param certificate: The Amazon Resource Name (ARN) of the Amazon Web ServicesCertificate
        Manager (ACM) certificate.
        :param protocol_details: The protocol settings that are configured for your server.
        :param endpoint_details: The virtual private cloud (VPC) endpoint settings that are configured
        for your server.
        :param endpoint_type: The type of endpoint that you want your server to use.
        :param host_key: The RSA, ECDSA, or ED25519 private key to use for your SFTP-enabled
        server.
        :param identity_provider_details: An array containing all of the information required to call a customer's
        authentication API method.
        :param logging_role: The Amazon Resource Name (ARN) of the Identity and Access Management
        (IAM) role that allows a server to turn on Amazon CloudWatch logging for
        Amazon S3 or Amazon EFSevents.
        :param post_authentication_login_banner: Specifies a string to display when users connect to a server.
        :param pre_authentication_login_banner: Specifies a string to display when users connect to a server.
        :param protocols: Specifies the file transfer protocol or protocols over which your file
        transfer protocol client can connect to your server's endpoint.
        :param security_policy_name: Specifies the name of the security policy that is attached to the
        server.
        :param workflow_details: Specifies the workflow ID for the workflow to assign and the execution
        role that's used for executing the workflow.
        :returns: UpdateServerResponse
        :raises AccessDeniedException:
        :raises ServiceUnavailableException:
        :raises ConflictException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateUser")
    def update_user(
        self,
        context: RequestContext,
        server_id: ServerId,
        user_name: UserName,
        home_directory: HomeDirectory = None,
        home_directory_type: HomeDirectoryType = None,
        home_directory_mappings: HomeDirectoryMappings = None,
        policy: Policy = None,
        posix_profile: PosixProfile = None,
        role: Role = None,
    ) -> UpdateUserResponse:
        """Assigns new properties to a user. Parameters you pass modify any or all
        of the following: the home directory, role, and policy for the
        ``UserName`` and ``ServerId`` you specify.

        The response returns the ``ServerId`` and the ``UserName`` for the
        updated user.

        :param server_id: A system-assigned unique identifier for a server instance that the user
        account is assigned to.
        :param user_name: A unique string that identifies a user and is associated with a server
        as specified by the ``ServerId``.
        :param home_directory: The landing directory (folder) for a user when they log in to the server
        using the client.
        :param home_directory_type: The type of landing directory (folder) that you want your users' home
        directory to be when they log in to the server.
        :param home_directory_mappings: Logical directory mappings that specify what Amazon S3 or Amazon EFS
        paths and keys should be visible to your user and how you want to make
        them visible.
        :param policy: A session policy for your user so that you can use the same Identity and
        Access Management (IAM) role across multiple users.
        :param posix_profile: Specifies the full POSIX identity, including user ID (``Uid``), group ID
        (``Gid``), and any secondary groups IDs (``SecondaryGids``), that
        controls your users' access to your Amazon Elastic File Systems (Amazon
        EFS).
        :param role: The Amazon Resource Name (ARN) of the Identity and Access Management
        (IAM) role that controls your users' access to your Amazon S3 bucket or
        Amazon EFS file system.
        :returns: UpdateUserResponse
        :raises ServiceUnavailableException:
        :raises InternalServiceError:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError
