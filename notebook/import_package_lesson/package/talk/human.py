from package.tools import utils
# from ..tools import utils # わかりづらいのであまり推奨されていない

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')
