# Реализовать дескрипторы для любых двух классов.

import datetime


class CheckIsInt:
    def __set_name__(self, owner, attr_name):
        self.attr_name = attr_name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('Type error')
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr_name]

    def __delete__(self, instance):
        del instance.__dict__[self.attr_name]


class CheckIsDate:
    def __set_name__(self, owner, attr_name):
        self.attr_name = attr_name

    def __set__(self, instance, value):
        if not isinstance(value, datetime.datetime):
            raise ValueError('Type error')
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr_name]

    def __delete__(self, instance):
        del instance.__dict__[self.attr_name]


class CheckLen:
    def __set_name__(self, owner, attr_name):
        self.attr_name = attr_name

    def __set__(self, instance, value):
        if len(value) > 128:
            raise ValueError('Length exceeded')
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr_name]

    def __delete__(self, instance):
        del instance.__dict__[self.attr_name]


class User:
    user_id = CheckIsInt()
    auth_date_time = CheckIsDate()

    def __init__(self, user_id, name, auth_date_time):
        self.user_id = user_id
        self.name = name
        self.auth_date_time = auth_date_time

    def __str__(self):
        return f'Пользователь: {self.name}, id: {self.user_id}, зарегистрирован: {self.auth_date_time}'


class Message:
    message_id = CheckIsInt()
    sender_id = CheckIsInt()
    receiver_id = CheckIsInt()
    message_text = CheckLen()
    send_date_time = CheckIsDate()

    def __init__(self, message_id, message_text, sender_id, receiver_id, send_date_time):
        self.message_id = message_id
        self.message_text = message_text
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.send_date_time = send_date_time

    def __str__(self):
        return f'Идентификатор сообщения: {self.message_id}, текст сообщения: {self.message_text}, ' \
               f'id отправителя: {self.sender_id}, получателя: {self.receiver_id}'


class TypeValidation:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Введенное значение должно быть строкой")
        instance.__dict__[self. my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self. my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = TypeValidation()
    surname = TypeValidation()
    position = TypeValidation()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'Сотрудник {self.name} {self.surname}, находится в должности: ' \
               f'{self.position}.'

    def get_total_income(self):
        return f'Доход всего составляет: {self._income["wage"] + self._income["bonus"]}'

    def __str__(self):
        return f'{self.get_full_name()} {Position.get_total_income(self)}'


new_user = User(5, 'Перцев Александр', datetime.datetime.now())
print(new_user)
new_message = Message(1, 'Александр, здравствуйте!', 3, 5, datetime.datetime.now())
print(new_message)
worker = Position(11165, 'Перцев', 'Мастер', 50000, 5000)
print(worker.get_full_name())
print(worker.get_total_income())
print(worker)
