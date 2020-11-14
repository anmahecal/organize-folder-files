import os
import json

class Settings:
    """
    Create, read, edit settings file to manage extensions and folder names

    Attributes
    ----------
        extensions:
            Show the supported extensions

    Methods
    -------
        create_settings_file():
            Creates settings.json file in the folder you are now
        edit_settings_file():
            Edit settings.json file in the folder you are now
        read_settings_file():
            Read settings.json file in the folder you are now (JSON format)
        check_if_settings_file_exists():
            Check if settings is in the current folder

    """

    def __init__(self, path:str, extensions:dict, filename='settings'):
        self.path = path
        self.__extensions = extensions
        self.filename = filename + '.json'


    def create_settings_file(self):
        """Creates settings.json file in the folder you are now."""
        try:
            if self.check_if_settings_file_exists():
                print('Settings file already exists.')
            else:
                with open(self.filename, 'w') as settings:
                    extensions = json.dump(self.__extensions, settings, indent=4)
                print('Settings file created.')
        except Exception as e:
            print(e)


    def edit_settings_file(self):
        """Opens notepad to edit settings file."""
        if self.check_if_settings_file_exists():
            os.system(f'notepad {self.filename}')
            print('Finish edit.')
        else:
            print('File does not exist.')



    def read_settings_file(self) -> dict:
        """Shows in console settings file with supported extensions."""
        try:
            with open(self.filename, 'r') as settings:
                extensions = json.load(settings)
            # self.print_settings_file_in_console(extensions)
            return extensions
        except FileNotFoundError as e:
            return self.__extensions


    @property
    def extensions(self):
        """Prints formatted settings file."""
        formatted = []
        extensions = self.read_settings_file()
        for folder_name, ext in extensions.items():
            ext_str = ', '.join(ext)
            formatted.append(f'-{folder_name}: {ext_str}')
        return formatted

    

    def check_if_settings_file_exists(self) -> bool:
        """Check if settings is in the current folder"""
        if (os.path.exists(os.path.join(self.path, self.filename))):
            return True
        return False