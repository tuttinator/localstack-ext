_A='__dict__'
import logging,os
from collections import defaultdict
from typing import Any,Callable,List,OrderedDict,Set,Tuple
from localstack.utils.files import rm_rf
from localstack.utils.objects import ObjectIdHashComparator
KINESIS_DIR='kinesis'
DYNAMODB_DIR='dynamodb'
POD_KEEP='.podkeep'
LOG=logging.getLogger(__name__)
def traverse_object(obj,handler,safe=True,visited=None):
	D=safe;C=handler;B=visited;A=obj
	try:
		if isinstance(A,dict)and type(A)not in(dict,defaultdict):traverse_object(A.__dict__,handler=C,safe=D,visited=B)
		E=get_object_dict(A)
		if E is None:return
		F,B=check_already_visited(A,B)
		if F:return
		for G in E.values():traverse_object(G,handler=C,safe=D,visited=B)
		C(A)
	except Exception as H:
		if not D:raise
		LOG.warning('Unable to add missing attributes to persistence state object %s: %s',A,H)
def check_already_visited(obj,visited):
	A=visited
	if hasattr(obj,_A):
		A=A or set();B=ObjectIdHashComparator(obj)
		if B in A:return True,A
		A.add(B)
	return False,A
def check_already_visited_obj_id(obj,visited):A=visited;A=A or set();B=id(obj);C=B in A;A.add(B);return C,A
def get_object_dict(obj):
	A=obj
	if isinstance(A,dict):return A
	B=getattr(A,_A,None);return B
def is_composite_type(obj):return isinstance(obj,(dict,OrderedDict,list,set))or hasattr(obj,_A)
def api_states_traverse(api_states_path,side_effect,mutables):
	B=side_effect
	for (A,K,E) in os.walk(api_states_path):
		for C in E:
			try:F=os.path.normpath(A).split(os.sep);G,H,I=F[-3:];B(dir_name=A,fname=C,region=I,service_name=H,account_id=G,mutables=mutables)
			except Exception as J:
				D=f"Failed to apply {B.__name__} for {C} in dir {A}: {J}";LOG.warning(D)
				if LOG.isEnabledFor(logging.DEBUG):LOG.exception(D)
				continue
def cleanse_keep_files(file_path):
	for (B,D,C) in os.walk(file_path):
		for A in C:
			if A==POD_KEEP:rm_rf(os.path.join(B,A))