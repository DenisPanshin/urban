from time import sleep


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title: str, duration: int, time_now: str = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname in i:
                self.current_user = nickname
                break

    def register(self, nickname, password, age):
        if len(self.users) == 0:
            self.users.append([nickname, password, age])
            self.log_in(nickname, password)

        else:
            for i in self.users:
                if nickname in i:
                    print(f'Пользователь {nickname} уже существует')
                    break
                else:
                    self.users.append([nickname, password, age])
                    self.log_in(nickname, password)
                    break

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, word):
        my_list = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                my_list.append(i.title)
        return my_list

    def watch_video(self, film):
        flag = False
        age1 = 0
        for i in self.users:
            if i[0] == self.current_user:
                age1 = i[2]
                flag = True
                break
        if flag and age1 <= 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')

        elif flag:
            flag = False
            duration = 0
            for i in self.videos:
                if film in i.title:
                    duration = i.duration
                    flag = True
                    break
            if flag:
                for i in range(1, duration + 1):
                    print(i, end=' ')
                print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
