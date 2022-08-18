import os

BASE = 'pystable/_extensions/'
PATH_DEFAULT = '{}libstable.so'.format(BASE)


def libstable_path(libstable_path=None) -> str:
    '''Get path to libstable.so'''
    libstable_path = PATH_DEFAULT
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.abspath(os.path.join(path, os.pardir))
    return os.path.abspath(os.path.join(path, libstable_path))
