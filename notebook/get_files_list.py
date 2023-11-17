import os

dirPath = 'data'
exts_list = ['.jpg', '.JPG', '.png', '.PNG']

def get_files_list(dirPath, exts_list):
    """
    dirPath以下にあるexts_listで指定したファイル名のパスをリストとして返却
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dirPath):
        for filename in filenames:
            for ext in exts_list:
                if filename.endswith(ext):
                    files_list.append(os.path.join(parent, filename))
                    break
    return files_list

print(get_files_list(dirPath, exts_list))
# ['data/onepiece05_sanji.png', 'data/onepiece01_luffy2.png', 'data/onepiece02_zoro.png']