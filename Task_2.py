class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

    def validate_phone(self, value):
        return len(value) == 10 and value.isdigit()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return True
        return False

    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number
                return True
        return False

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        phones_str = "; ".join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False
