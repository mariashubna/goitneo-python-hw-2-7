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
            raise ValueError('Enter the correct phone in number format 10 characters.')

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
        