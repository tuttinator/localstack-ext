_F='url-or-name'
_E="[red]Error:[/red] Login to save to the Cloud Pod's platform"
_D='name'
_C=True
_B=False
_A=None
import argparse,sys,traceback
from typing import Dict,List,Optional,Set
from urllib.parse import urlparse
import click,requests
from click import Context
from localstack import config
from localstack.cli import console
from localstack.utils.analytics.cli import publish_invocation
from localstack_ext.bootstrap import licensing
from localstack_ext.bootstrap.pods.api_types import DEFAULT_MERGE_STRATEGY,MergeStrategy
from localstack_ext.bootstrap.pods.utils.common import is_comma_delimited_list
from localstack_ext.cli.cli_help import delete_help,list_help,save_help,versions_help
from localstack_ext.cli.click_utils import print_table
from localstack_ext.cli.cloud_pods_pretty import MergeStrategyPretty
from localstack_ext.cli.tree_view import TreeRenderer
class PodsCmdHandler(click.Group):
	def invoke(B,ctx):
		A=ctx
		try:
			D=B._is_restricted_cmd(A)
			if D and not licensing.is_logged_in():console.print('[red]Error:[/red] not logged in, please log in first');return sys.exit(1)
			return super(PodsCmdHandler,B).invoke(A)
		except Exception as C:
			if isinstance(C,click.exceptions.Exit):raise
			click.echo(f"Error: {C}")
			if A.parent and A.parent.params.get('debug'):click.echo(traceback.format_exc())
			A.exit(1)
	def _is_restricted_cmd(B,ctx):
		if ctx.protected_args!=['pull']:return _C
		A=argparse.ArgumentParser();A.add_argument('--name');C=dict(A.parse_known_args(ctx.args)[0].__dict__);D=C.get(_D)or'';return not B._is_public_community_pod(D)
	def _is_public_community_pod(A,pod_name):return'/'in pod_name
def _cloud_pod_initialized(pod_name):
	A=pod_name;from localstack_ext.bootstrap import pods_client as B
	if not B.is_initialized(pod_name=A):console.print(f"[red]Error:[/red] Could not find local CloudPods instance '{A}'");return _B
	return _C
def _is_host_reachable():
	A=_B
	try:B=requests.get(config.get_edge_url());return _C
	except requests.ConnectionError:console.print('[red]Error:[/red] Destination host unreachable.')
	return A
@click.group(name='pod',help='Manage the state of your instance via Cloud Pods.',cls=PodsCmdHandler,context_settings=dict(max_content_width=120))
def pod():0
@pod.command(name='delete',short_help='Delete a Cloud Pod',help=delete_help)
@click.argument(_D)
@publish_invocation
def cmd_pod_delete(name):
	A=name;from localstack_ext.bootstrap import pods_client as B;C=B.delete_pod(pod_name=A)
	if C:console.print(f"Successfully deleted {A}")
	else:console.print(f"[yellow]Could not delete Cloud Pod {A}[/yellow]")
@pod.command(name='save',short_help='Create a new Cloud Pod',help=save_help)
@click.argument(_F)
@click.option('-m','--message',help="Add a comment describing this Cloud Pod's version")
@click.option('-s','--services',help='Comma-delimited list of services to push in the Cloud Pod (all by default)')
@click.option('--visibility',help='Set the visibility of the Cloud Pod [`public` or `private`]. Does not create a new version')
@publish_invocation
def cmd_pod_save(url_or_name=_A,url=_A,services=_A,message=_A,visibility=_A):
	G='public';D=visibility;C=services;A=url_or_name;from localstack_ext.bootstrap import pods_client as E
	if not _is_host_reachable():return
	H=urlparse(A).scheme=='file'
	if url or H:
		F=url or A;B=E.export_pod(target=F)
		if B:console.print(f"Cloud Pods {F} successfully exported")
		return _C
	if not licensing.is_logged_in():console.print(_E);return
	if C and not is_comma_delimited_list(C):console.print('[red]Error:[/red] Input the services as a comma-delimited list');return _B
	if D:
		if D not in[G,'private']:console.print('[red]Error:[/red] Possible values for visibility are `public` and `private`');return
		B=E.set_public(pod_name=A,public=D==G)
		if B:console.print(f"Cloud Pod {A} made {D}")
		else:console.print('[red]Error:[/red] Visibility change failed')
		return
	I=[A.strip()for A in C.split(',')]if C else _A;B=E.push_state(pod_name=A,comment=message,services=I,local=_B)
	if B:console.print(f"Cloud Pod {A} successfully created")
	else:console.print(f"[red]Error:[/red] Failed to create Cloud Pod {A}")
@pod.command(name='load',short_help='Load the state of a Cloud Pod into the application runtime')
@click.argument(_F)
@click.option('-s','--strategy',help=MergeStrategyPretty.help_message(),default=MergeStrategyPretty.from_merge_strategy(DEFAULT_MERGE_STRATEGY))
@publish_invocation
def cmd_pod_load(url_or_name=_A,url=_A,strategy=MergeStrategyPretty.from_merge_strategy(DEFAULT_MERGE_STRATEGY)):
	B=url;A=url_or_name;from localstack_ext.bootstrap import pods_client as E
	if not _is_host_reachable():return
	D=MergeStrategyPretty.to_merge_strategy(strategy)
	if D is _A:console.print('[red]No such inject strategy[/red]');return
	def F(_result):
		if _result:console.print(f"Cloud Pod {A or B} successfully loaded")
		else:console.print(f"[red]Error:[/red] Failed to load Cloud Pod {A or B}")
	G=urlparse(A).scheme in['file','http','https','git']
	if B or G:H=B or A;C=E.import_pod(source=H,merge_strategy=D);F(C);return C
	if not licensing.is_logged_in():console.print(_E);return
	C=E.pull_state(pod_name=A,merge_strategy=D)
	if C:console.print(f"Cloud Pod {A} successfully loaded")
	else:console.print(f"[red]Error:[/red] Failed to load Cloud Pod {A}")
@pod.command(name='list',short_help='List all available Cloud Pods',help=list_help)
@click.option('--public','-p',help='List all the available public Cloud Pods',is_flag=_C,default=_B)
@publish_invocation
def cmd_pod_list_pods(public=_B):
	from localstack_ext.bootstrap import pods_client as B
	if public:C=B.list_public_pods();print_table(column_headers=['Cloud Pod'],columns=[C]);return
	A=B.list_pods()
	if not A:console.print('[yellow]No pods available[/yellow]')
	print_table(column_headers=['local/remote','Name'],columns=[['local+remote'if len(B)>1 else list(B)[0]for B in list(A.values())],list(A.keys())])
@pod.command(name='versions',short_help='List all available versions for a Cloud Pod',help=versions_help)
@click.argument(_D)
@publish_invocation
def cmd_pod_versions(name):
	from localstack_ext.bootstrap import pods_client as A
	if not _cloud_pod_initialized(pod_name=name):return
	B=A.get_version_summaries(pod_name=name);C='\n'.join(B);console.print(C)
@pod.command(name='inspect',help='Inspect the contents of a Cloud Pod')
@click.argument(_D)
@click.option('-f','--format',help='Format (curses, rich, json).',default='curses')
@publish_invocation
def cmd_pod_inspect(name,format):
	from localstack_ext.bootstrap import pods_client as B
	if not _cloud_pod_initialized(pod_name=name):return
	A=B.get_version_metamodel(pod_name=name,version=-1);C=['cloudwatch']
	for (D,E) in A.items():A[D]={A:B for(A,B)in E.items()if A not in C}
	TreeRenderer.get(format).render_tree(A)
def get_pods_community_commands():B='url';A=click.Group(name='pod',help='Manage the state of your instance via Cloud Pods',context_settings=dict(max_content_width=120));[A.add_command(B)for B in community_pods_commands];cmd_pod_save.params=list(filter(lambda x:isinstance(x,click.Argument),cmd_pod_save.params));cmd_pod_save.params[0].name=B;cmd_pod_save.short_help='Create a new Cloud Pod and saves it to disk';cmd_pod_save.help='\n    Save the current state of the LocalStack container in a Cloud Pod.\n    To export on a local path run the following command:\n\n    localstack pod save file://<path_on_disk>/<pod_name>\n\n    The output will be a <pod_name> zip file in the specified directory. This Cloud Pod instance can be restored at any\n    point in time with the load command.\n    ';cmd_pod_load.params=list(filter(lambda x:isinstance(x,click.Argument),cmd_pod_load.params));cmd_pod_load.params[0].name=B;cmd_pod_load.short_help='Load the state of a Cloud Pod into the application runtime from a given URL';cmd_pod_load.help="\n    Load a Cloud Pod into the running LocalStack container. Users can import Pods different sources, i.e., local\n    storage or any provided HTTP URL.\n\n    Use the URL argument to specify the URL where the Cloud Pod's content is stored.\n\n    \x08\n    We support the following protocols:\n    localstack pod load file://<path_to_disk>\n    localstack pod load https://<some_url>\n    localstack pod load git://<user>/<repo>/<local_repo_path>\n\n    The latter option is merely a shortcut for:\n    \x08\n    localstack pod load https://raw.githubusercontent.com/<user>/<repo>/<branch>/<path>\n\n    Importing via a provided a given URL is available to all the users.\n    ";return A
community_pods_commands=[cmd_pod_save,cmd_pod_load]