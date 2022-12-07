_G='uninstall'
_F='install'
_E='bin/python'
_D='extensions-dev.json'
_C='host_path'
_B=True
_A='extensions'
import os
from typing import List
import click
from click import ClickException
from localstack.utils.analytics.cli import publish_invocation
@click.group(name=_A,help='Manage LocalStack extensions (beta)')
def extensions():0
@extensions.command('init')
@publish_invocation
def cmd_extensions_init():_run_localstack_container_command(['.venv/bin/python','-m','localstack_ext.bootstrap.extensions','init'])
def assert_venv_initialized():
	from localstack import config as A;from localstack_ext.bootstrap.extensions import repository as B;C=os.path.join(A.VOLUME_DIR,'lib',B.VENV_DIRECTORY)
	if not os.path.exists(C):raise ClickException('extensions dir not initialized, please run `localstack extensions init` first or check if `LOCALSTACK_VOLUME_DIR` is set correctly')
@extensions.command(_F)
@click.argument('name',required=_B)
@publish_invocation
def cmd_extensions_install(name):from localstack import config as A;from localstack_ext.bootstrap.extensions import repository as B;assert_venv_initialized();C=os.path.join(A.Directories.for_container().var_libs,B.VENV_DIRECTORY,_E);_run_localstack_container_command([C,'-m','pip',_F,name])
@extensions.command(_G,help='Remove a LocalStack extension')
@click.argument('name',required=_B)
@publish_invocation
def cmd_extensions_uninstall(name):from localstack import config as A;from localstack_ext.bootstrap.extensions import repository as B;assert_venv_initialized();C=os.path.join(A.Directories.for_container().var_libs,B.VENV_DIRECTORY,_E);_run_localstack_container_command([C,'-m','pip',_G,'-y',name])
@extensions.group('dev',help='Developer tools for developing Localstack extensions')
def dev():0
@dev.command('new')
@publish_invocation
def cmd_dev_new():
	try:from cookiecutter.main import cookiecutter as A
	except ImportError:B='this command requires the cookiecutter CLI, please run:\npip install cookiecutter';raise ClickException(B)
	A('https://github.com/localstack/localstack-extensions',directory='template')
@dev.command('enable')
@click.argument('path',type=click.Path(exists=_B))
@publish_invocation
def cmd_dev_enable(path):
	B=path;from localstack import config as A;from localstack.utils.json import FileMappedDocument as C;B=os.path.abspath(B);A=C(os.path.join(A.CONFIG_DIR,_D))
	if _A not in A:A[_A]=[]
	for D in A[_A]:
		if D[_C]==B:click.echo(f"{B} already enabled");return
	A[_A].append({_C:B});A.save();click.echo(f"{B} enabled")
@dev.command('disable')
@click.argument('path',type=click.Path(exists=False))
@publish_invocation
def cmd_dev_disable(path):
	B=path;from localstack import config as A;from localstack.utils.json import FileMappedDocument as C;B=os.path.abspath(B);A=C(os.path.join(A.CONFIG_DIR,_D))
	if _A not in A:A[_A]=[]
	D=len(A[_A]);A[_A]=[C for C in A[_A]if C[_C]!=B];E=len(A[_A])
	if D==E:click.echo(f"{B} not enabled");return
	A.save();click.echo(f"{B} disabled")
@dev.command('list')
def cmd_dev_list():
	from localstack import config as A;from localstack.utils.json import FileMappedDocument as B;A=B(os.path.join(A.CONFIG_DIR,_D))
	if _A not in A:return
	for C in A[_A]:click.echo(C[_C])
def _run_localstack_container_command(cmd):
	from localstack import config as D,constants as B;from localstack.utils import docker_utils as A;C=A.DOCKER_CLIENT.create_container(image_name=B.DOCKER_IMAGE_NAME,entrypoint='',remove=_B,command=cmd,mount_volumes=[(D.VOLUME_DIR,B.DEFAULT_VOLUME_DIR)]);A.DOCKER_CLIENT.start_container(C);E=A.DOCKER_CLIENT.stream_container_logs(C)
	for F in E:print(F.decode('utf-8'),end='')