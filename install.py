import getpass
import os, sys
import time, shutil, requests, zipfile
from colorama import Fore, Back, Style, init
from termcolor import colored
from bs4 import BeautifulSoup

init()

USER_NAME = getpass.getuser()
file_path = r"C:\Zoiper\Zoiper_5.exe"
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
bat_name = "\\open.bat"
url_tree = "https://github.com/ICOQET/git-updater"

def add_to_startup(file_path):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    if (os.path.isfile(bat_path + '\\' + bat_name)):
        print('Удаление прошлых файлов...')
        os.remove(bat_path + '\\' + bat_name)
        time.sleep(2)
    print("Создание автозагрузки...")
    with open(bat_path + '\\' + bat_name, "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
        print(Fore.YELLOW + "$ Zoiper был добавлен в автозагрузку.")
        print(Fore.YELLOW + "$ Расположение batch файла для автозапуска: %s" % bat_path + bat_name)

def extract_zip_and_install_program_files(path_zip, title_zip):
    print('Распаковка архива...')
    print(path_zip + title_zip)
    already_zip = zipfile.ZipFile(path_zip + title_zip)
    already_zip.extractall(path_zip)
    already_zip.close()
    print('Распаковка закончена!')
    path_to_extracted_files = path_zip + 'git-updater-master'
    print("Расположение распаковки: " + path_to_extracted_files)
    print("Установка...")

    dst = 'C:\\Zoiper'
    src = path_to_extracted_files

    if (os.path.exists(dst)):
        print( os.getcwd() )
        os.path.join(os.getcwd(), dst)
        print('Удаление прошлых файлов...')
        shutil.rmtree(dst)

    print("Создание папки: " + dst)
    os.mkdir(dst)
    print("Перемещение в: " + dst)

    path = path_to_extracted_files
    dirs = os.listdir( path )
    for file in dirs:
        print("Перемещение " + file + " в: " + dst)
        shutil.move(path + "\\" + file, dst)
    print('Перемещение остаточных файлов...')
    path_certifi = dst + '\\certifi'
    os.mkdir(path_certifi)
    shutil.move(dst + '\\cacert.pem', path_certifi)
    print("Готово!")

    '''temp_ = 'C:\\Hello'
    if (os.path.isdir(temp_)):
        print("[INFO] Find trash folder...")
        shutil.rmtree(temp_)
        if (os.path.isdir(temp_)):
            print("[INFO] Temp deleted!")
        else:
            print("[ERROR] Don't deleted!")'''

    if (os.path.isdir(dst) and os.path.isdir(path_certifi)):
        print(Fore.RESET)
        print(Back.GREEN + "Установка прошла успешно!")
        print(Back.RESET)
        print(Fore.YELLOW + "Расположение программы: " + dst)
        print('Запуск программы в автоматическом режиме...')
        os.startfile(dst + '\\Zoiper_5.exe')
    else:
        print(Fore.RED + "Сбой установки...")


def download(url_load):
    #url_load = 'https://github.com/ICOQET/git-updater/archive/master.zip'
    title = 'master.zip'
    path_load = 'C:\\Users\\%s\\Downloads\\' % USER_NAME
    send = requests.get(url_load)
    print("Загрузка...")
    with open(path_load + title,'wb') as f:
        f.write(send.content)
        print('Загружено!')
    extract_zip_and_install_program_files(path_load, title)

print("# Установка программы...")
add_to_startup(file_path)
print(Fore.RESET + "Начало распаковки...")
page = requests.get(url_tree)
soup = BeautifulSoup(page.text, 'html.parser')
divs = soup.find_all('div', attrs = { 'class': 'get-repo-modal-options'} )
for soup in divs:
    link = soup.find('div', attrs={ 'class' : 'mt-2' }).find('a').get('href')
    link = 'https://github.com' + link
    download(link)
print(Back.RESET)
print(Fore.RESET)
