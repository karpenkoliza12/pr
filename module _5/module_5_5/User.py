#Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
#Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем.
# Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
from UrTube import *
from Video import *
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


# u1 = User('liza', 123, 12)
# print(User.users)
