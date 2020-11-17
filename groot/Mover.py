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

        if os.path.isdir(os.path.join(self.src_path, filename)):
            return None

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
                try:
                    os.rename(self._get_current_file_path(), self._set_next_file_path(folder_name))
                except FileExistsError as e:
                    new_filename = self._add_consecutive_to_filename(filename)

                    # Change the filename inside current folder
                    os.rename(self._get_current_file_path(), self._get_current_file_path(new_filename))

                    # Try to move the file recursively
                    self.move_file(new_filename)
                

            # TODO: Files that don't match any of the supported extensions should stay
            # in source folder or create a folder for all of them?


    def _add_consecutive_to_filename(self, filename: str) -> str:
        """Concatenate a number at the end of the filename if filename already exists in destination"""

        import re

        file, ext = os.path.splitext(filename)
        pattern = '\(\d+\)' # (1), (33)
        # TODO: This pattern has to be at the end of the file name
        is_pattern = re.findall(pattern, file)
        if is_pattern:
            new_filename = self._increment_consecutive_number(file, is_pattern[0]) + ext
        else:
            new_filename = file + '(1)' + ext
        return new_filename


    @staticmethod
    def _increment_consecutive_number(file: str, pattern: str) -> str:
        """Search for consecutive number in parenthesis, add one and return the new filename"""
        
        print(f'file: {file}, patt: {pattern}')
        cons_number = int(pattern.lstrip('(').rstrip(')'))
        new_cons_number = cons_number + 1
        new_cons_str = f'({new_cons_number})'
        return file.replace(pattern, new_cons_str)


    def _split_ext(self, filename:str):
        """Split the name of the file and the extension to separate attributes"""

        file_name, file_ext = os.path.splitext(filename)
        self.filename = filename
        self.file_name = file_name
        self.file_ext = file_ext


    def _get_current_file_path(self, filename=None) -> str:
        """Return the full current path to the file"""

        if not filename:
            filename = self.filename


        return os.path.join(self.src_path, filename)


    def _set_next_file_path(self, folder_name:str, filename=None) -> str:
        """Return the destination path to the file"""
        
        if not filename:
            filename = self.filename

        return os.path.join(self.src_path, folder_name, filename)


    def __repr__(self):
        return f'Mover({self.filename})'
