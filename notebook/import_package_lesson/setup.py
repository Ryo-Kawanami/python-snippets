from distutils.core import setup

setup(
    name='python-sample-package',
    version='1.0.0',
    packages=['package', 'package.talk', 'package.tools'],
    url='',
    license='Free',
    author='Ryo Kawanami',
    author_email='',
    description='Python Sample Package'
)

# 実行コマンド：python3 setup.py sdist
# 結果：
# dist以下にpython-sample-package-1.0.0.tar.gz, 直下にMANIFESTファイルが作成される
# このtar.gzファイルをユーザに共有することでパッケージを配布できる

# 実行コマンド：pip install .
# 結果：パッケージがインストールされる
