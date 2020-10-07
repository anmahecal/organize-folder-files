import os
from abc import ABCMeta, abstractmethod

class Move(metaclass=ABCMeta):
    ''' Abstract class. Creator '''
    @abstractmethod
    def create_mover():
        pass

class MoveFactory(Move):
    ''' Concrete creator '''
    folder_name = 'default/'

    def __init__(self, filename):
        self.filename = filename
        self._split_ext()
        self.src = os.getcwd()
        self.destination = os.getcwd() + '/' + self.folder_name

    def create_mover(self):
        if (self.file_ext == '.pdf'):
            return MovePdf(self.filename)
        elif(self.file_ext in ['.jpg', '.jpeg', '.png']):
            return MoveImages(self.filename)
        elif(self.file_ext in ['.docx', '.xlsx']):
            return MoveOfficeFiles(self.filename)
        elif(self.file_ext in ['.exe', '.msi']):
            return MoveInstallers(self.filename)
        else:
            return MoveOthers(self.filename)
        
    def move_file(self):
        if (os.path.isdir(self.destination)):
            print(f'Moving --> {self.filename}')
        else:
            os.mkdir(self.destination)
        os.rename(self._get_current_file_path(), self._set_next_file_path())

    def _split_ext(self):
        file_name, file_ext = os.path.splitext(self.filename)
        self.file_name = file_name
        self.file_ext = file_ext

    def _get_current_file_path(self):
        return self.src + '/' + self.filename

    def _set_next_file_path(self):
        return self.destination + self.filename

    def __repr__(self):
        return f'Mover({self.filename})'


class MovePdf(MoveFactory):
    folder_name = 'PDF/'

class MoveImages(MoveFactory):
    folder_name = 'Images/'

class MoveOfficeFiles(MoveFactory):
    folder_name = 'Docs/'

class MoveInstallers(MoveFactory):
    folder_name = 'Installers/'

class MoveOthers(MoveFactory):
    pass