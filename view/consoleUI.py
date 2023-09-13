from view.texts import *
from model.note import Note

import datetime

def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print(input_error)
        
def print_notes(notes: Note):
    print_message("All notes")
    if notes == None or notes == []:
        print("No notes found")
    else:
        for note in notes:
            print_note(note)

def print_note(message: str):
    if message == None:
        print("Note not found")
    else: 
        print("-" * 30)
        print(message)
        print("-" * 30)

def enter_id(message=None):
    print_message("Enter the ID " + message)
    id = input("ID: ")
    return id

def enter_date():
    print_message("Enter date to see notes only from this date")
    
    while True:
        date_input = input("Date in format YYYY-MM-DD: ")
        
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")



def enter_note(message=None):
    if message != None:
        print_message("Enter the note info " + message)
        name = input("The header: ")
        content = input()
        note = Note(name, content)
        return note

def print_message(message: str):
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')
