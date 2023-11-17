import os

dirPath = 'data'
ext_list = ['.jpg', '.JPG', '.png', '.PNG']

def get_file_list(dirPath, ext_list):
    """
    dirPath以下にあるext_listで指定したファイル名のパスをリストとして返却
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dirPath):
        for filename in filenames:
            for ext in ext_list:
                if filename.endswith(ext):
                    files_list.append(os.path.join(parent, filename))
                    break
    return files_list

print(get_files_list(dirPath, ext_list))
# ['data/onepiece05_sanji.png', 'data/onepiece01_luffy2.png', 'data/onepiece02_zoro.png']