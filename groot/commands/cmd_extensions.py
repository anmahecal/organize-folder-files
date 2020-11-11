import click
from groot import mover


@click.command()
@click.option('-c', '--create', is_flag=True, help='Create settings file, to modify extensions and folders.')
@click.option('-e', '--edit', is_flag=True, help='Edit the supported file extensions and folder names.')
def cli(create, edit):
	"""
	Create, read, edit extensions settings file.

	Add, remove, change folder names.
	"""
	
	if create:
		mover.settings.create_settings_file()

	if edit:
		mover.settings.edit_settings_file()

	for ext in mover.settings.extensions:
		click.secho(ext)
