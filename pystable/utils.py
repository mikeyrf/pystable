import os

BASE = 'pystable/_extensions/'
PATH_DEFAULT = '{}libstable.so'.format(BASE)


def libstable_path(libstable_path=None) -> str:
    '''Get path to libstable.so'''
    libstable_path = PATH_DEFAULT
    # TODO: remove
    print('libstable_path', libstable_path)
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.abspath(os.path.join(path, os.pardir))
    # TODO: remove
    print('os.path.abspath(os.path.join(path, libstable_path))',
          os.path.abspath(os.path.join(path, libstable_path)))
    return os.path.abspath(os.path.join(path, libstable_path))
