from datetime import date
import model as m
import controller as c
def main_menu(): 
    print("Вас приветствует умное приложение Заметки!\nПожалуйста,\
введите нужную цифру в зависимости от Ваших целей:\n\
    1. Показать все существующие заметки\n\
    2. Фильтрация заметок по дате\n\
    3. Добавить новую заметку\n\
    4. Удалить заметку\n\
    5. Изменить заметку\n\
    6. Выход") 
    return int(input("введите выбранную цифру: "))

def view_data(data):
    print(data)

def filter_by_date():
    start_date = str(input("Введите начальную дату в формате ГГГГ-ММ-ДД: "))
    end_date = str(input("Введите конечную дату в формате ГГГГ-ММ-ДД: "))
    return start_date, end_date

def close():
    print(input("Нажмите любую клавишу, чтобы продолжить"))
    c.click_button()

def new_note():
    id_ = str(input("Введите id заметки: "))
    header = str(input("Введите заголовок заметки: "))
    note = str(input("Введите заметку: "))
    date_ = str(date.today())
    result = list([id_, header, note, date_])
    return result

def remove_note():
    note = input(str("Введите id заметки для удаления: "))
    return note

def change_note():
    note_id = input(str("Введите id заметки для изменения: "))
    note_ = input(str("Введите новую заметку: "))
    return note_id, note_
