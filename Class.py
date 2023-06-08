from collections import UserDict
from datetime import datetime, timedelta


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
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def correct_value(self):
        pass


class Birthday(Field):
    def correct_value(self):
        pass

# екземпляри класів присвоєні змінним для перевірки та відладки
# if __name__ == '__main__':
#     name = Name('Bill')
#     phone = Phone('1234567890')
#     rec = Record(name, phone)
#     ab = AddressBook()
#     ab.add_record(rec)
#     assert isinstance(ab['Bill'], Record)
#     assert isinstance(ab['Bill'].name, Name)
#     assert isinstance(ab['Bill'].phones, list)
#     assert isinstance(ab['Bill'].phones[0], Phone)
#     assert ab['Bill'].phones[0].value == '1234567890'
#     print('All Ok)')
