# 3. Задание на закрепление знаний по модулю yaml.
# Написать скрипт, автоматизирующий сохранение данных
# в файле YAML-формата.
#
# Для этого:
#
# Подготовить данные для записи в виде словаря, в котором
# первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа —
# это целое число с юникод-символом, отсутствующим в кодировке
# ASCII(например, €);
#
# Реализовать сохранение данных в файл формата YAML — например,
# в файл file.yaml. При этом обеспечить стилизацию файла с помощью
# параметра default_flow_style, а также установить возможность работы
# с юникодом: allow_unicode = True;
#
# Реализовать считывание данных из созданного файла и проверить,
# совпадают ли они с исходными.

import yaml


def write_to_yaml(destination, data):
    with open(destination, "w", encoding="utf-8") as destination_file:
        yaml.dump(data, destination_file,
                  default_flow_style=True, allow_unicode=True)


def read_from_yaml(origin):
    with open(origin, encoding="utf-8") as origin_file:
        data_from_file = yaml.load(origin_file, Loader=yaml.FullLoader)
        for key, value in data_from_file.items():
            print(f'{key} {value}')


data = {"list_example": ['first', 'second'],
        "int_example": 22,
        "dict_example": {True: '+', False: '-'}
        }

write_to_yaml('Task_3.yaml', data)
read_from_yaml('Task_3.yaml')
