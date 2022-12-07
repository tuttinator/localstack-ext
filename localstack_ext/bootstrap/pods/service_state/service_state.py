from __future__ import annotations
import hashlib,logging
from typing import Dict,List
from localstack_ext.bootstrap.pods.service_state.service_state_types import AssetByNameType,AssetNameType,AssetValueType,BackendState,ServiceKey,ServiceNameType
LOG=logging.getLogger(__name__)
class ServiceState:
	def __init__(A):A.state={};A.assets={}
	def put_service_state(A,service_state):
		B=service_state
		for C in B.state.values():A.put_backend(C)
		for (D,E) in B.assets.items():A.put_assets(D,E)
	def put_backend(B,backend_state):
		A=backend_state
		if A.key not in B.state:B.state[A.key]=A;return
		C=B.state[A.key];C.backends.update(A.backends)
	def put_asset(A,service_name,asset_name,asset_value):B=service_name;C=A.assets.get(B,{});C[asset_name]=asset_value;A.assets[B]=C
	def put_assets(A,service_name,assets_by_name):A.assets[service_name]=assets_by_name
	def is_empty(A):return len(A.state)==0 and len(A.assets)==0
	def get_services(C):
		A=set()
		for B in C.state:A.add(B.service)
		for B in C.assets:A.add(B)
		return list(A)
	def compute_hash_on_state(A):
		B=hashlib.sha1();F=sorted(A.state.keys())
		for G in F:
			C=A.state.get(G);H=sorted(C.backends.keys())
			for D in H:
				E=C.backends.get(D)
				if isinstance(E,bytes):B.update(E)
				else:LOG.debug(f"{D} is not serialized")
		return B.hexdigest()
	def __str__(A):return f"Backends: {A.state.__str__()}\nAssets: {A.assets.__str__()}"