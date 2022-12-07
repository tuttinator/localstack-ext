from localstack_ext import __version__

# version of localstack-ext
# TODO deprecated - use localstack-ext.__version__ instead
VERSION = __version__

# default expiry seconds for Cognito access tokens (1h by default in AWS)
TOKEN_EXPIRY_SECONDS = 60 * 60

# name of Docker registry for Lambda images
DEFAULT_LAMBDA_DOCKER_REGISTRY = "localstack/lambda"

# request path for local pod management API
API_PATH_PODS = "/_pods"

# name of S3 bucket containing assets that are lazily downloaded
ASSETS_S3_BUCKET = "localstack-assets"

# Root directory for pickled (persisted) states
API_STATES_DIR = "api_states"

# Filename for pickled (persisted) Moto BackendDict
MOTO_BACKEND_STATE_FILE = "backend.state"

# Filename for pickled (persisted) provider AccountRegionBundle
STORE_STATE_FILE = "store.state"

# active MQ download URL
ACTIVE_MQ_URL = "https://dlcdn.apache.org/activemq/5.16.5/apache-activemq-5.16.5-bin.tar.gz"

UPDATE_HTTP_METHODS = ["POST", "PUT", "DELETE", "PATCH"]
