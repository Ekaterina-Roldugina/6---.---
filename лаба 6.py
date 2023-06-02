class Directory:
 def __init__(self):
 self.entries = []
 
 def add_entry(self, entry):
 self.entries.append(entry)
 
 def remove_entry(self, entry):
 self.entries.remove(entry)
 
 def search_entries(self, attribute, value):
 found_entries = []
 for entry in self.entries:
 if getattr(entry, attribute) == value:
 found_entries.append(entry)
 return found_entries
 
 def sort_entries(self, attribute):
 self.entries.sort(key=lambda entry: getattr(entry, attribute))
 
class Entry:
 def __init__(self, surname, date_of_birth, phone_number):
 self.surname = surname
 self.date_of_birth = date_of_birth
 self.phone_number = phone_number
 
 def __repr__(self):
 return f"Entry(surname='{self.surname}', date_of_birth='{self.date_of_birth}', phone_number='{self.phone_number}')"
directory = Directory()

entry1 = Entry("Smith", "1990-01-01", "1234567890")
entry2 = Entry("Johnson", "1995-05-05", "9876543210")

directory.add_entry(entry1)
directory.add_entry(entry2)

found_entries = directory.search_entries("surname", "Smith")
print(found_entries)
# Output: [Entry(surname='Smith', date_of_birth='1990-01-01', phone_number='1234567890')]

directory.sort_entries("surname")
print(directory.entries)
# Output: [Entry(surname='Johnson', date_of_birth='1995-05-05', phone_number='9876543210'),
# Entry(surname='Smith', date_of_birth='1990-01-01', phone_number='1234567890')]
