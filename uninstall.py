import os
import getpass
import shutil

USER_NAME = getpass.getuser()
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\open.bat' % USER_NAME
program_path = r"C:\Zoiper"

if (os.path.isfile(bat_path)):
    print('Удаление из автозапуска...')
    os.remove(bat_path)
else:
    print('Не обнаружен batch файл.')

if (os.path.exists(program_path)):
    print('Удаление программы...')
    os.path.join(os.getcwd(), program_path)
    shutil.rmtree(program_path)
else:
    print('Программа не обнаружена!')
