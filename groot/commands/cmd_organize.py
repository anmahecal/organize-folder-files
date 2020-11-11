import os, click
from groot import mover


@click.command()
def cli():
	"""Entry point to organize files into folders"""

	if mover.settings.check_if_settings_file_exists():
		click.secho('Running...')
		for filename in os.listdir():
			mover.move_file(filename)
		click.secho('Done!', fg='green')
		return True
	else:
		click.secho('>> There isn\'t a groot settings file in this folder. ', fg='yellow')
		click.secho('>> It allows you to modify folder names and supported extensions.', fg='yellow')
		create_settings = input('>> Do you want to create a settings file? (If not, it will apply default settings) [y/n]: ')
		if create_settings == 'y':
			mover.settings.create_settings_file()
			mover.settings.edit_settings_file()
			click.secho('>> Please re run groot organize.')
		else:
			for filename in os.listdir():
				mover.move_file(filename)
			return True
