import sys
from keeper import PhotosKeeper


class InputHandler:
    def __init__(self):
        self.keeper = PhotosKeeper()
        self.command_list = {
            'help': InputHandler.help,
            'svk': self.save_vk,
            'sok': self.save_ok,
            'stoken': self.set_ya_token,
            'exit': InputHandler.exit
        }

    @staticmethod
    def __get_user_input():
        try:
            user_id = int(input('Введите id пользователя: '))
            photos_count = int(input('Введите максимальное кол-во сохраняемых фотографий: '))
        except ValueError as ex:
            raise ValueError("Введены некорректные данные\n")
        return user_id, photos_count

    @staticmethod
    def exit():
        sys.exit()

    @staticmethod
    def help():
        lines = """
         |Программа для сохранения фотографий из ВК и ОК на яндекс диске|
         svk - сохранить фото пользователя с вк
         sok - сохранить фото пользователя с ок
         stoken - установить токен для яндекс диска
         exit - выйти
         """
        print(lines)

    def save_vk(self):
        user_id, photos_count = InputHandler.__get_user_input()
        self.keeper.query_save_photos_vk(user_id, photos_count)

    def save_ok(self):
        user_id, photos_count = InputHandler.__get_user_input()
        self.keeper.query_save_photos_ok(user_id, photos_count)

    def set_ya_token(self):
        token = input('Введите токен: ')
        self.keeper.save_yandex_token(token)
        print('Токен сохранен успешно')

    def execute_command(self, command):
        if command not in self.command_list:
            print(f'Неизвестаня команда {command} введите help')
            return

        self.command_list[command]()

    def main_loop(self):
        self.help()
        while True:
            command = input('Введите комманду: ')
            try:
                self.execute_command(command)
            except ValueError as ex:
                print(f'Ошибка при выполнении команды: {ex}')


if __name__ == "__main__":
    handler = InputHandler()
    handler.main_loop()
