from datetime import date

class Note:
    def __init__(self, name, content, id=None, date=None):
        self.id = id
        self.date = date
        self.name = name
        self.content = content
    def __str__(self) -> str:
        return "ID: " + self.id + " Date: " + self.date + "\nName of the Note: " + self.name + "\nContent: " + self.content
