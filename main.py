"""
Задание: Напишите программу, которая принимает имя файла и выводит его расширение.
Если расширение у файла определить невозможно, выбросите исключение.
В качестве выполненного ДЗ отправить файл с расширением .py в котором будет находится код программы.
"""


def file_extension(filename):
    filename_parts = filename.split(".")
    if len(filename_parts) < 2:
        raise ValueError("Файл без расширения!")
    first, *middle, last = filename_parts
    if (not last or last == " ") or not first and not middle:
        raise ValueError("Файл без расширения!")
    return print(filename_parts[-1])


file_extension("text.txt")
