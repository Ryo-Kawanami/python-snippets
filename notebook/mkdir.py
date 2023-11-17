import os

path = 'path/to/dir'

def mkdir(path):
    """
    pathで指定したディレクトリがまだなければ作成してディレクトリのパスを返却
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return path

print(mkdir(path))
# path/to/dir