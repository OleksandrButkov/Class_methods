from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  # Записи Record в AddressBook зберігаються як значення у словнику.
        # Як ключі використовується значення Record.name.value.


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
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Name(Field):
    pass


class Phone(Field):

    @property
    def correct_phone(self):
        return self._value

    @correct_phone.setter
    def correct_phone(self, value):
        if not isinstance(value, str):
            raise ValueError("Phone number must be a string")
        # Перевірка, чи містить номер телефону тільки цифри та має довжину 10
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number")
        self._value = value


class Birthday(Field):

    @property
    def correct_birthday(self):
        return self._value

    @correct_birthday.setter
    def correct_birthday(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Birthday must be a datetime object")
        self._value = value





if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    birthday = Birthday(datetime(1990, 5, 17))
    ab = AddressBook()
    rec = Record(name, phone, birthday)
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('all ok')
