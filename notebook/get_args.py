import argparse

def get_args():
    """
    引数の読込
    """
    parser = argparse.ArgumentParser(description='set parameters')
    parser.add_argument(
        '--input_dir', '-i', type=str, default='./data/', required=False, help='入力のディレクトリパス')
    parser.add_argument(
        '--output_dir', '-o', type=str, default='./output/', required=False, help='出力のディレクトリパス')
    parser.add_argument(
        '--frame_rate', '-fr', type=int, default=24, required=False, help='フレームレート')
    parser.add_argument(
        '--ext_list', '-ex', type=str, default='.png .jpg', required=False, nargs="*", help='指定する拡張子のリストを".png .jpg"などのように指定')
    parser.add_argument(
        '--no_save', action='store_false', help='本オプションをつけた場合はFalseになりファイル保存の処理を行わない')
    args = parser.parse_args()
    return args


args = get_args()

print(args.input_dir, type(args.input_dir))
print(args.output_dir, type(args.output_dir))
print(args.frame_rate, type(args.frame_rate))
print(args.ext_list, type(args.ext_list))
print(args.no_save, type(args.no_save))

# 実行コマンド： python3 get_args.py -i data -o output -ex .png .jpg --no_save
# 結果： 
# data <class 'str'>
# output <class 'str'>
# 24 <class 'int'>
# ['.png', '.jpg'] <class 'list'>
# False <class 'bool'>
