from UrTube import *
from User import *
from Video import *

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

u1 = User('liza', 1234, 18)

u1.lod_in('liza', 1234)
print(ur.current_user)