_G='key_hash'
_F='enterprise'
_E='timestamp'
_D='token'
_C='key'
_B=True
_A=False
import base64,json,logging,os,sys,traceback
from typing import Dict,Union
from localstack import config as localstack_config
from localstack.constants import ENV_PRO_ACTIVATED
from localstack.utils.files import load_file
from localstack.utils.http import get_proxies
from localstack.utils.http import safe_requests as requests
from localstack.utils.json import FileMappedDocument
from localstack.utils.strings import md5,str_insert,str_remove,to_bytes,to_str
from localstack.utils.time import now_utc
from localstack_ext import __version__,config
from localstack_ext.bootstrap.auth import AuthClient,AuthToken,get_auth_cache
from localstack_ext.bootstrap.decryption import DecryptionHandler,init_source_decryption
from localstack_ext.config import ROOT_FOLDER
LOG=logging.getLogger(__name__)
ENV_PREPARED={}
MAX_KEY_CACHE_DURATION_SECS=60*60*24
ENV_LOCALSTACK_API_KEY='LOCALSTACK_API_KEY'
AuthCache=Union[FileMappedDocument,Dict]
class KeyActivationError(Exception):0
class CachedKeyError(KeyActivationError):0
class InvalidKeyError(KeyActivationError):0
class InvalidDecryptionKeyError(KeyActivationError):0
def is_enterprise():return read_api_key(raise_if_missing=_A)==_F
def read_api_key(raise_if_missing=_B):
	A=(os.environ.get(ENV_LOCALSTACK_API_KEY)or'').strip()
	if not A and raise_if_missing:raise Exception('Unable to retrieve API key. Please configure $%s in your environment'%ENV_LOCALSTACK_API_KEY)
	return A
def truncate_api_key(api_key):A=api_key;return'"%s..."(%s)'%(A[:3],len(A))
def fetch_key():
	F='py.warnings';A=read_api_key()
	if A=='test':return b'test'
	elif A==_F:LOG.debug('Looking for a cached enterprise key, skipping online activation.');C=load_cached_key(api_key=A,check_timeout=_A);D=base64.b64decode(C);return D
	G=get_proxies()or None;H={'api_key':A,'version':__version__}
	try:
		logging.getLogger(F).setLevel(logging.ERROR);B=requests.post('%s/activate'%config.API_URL,json.dumps(H),verify=_A,proxies=G)
		if B.status_code>=400:
			E=B.content;I=B.headers.get('Content-Type')
			if B.status_code==403:J=json.loads(to_str(E))['message'];raise InvalidKeyError('Activation key %s is invalid or expired! Reason: %s'%(truncate_api_key(A),J))
			raise KeyActivationError('Received error activating key (code %s): ctype "%s" - %s'%(B.status_code,I,E))
		C=json.loads(to_str(B.content))[_C];cache_key_locally(A,C)
	except InvalidKeyError:raise
	except Exception as K:
		if log_license_issues():A=str(api_key_configured()or'');LOG.warning('Error activating API key %s: %s %s'%(truncate_api_key(A),K,traceback.format_exc()));LOG.warning('Looking for cached key as fallback...')
		C=load_cached_key(A)
	finally:logging.getLogger(F).setLevel(logging.WARNING)
	D=base64.b64decode(C);return D
def get_key_cache():A=localstack_config.dirs.cache if not is_enterprise()else localstack_config.dirs.static_libs;return FileMappedDocument(os.path.join(A,'key.json'),mode=384)
def cache_key_locally(api_key,key_b64):
	A=key_b64;B=str(int(now_utc()));C=to_str(base64.b64decode(A))
	for D in range(len(B)):C=str_insert(C,D*2,B[D])
	A=to_str(base64.b64encode(to_bytes(C)));E=get_key_cache();E.update({_E:int(B),_G:md5(api_key),_C:A});E.save()
def load_cached_key(api_key,check_timeout=_B):
	A=get_key_cache()
	if not A.get(_C):raise CachedKeyError('Could not find cached key')
	if A.get(_G)!=md5(api_key):raise CachedKeyError('Cached key was created for a different API key')
	E=now_utc()
	if check_timeout and E-A[_E]>MAX_KEY_CACHE_DURATION_SECS:raise CachedKeyError('Cached key expired')
	D=str(A[_E]);B=to_str(base64.b64decode(A[_C]))
	for C in range(len(D)):assert B[C]==D[C];B=str_remove(B,C)
	F=to_str(base64.b64encode(to_bytes(B)));return F
def enable_file_decryption(key):
	A=DecryptionHandler(key)
	try:
		B=f"{ROOT_FOLDER}/localstack_ext/utils/common.py.enc";C=load_file(B,mode='rb');D=A.decrypt(C)
		if'import'not in to_str(D):raise ValueError('Decryption resulted in invalid python file!')
	except Exception:raise InvalidDecryptionKeyError('Error while trying to validate decryption key!')
	init_source_decryption(A)
def check_require_pro():
	if config.REQUIRE_PRO:LOG.error('Unable to activate API key, but $REQUIRE_PRO is configured - quitting.');sys.exit(1)
def prepare_environment():
	D='finalized'
	class A:
		def __exit__(A,*B,**C):ENV_PREPARED[D]=_B
		def __enter__(A,*B,**C):0
	if ENV_PREPARED.get(D):return A()
	try:from localstack_ext.services.amplify import provider;os.environ[ENV_PRO_ACTIVATED]='1';return A()
	except Exception:pass
	try:
		B=fetch_key()
		if not B:raise Exception('Unable to fetch and validate API key from environment')
		if to_str(B)!='test':enable_file_decryption(B);LOG.info('Successfully activated API key')
		else:LOG.info('Using test API key')
		os.environ[ENV_PRO_ACTIVATED]='1'
	except KeyActivationError as C:
		if log_license_issues():
			if LOG.isEnabledFor(level=logging.DEBUG):LOG.exception('exception while activating key')
			else:LOG.warning('error while activating key: %s',C)
		check_require_pro()
	except Exception as C:
		if log_license_issues():LOG.warning('Unable to activate API key: %s %s'%(C,traceback.format_exc()))
		check_require_pro()
	return A()
def log_license_issues():return api_key_configured()and localstack_config.is_env_not_false('LOG_LICENSE_ISSUES')
def api_key_configured():return read_api_key(raise_if_missing=_A)
def is_logged_in():return _B if get_auth_cache().get(_D)else _A
def get_auth_headers(auth_cache=None):
	B=auth_cache;B=B or get_auth_cache();C=B.get(_D);A=C
	if isinstance(A,dict):
		H=AuthClient();D=AuthToken(C.get(_D),metadata=C);D=H.refresh_token(D);E=D.to_dict()
		if C!=E:C.update(E);B[_D]=C;B.save()
		A=D.token
	if A:
		I=B.get('provider')or'internal';F=f"{I} "
		if not A.startswith(F)and' 'not in A:A=f"{F}{A}"
		return{'authorization':A}
	G=read_api_key(raise_if_missing=_A)
	if G:return{'ls-api-key':G,'ls-version':__version__}
	raise Exception('Please log in first')