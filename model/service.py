import csv
from datetime import date
from model.note import Note

CSV_FILE_PATH = 'notes.csv'

def open_note(note_id):
    try:
        with open(CSV_FILE_PATH, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] == note_id:
                    return Note(row['name'], row['content'], row['id'], row['date'])
        return None
    except FileNotFoundError:
        print(f"File '{CSV_FILE_PATH}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def change_note(note_id, new_note):
    notes = []

    with open(CSV_FILE_PATH, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_note_id = row['id']
            if csv_note_id == note_id:
                row['name'], row['content'], row['date'] = new_note.name, new_note.content, date.today()
            notes.append(row)

    with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'name', 'content', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(notes)

def retrieve_all(date_filter=None):
    try:
        notes = []

        with open(CSV_FILE_PATH, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                note_date = row['date'].strip()
                if date_filter is None or note_date == date_filter:
                    notes.append(Note(row['name'], row['content'], row['id'], note_date))

        return notes
    except FileNotFoundError:
        print(f"File '{CSV_FILE_PATH}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def add_note(new_note):
    new_id = generate_unique_id()

    with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
        fieldnames = ['id', 'name', 'content', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        new_note.id, new_note.date = new_id, date.today()
        writer.writerow({'id': new_note.id, 'name': new_note.name, 'content': new_note.content, 'date': new_note.date})

def generate_unique_id():
    try:
        with open(CSV_FILE_PATH, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            last_id = max(int(row['id']) for row in reader)

        return last_id + 1
    except FileNotFoundError:
        print(f"File '{CSV_FILE_PATH}' not found. It will be created now")
        return 1
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_note(note_id):
    try:
        with open(CSV_FILE_PATH, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            notes = [row for row in reader if row['id'] != note_id]

        with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'name', 'content', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(notes)

    except FileNotFoundError:
        print(f"File '{CSV_FILE_PATH}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
