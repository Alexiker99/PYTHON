# Задание 5.
# 
# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.
#
# Подсказки:
#--- используйте модуль chardet, иначе задание не засчитается!!!

import subprocess
import chardet

web_address_list = ['2ch.hk', 'playground.com']

def ping_website(adresses):
    for address in adresses:
        print(f'Пинг сайта: {address}')
        command = ['ping']
        command.append(address)
        res_ping = subprocess.Popen(command, stdout=subprocess.PIPE)
        for line in res_ping.stdout:
            line_encode = chardet.detect(line)
            print(line.decode(line_encode['encoding']))

ping_website(web_address_list)