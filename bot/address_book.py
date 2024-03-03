from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            raise ValueError('Enter the correct phone in number format from 5 to 12 characters.')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone)) 
    
    def edit_phone(self, old_phone, new_phone):
        for number in self.phones:
            if number.value == old_phone:
                number.value = new_phone
                return
    
    def remove_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                self.phones.remove(phone) 
                return 'Phone number was removed'            
            else:
                raise KeyError("The specified phone number doesn't exist.")
        

    def find_phone(self, phone):
        return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data.get(name)
        else:
            raise KeyError("The specified name doesn't exist.")
    
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            raise KeyError("The specified name doesn't exist.")

    

   # Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")

john_record.add_phone("1234567890")

john_record.add_phone("5555555555")


    # # Додавання запису John до адресної книги
book.add_record(john_record)

    # # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
# print(jane_record)
book.add_record(jane_record)

    # # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

    # # Знаходження та редагування телефону для John
john = book.find("John")

john.edit_phone("1234567890", "1112223333")


    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
book.delete("Jane")
print(jane_record)


for name, record in book.data.items():
    print(record)



