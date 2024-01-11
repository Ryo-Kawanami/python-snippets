# import package.talk
# print(talk.human.sing())

# ローカル関数とのバッティングを避けるためにパッケージ名をつける。上記のようにフルパスで指定することも可能だが、長くなりすぎるためこちらの方が一般的。
from package.talk import human, animal
# from package.talk import * # *で全てimportできるが何が読み込まれているかわかりづらいのであまり推奨されていない
print(human.sing())
print(human.cry())
print(animal.sing())
print(animal.cry())


# ImportErrorの使い道
# 例えば以下のようにすることでどちらのバージョンのパッケージも使えるようにできる
try:
    from package import utils
except ImportError:
    from package.tools import utils

print(utils.say_twice('word'))


# 実行コマンド：python3 import_package.py
# 結果：
# sing
# cry!cry!
# sing
# cry
# word!word!