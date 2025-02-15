'''
utils
'''
import os


def get_script_from_file(filename: str) -> str:
    '''
    gets script from file
    '''
    with open(os.path.join("./db", "scripts", filename), "r", encoding='utf-8') as f:
        return f.read()
