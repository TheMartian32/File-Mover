from pathlib import Path
import shutil
import os
from time import sleep


def ask_for(prompt, error_msg=None, _type=None):
    """ While the desired prompt is not given, it repeats the prompt. """
    while True:
        inp = input(prompt).strip()
        if not inp:
            if error_msg:
                print(error_msg)
            continue

        if _type:
            try:
                inp = _type(inp)
            except ValueError:
                if error_msg:
                    print(error_msg)
                continue

        return inp


def move(file_extension=str):
    """
    Moves any .jpg file to the desired folder
    """
    # * Creating / Finding folder
    not_folder = True
    while not_folder:
        folder = ask_for(
            '\nDirectory file path ( enter "new" or just enter "existing" if you already have a folder ): ', _type=str).lower()

        # Creating new folder
        if folder == 'new':
            print('\nWhat would you like your folder to be called?')
            print('IMPORTANT: This new directory will be created in the current directory this script is running in.')
            folder = ask_for(': ')
            try:
                #! Define your own path here. It should be the directory the script is running in.
                os.mkdir(f'/{folder}')
            except:
                print('\nInvalid path.')
                print('\nCheck if the directory you tried to create already exists.')
            else:
                print('\nContinuing...')
                not_folder = False

        # Pre existing folder
        elif folder == 'existing':
            folder = ask_for(
                '\nWhats the path to the pre existing directory?: ')
            if os.path.isdir(folder):
                print('\nContinuing...')
                not_folder = False
            else:
                print('\nThe path you gave was not a directory.')
                not_folder = False
                raise NotADirectoryError
        while True:
            # * For every filename in the listed directory, it moves the file to the desired folder.
            for filename in os.listdir():
                if filename.endswith(f'{file_extension}'):
                    # * Using F-string to have every file moved.
                    os.replace(f'{filename}', f'{folder}/{filename}')
            else:
                print(f'No more {file_extension} files to move.')
                break


if __name__ == "__main__":
    def main():
        print('\nDISCLAIMER: You may want to make a copy of your data beforehand if its especially important. Buggy code can cause you to lose your data.')
        sleep(2.75)
        user_file_extension = ask_for(
            '\nFile extension you would like to move into a folder ( EX: .txt or .PDF | Case Sensitive ): ')
        move(user_file_extension)
    main()
    repeat = ''
    while True:
        # * Asks to repeat the script.
        repeat = input(
            '\nWould you like to repeat the program? (Y/N): ').lower()
        if repeat[0] == 'y':
            main()
            continue
        if repeat[0] == 'n':
            break
