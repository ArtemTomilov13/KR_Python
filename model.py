import csv
from csv import writer

def new_file():
    file = "notes.csv"
    return(file)

def show_note():
    with open(new_file(), "r") as s:
        return(s.read())

def filter_by_date(a):
    start_date = a[0]
    end_date = a[1]
    with open(new_file(), mode="r") as inp:
        data = csv.reader(inp, delimiter = ";", lineterminator="\r")
        for row in data:
            if start_date >= row[3] >= end_date:
                print(row, sep="\n")

def new_note(note): 
    with open(new_file(), mode="a", encoding='utf-8', newline='') as n:
        file_writer = csv.writer(n, delimiter = ";", lineterminator="\r")
        file_writer.writerow(note)
        
def remove_note(id_):
    with open(new_file(), mode="r") as inp:
        newrows = []
        data = csv.reader(inp, delimiter = ";", lineterminator="\r")
        for row in data:
            if row[0] != id_:
                newrows.append(row)
    with open(new_file(), mode="w") as out:
        csv_writer = writer(out, delimiter = ";", lineterminator="\r")
        for row in newrows:
            csv_writer.writerow(row)
   
def change_note(a):
    with open(new_file(), mode="r") as inp:
        newrows = []
        data = csv.reader(inp, delimiter = ";", lineterminator="\r")
        note_id = a[0]
        note = a[1]
        for row in data:
            if row[0] != note_id:
                newrows.append(row)
            else:
                row[2] = note
                newrows.append(row)
    with open(new_file(), mode="w") as out:
        csv_writer = writer(out, delimiter = ";", lineterminator="\r")
        for row in newrows:
            csv_writer.writerow(row)
                