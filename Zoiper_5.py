# -*- coding: utf-8 -*-

import os, getpass, requests, urllib.request
import tempfile, zipfile, datetime
from bs4 import BeautifulSoup

USER_NAME = getpass.getuser()

url_tree = 'https://github.com/bogdan2200/Hello'
url_load = ''
path_load = ''
title = ''
path_to_extracted_files = ''
title_files = ''

hour_update_1 = "09"
min_update_1 = "30"
sec_update_1 = "00"

hour_update_2 = "14"
min_update_2 = "30"
sec_update_2 = "00"

hour_update_3 = "20"
min_update_3 = "00"
sec_update_3 = "00"

hour_update_4 = "22"
min_update_4 = "00"
sec_update_4 = "00"

hour_update_5 = "04"
min_update_5 = "20"
sec_update_5 = "00"


def start_programs(path_file):
    page = requests.get(url_tree)
    soup = BeautifulSoup(page.text, 'html.parser')
    trs = soup.find_all('tr', attrs = { 'class': 'js-navigation-item'} )
    for soup in trs:
        title_files = soup.find('td', attrs={ 'class' : 'content' }).find('a').get('title')
        print("Запуск: " + title_files)
        os.startfile(path_file + '\\' + title_files)


def extract_zip_and_start(path_zip, title_zip):
    print('Распаковка архива...')
    print(path_zip + title_zip)
    already_zip = zipfile.ZipFile(path_zip + title_zip)
    already_zip.extractall(path_zip)
    already_zip.close()
    print('Распаковка закончена!')
    path_to_extracted_files = path_zip + 'Hello-master'
    print("Расположение распаковки: " + path_to_extracted_files)
    print("Открываю файлы...")
    start_programs(path_to_extracted_files)

def download(url_load):
    #url_load = 'https://github.com/ICOQET/git-updater/archive/master.zip'
    title = 'master.zip'
    path_load = 'C:\\Users\\%s\\Downloads\\' % USER_NAME
    send = requests.get(url_load)
    print("Загрузка...")
    with open(path_load + title,'wb') as f:
        f.write(send.content)
        print('Загружено!')
    extract_zip_and_start(path_load, title)
    #extract_zip(path_load + title, title, path_load)
    #url_open = urllib.request.urlopen(url_load)
    #urllib.request.urlretrieve(url_load, path_load)
    #subprocess.call(path_load + title, shell=True)

    '''file = urllib.request.urlopen(link).read()
    f = open(path_load + title, "wb")
    f.write(file)
    f.close()'''
    #urllib.request.urlretrieve(url_load, title)
    #os.system(path_load + title)
    '''fantasy_zip = zipfile.ZipFile(path_load + title)
    fantasy_zip.extractall(path_load)
    fantasy_zip.close()'''

def get_properties():
    page = requests.get(url_tree)
    soup = BeautifulSoup(page.text, 'html.parser')
    divs = soup.find_all('div', attrs = { 'class': 'get-repo-modal-options'} )
    for soup in divs:
        link = soup.find('div', attrs={ 'class' : 'mt-2' }).find('a').get('href')
        link = 'https://github.com' + link
        print(link)
        download(link)
'''
page = requests.get(url_tree)
soup = BeautifulSoup(page.text, 'html.parser')
trs = soup.find_all('tr', attrs = { 'class': 'js-navigation-item'} )
for soup in trs:
    #datetime_ = soup.find('td', attrs={ 'class' : 'age' }).find('time-ago').get('datetime')
    title = soup.find('td', attrs={ 'class' : 'content' }).find('a').get('title')
    #print(title + "Последнее обновлениe: " + datetime + "Link: " + link) INFO'''


while True:
    now = datetime.datetime.today()
    if(now.strftime("%H") == hour_update_1 or now.strftime("%H") == hour_update_2 or now.strftime("%H") == hour_update_3 or now.strftime("%H") == hour_update_4 or now.strftime("%H") == hour_update_5):
        if(now.strftime("%M") == min_update_1 or now.strftime("%M") == min_update_2 or now.strftime("%M") == min_update_3 or now.strftime("%M") == min_update_4 or now.strftime("%M") == min_update_5):
            if(now.strftime("%S") == sec_update_1 or now.strftime("%S") == sec_update_2 or now.strftime("%S") == sec_update_3 or now.strftime("%S") == sec_update_4 or now.strftime("%S") == sec_update_5):
                print("Time for the update!")
                get_properties()
