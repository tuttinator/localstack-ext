import os,click
from localstack import config
from .  import repository
@click.group('extensions')
def cli():from localstack.utils.bootstrap import setup_logging as A;A()
@cli.command('debug')
def debug():
	B='not initialized';click.echo('Directories');click.echo('===========')
	for (C,D) in config.dirs.__dict__.items():click.echo(f"{C:13} {D}")
	click.echo();click.echo('Extensions venv');click.echo('===============');A=repository.LOCALSTACK_VENV;click.echo(f"localstack venv: {A.venv_dir}");click.echo(f"  site-packages: {A.site_dir if A.exists else B}");A=repository.get_extensions_venv();click.echo(f"extensions venv: {A.venv_dir}");click.echo(f"  site-packages: {A.site_dir if A.exists else B}");click.echo();click.echo('pip list');click.echo('========');os.system(f"bash -c '. {A.venv_dir}/bin/activate && pip list'")
@cli.command('init')
def init():from .  import repository as A;A.init()
if __name__=='__main__':cli()