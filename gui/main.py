import tkinter as tk
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..\db'))
print(sys.path)
from db_operations import *
def button_new_manga_ins():
    name = entry_name.get()
    cr_chap = int(entry_chap.get())
    new_manga_ins(name, cr_chap)

# Создаем экземпляр главного окна
root = tk.Tk()
root.title("MangaDB")

# Устанавливаем размеры окна
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Создаем метку для поля ввода имени манги
label_name = tk.Label(root, text="Название манги:")
label_name.pack()

# Создаем поле ввода для имени манги
entry_name = tk.Entry(root)
entry_name.pack()

# Создаем метку для поля ввода текущей главы
label_chap = tk.Label(root, text="Текущая глава:")
label_chap.pack()

# Создаем поле ввода для текущей главы
entry_chap = tk.Entry(root)
entry_chap.pack()

# Создаем кнопку
button = tk.Button(root, text="Добавить мангу", command=button_new_manga_ins)
button.pack(pady=20)

# Запускаем главный цикл обработки событий
root.mainloop()