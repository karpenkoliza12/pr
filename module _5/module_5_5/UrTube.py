# Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
from User import *
from Video import *
class UrTube:
    def __init__(self, users, videos):
        self.users.append(User)
        self.videos.append(Video)
        current_user = None

    def lod_in(self, nickname, password):
        for nic, pas in self.users.items():
            if nic == nickname and pas == password:
                self.current_user = self.users[]
