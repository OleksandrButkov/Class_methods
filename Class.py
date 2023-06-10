from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  # Записи Record в AddressBook зберігаються як значення у словнику.
        # Як ключі використовується значення Record.name.value.

    def iterator(self, n):
        count = 0
        for record in self.data.values():
            yield record
            count += 1
            if count >= n:
                return

# Клас, який відповідає за логіку додавання та обробки полів
class Record:
    def __init__(self, name, phone, birthday):
        self.name = name  # Обов'язкове поле name
        self.phones = [phone]
        self.birthday = birthday

    def add_phone(self, phone):
        self.phones.append(phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index_of_old_phone = self.phones.index(old_phone)
        self.phones[index_of_old_phone] = new_phone

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.today()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day)
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day)
            return (next_birthday - today).days


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    pass


class Phone(Field):

    @property
    def correct_phone(self):
        return self.__value

    @correct_phone.setter
    def correct_phone(self, value):
        if not isinstance(value, str):
            raise ValueError("Phone number must be a string")
        # Перевірка, чи містить номер телефону тільки цифри та має довжину 10
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number")
        self.__value = value


class Birthday(Field):

    @property
    def correct_birthday(self):
        return self.__value

    @correct_birthday.setter
    def correct_birthday(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Birthday must be a datetime object")
        self.__value = value


if __name__ == '__main__':
    pass