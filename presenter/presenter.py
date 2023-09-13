from model import service
from view import consoleUI

def start():
    while True:
        choice = consoleUI.menu()
        match choice:
            case 1:
                consoleUI.print_notes(service.retrieve_all())
                consoleUI.print_note(service.open_note(consoleUI.enter_id("to find note")))
            case 2:
                consoleUI.print_notes(service.retrieve_all())
                id = consoleUI.enter_id("to change note")
                consoleUI.print_note(service.open_note(id))
                service.change_note(id, consoleUI.enter_note())
            case 3:
                consoleUI.print_notes(service.retrieve_all())
            case 4:
                consoleUI.print_notes(service.retrieve_all(consoleUI.enter_date()))
            case 5:
                service.add_note(consoleUI.enter_note("to create new note"))
            case 6:
                consoleUI.print_notes(service.retrieve_all())
                id = consoleUI.enter_id("to delete note")
                consoleUI.print_note(service.open_note(id))
                service.delete_note(id)
            case 7:
                break
