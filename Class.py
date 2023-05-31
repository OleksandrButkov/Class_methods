from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record   # Записи Record в AddressBook зберігаються як значення у словнику.
                                                # Як ключі використовується значення Record.name.value.


class Record:                                   # Клас, який відповідає за логіку додавання та обробки полів
    def __init__(self, name):
        self.name = Name(name)                  # Обов'язкове поле name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index_of_old_phone = self.phones.index(old_phone)
        self.phones[index_of_old_phone] = new_phone


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


#екземпляри класів присвоєні змінним для перевірки та відладки
address_book = AddressBook()

record1 = Record("John")
phone1 = Phone("123456789")
record1.add_phone(phone1)

record2 = Record("Alice")
phone2 = Phone("987654321")
record2.add_phone(phone2)

address_book.add_record(record1)
address_book.add_record(record2)

print(address_book.data.items())
