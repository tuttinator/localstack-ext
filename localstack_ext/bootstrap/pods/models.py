_B=False
_A=None
import copy,json,logging,sys
from abc import ABC
from datetime import datetime
from enum import Enum
from typing import Any,Dict,List,Optional,Set,Union
if sys.version_info>=(3,8):from typing import Final
else:from typing_extensions import Final
import yaml
from localstack_ext.bootstrap.pods.constants import NIL_PTR
from localstack_ext.bootstrap.state_utils import DYNAMODB_DIR,KINESIS_DIR
from localstack_ext.constants import API_STATES_DIR
LOG=logging.getLogger(__name__)
class SerializableObject(ABC):
	def to_dict(A):return copy.deepcopy(A.__dict__)
	@classmethod
	def from_dict(B,obj):A=B();A.__dict__.update(obj);return A
	def to_yaml(A):return yaml.dump(A.to_dict())
	def to_json(A):return json.dumps(A.to_dict())
	def __str__(A):return A.to_yaml()
	def __repr__(A):return A.to_json()
class PodObject(SerializableObject):
	def __init__(A,hash_ref):A.hash_ref=hash_ref;A.obj_type=A.__class__.__name__
class Serialization(Enum):MAIN=API_STATES_DIR;DDB=DYNAMODB_DIR;KINESIS=KINESIS_DIR;serializer_root_lookup={str(MAIN):API_STATES_DIR,str(DDB):DYNAMODB_DIR,str(KINESIS):KINESIS_DIR}
class StateFileRef(PodObject):
	def __init__(A,hash_ref=_A,rel_path=_A,file_name=_A,size=_A,service=_A,region=_A,account_id=_A,serialization=_A):super(StateFileRef,A).__init__(hash_ref);A.rel_path=rel_path;A.file_name=file_name;A.size=size;A.service=service;A.region=region;A.account_id=account_id;A.serialization=serialization
	def __eq__(A,other):
		B=other
		if not B:return _B
		if not isinstance(B,StateFileRef):return _B
		return A.hash_ref==B.hash_ref and A.account_id==B.account_id and A.region==B.region and A.service==A.service and A.file_name==B.file_name and A.size==B.size
	def __hash__(A):return hash((A.hash_ref,A.account_id,A.region,A.service,A.file_name,A.size))
	def congruent(A,other):
		B=other
		if not B:return _B
		if not isinstance(B,StateFileRef):return _B
		return A.region==B.region and A.account_id==A.account_id and A.service==B.service and A.file_name==B.file_name and A.rel_path==B.rel_path
	def any_congruence(A,others):
		for B in others:
			if A.congruent(B):return True
		return _B
	def to_dict(C):B='serialization';A=super().to_dict();A[B]=A[B].name;return A
	@classmethod
	def from_dict(B,obj):A=super().from_dict(obj);A.serialization=Serialization[A.serialization];return A
class PodNode(PodObject):
	def __init__(A,hash_ref,state_files,parent_ptr):super(PodNode,A).__init__(hash_ref);A.state_files=state_files;A.parent_ptr=parent_ptr
	def state_files_info(A):return '\n'.join(list(map(lambda state_file:str(state_file),A.state_files)))
	def to_dict(C):
		B='state_files';A=super().to_dict()
		if isinstance(A.get(B),set):A[B]=list((C.to_dict()for C in A[B]))
		return A
	@classmethod
	def from_dict(B,obj):A=super().from_dict(obj);A.state_files=set((StateFileRef.from_dict(B)for B in A.state_files or[]));return A
class Commit(SerializableObject):
	tail_ptr:str;head_ptr:str;message:str;timestamp:str
	def __init__(A,tail_ptr=_A,head_ptr=_A,message=_A,timestamp=_A):A.tail_ptr=tail_ptr;A.head_ptr=head_ptr;A.message=message;A.timestamp=timestamp or str(datetime.now().timestamp())
	def get_summary(A):return f"from {A.tail_ptr}, to {A.head_ptr}, message: {A.message}, time: {A.timestamp}"
class Revision(PodNode):
	DEFAULT_INITIAL_REVISION_NUMBER=1
	def __init__(A,hash_ref=_A,state_files=_A,parent_ptr=_A,creator=_A,rid=_A,revision_number=_A,assoc_commit=_A,metamodel_file=_A):super(Revision,A).__init__(hash_ref,state_files,parent_ptr);A.creator=creator;A.rid=rid;A.revision_number=revision_number or A.DEFAULT_INITIAL_REVISION_NUMBER;A.assoc_commit=assoc_commit;A.metamodel_file=metamodel_file or''
	def to_dict(A):
		B=super().to_dict()
		if A.assoc_commit:B['assoc_commit']=A.assoc_commit.to_dict()
		return B
	@classmethod
	def from_dict(B,obj):
		A=super().from_dict(obj)
		if A.assoc_commit:A.assoc_commit=Commit.from_dict(A.assoc_commit)
		return A
class Version(PodNode):
	DEFAULT_INITIAL_VERSION_NUMBER=1;creator:str;comment:str;revisions:List[Revision];outgoing_revision_ptrs:Set[str];incoming_revision_ptr:str;version_number:int
	def __init__(A,hash_ref=_A,state_files=_A,parent_ptr=_A,creator=_A,comment=_A,outgoing_revision_ptrs=_A,incoming_revision_ptr=_A,version_number=_A):super(Version,A).__init__(hash_ref,state_files,parent_ptr);A.creator=creator;A.comment=comment;A.outgoing_revision_ptrs=outgoing_revision_ptrs;A.incoming_revision_ptr=incoming_revision_ptr;A.version_number=version_number;A.revisions=[]
	def get_latest_revision(A,with_commit=_B):
		B=A.revisions_with_commit if with_commit else A.revisions
		if not B:raise Exception('No revisions present in cloud pod version')
		return B[-1]
	@property
	def revisions_with_commit(self):return[A for A in self.revisions if A.assoc_commit]
	@property
	def active_revision_ptr(self):
		A=self.get_latest_revision()
		if not A:return NIL_PTR
		return A.hash_ref
	def get_revision(B,key):
		for A in B.revisions:
			if key in(A.hash_ref,A.revision_number):return A
	def update_revision_key(A,old_key,new_key):
		B=old_key
		if B in A.outgoing_revision_ptrs:A.outgoing_revision_ptrs.remove(B)
		A.outgoing_revision_ptrs.add(new_key)
	def to_dict(D):C='revisions';B='outgoing_revision_ptrs';A=super().to_dict();A[B]=list(A[B]or[]);A[C]=list((B.to_dict()for B in A[C]or[]));return A
	@classmethod
	def from_dict(B,obj):A=super().from_dict(obj);A.outgoing_revision_ptrs=set(A.outgoing_revision_ptrs or[]);A.revisions=[Revision.from_dict(B)for B in A.revisions];return A