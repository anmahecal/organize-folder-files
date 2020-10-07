import os
import sys
from Mover import MoveFactory

def main():
    if sys.platform in ['win32', 'win64']:
        path_to_organize = 'ENTER HERE THE DIRECTORY PATH YOU WANT TO ORGANIZE'
        os.chdir(path_to_organize)

    for filename in os.listdir():
        _, ext = os.path.splitext(filename)
        if (ext):    
            mover = MoveFactory(filename).create_mover()
            mover.move_file()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Something went wrong!')