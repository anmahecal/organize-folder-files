import os
from groot.Settings import Settings

class Mover():
    """
    A Class that allows move files by their extension to new folders
    
    Methods
    -------
        move_file():
            Move file from source directory to destination directory
    """
    
    extensions = {
        'PDF': ['.pdf'],
        'Docs': ['.docx', '.xlsx', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png'],
        'Installers': ['.exe', '.msi']
    }

    def __init__(self):
        self.src_path = os.getcwd()
        self.settings = Settings(self.src_path, self.extensions)
        self.extensions = self.settings.read_settings_file()

        
    def move_file(self, filename:str):
        """Move file from source directory to destination directory"""

        self._split_ext(filename)

        # Check current filename extension in supported extensions
        for folder_name, extensions in self.extensions.items():
            if (self.file_ext in extensions):
                destination_path = os.path.join(self.src_path, folder_name)        
                if (os.path.isdir(destination_path)):
                    print(f'Moving -> {filename} to {destination_path}')
                else:
                    os.mkdir(destination_path)
                    print(f'Creating directory {destination_path}')
                    print(f'Moving -> {filename} to {destination_path}')
                os.rename(self._get_current_file_path(), self._set_next_file_path(folder_name))

            # TODO: Files that don't match any of the supported extensions should stay
            # in source folder or create a folder for all of them?


    def _split_ext(self, filename:str):
        """Split the name of the file and the extension to separate attributes"""

        file_name, file_ext = os.path.splitext(filename)
        self.filename = filename
        self.file_name = file_name
        self.file_ext = file_ext


    def _get_current_file_path(self) -> str:
        """Return the full current path to the file"""

        return os.path.join(self.src_path, self.filename)


    def _set_next_file_path(self, folder_name:str) -> str:
        """Return the destination path to the file"""
        
        return os.path.join(self.src_path, folder_name, self.filename)


    def __repr__(self):
        return f'Mover({self.filename})'
