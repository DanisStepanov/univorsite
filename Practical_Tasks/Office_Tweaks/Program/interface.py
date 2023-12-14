# img_viewer.py

import PySimpleGUI as sg
import os.path
import cod
import viewier_new
import viewier


def create_main_window():
    # Установить тему для окна
    sg.theme('DarkAmber')

    # Определение компоновки окна, состоящей из виджетов (элементов GUI)
    layout = [
        [sg.Text('Основное окно')],  # Текстовый виджет (надпись)
        [sg.Button('Перейти к окну 2'), sg.Button('Выход')]  # Добавляем две кнопки
    ]

    # Возврат объекта Window с заголовком 'Окно 1' и вышеопределённой компоновкой
    return sg.Window('Окно 1', layout, finalize=True)

# Определение функции для создания второго окна
def create_second_window():
    # Установить другую тему для второго окна
    sg.theme('LightBlue')

    # Определение компоновки второго окна
    layout = [
        [sg.Text('Второе окно')],  # Текстовый виджет
        [sg.Button('Назад'), sg.Button('Выход')]  # Две кнопки для навигации и выхода
    ]

    # Возврат объекта Window с заголовком 'Окно 2' и компоновкой
    return sg.Window('Окно 2', layout, finalize=True)

# Создание первого окна и инициализация переменной window2 значением None
window1, window2 = create_main_window(), None
file_list_column = [
    [
        sg.Text("Поиск"),sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),sg.FolderBrowse(),
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
    ],
[
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

image_viewer_column = [
    [sg.Text("Выберите файл из списка слева:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Button('Доступные действия с файлом', size=(20, 2), disabled=True, button_color='white',key="-ENTER-")],
    [sg.Button('Удалить файл', size=(10, 1), disabled=True, button_color='red', key='-DELETE-')],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Menu", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        # cod.get_current_catalog(folder)
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
        ]
        window["-FILE LIST-"].update(fnames)
    try:
        window=["-SHOW-"].update(viewier.show())
    except:
        pass

    if event == '-FILE LIST-':
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()
