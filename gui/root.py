import tkinter as tk
from db.db_operations import *
from parsers.remanga_parser import *

def button_new_manga_ins():
    new_name = str(entry_name.get())
    cr_chap = int(entry_chap.get())
    new_manga_ins(new_name, cr_chap)

def button_manga_parser():
    manga_name_upd = str(entry_manga_name.get())
    params = manga_parser(manga_name_upd)
    manga_upd(str(params[0]), int(params[1]), str(params[2]), manga_name_upd )
    

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

# Создаем метку для поля ввода имени манги для второй функции
label_manga_name = tk.Label(root, text="Название манги для обновления:")
label_manga_name.pack()

# Создаем поле ввода для имени манги для второй функции
entry_manga_name = tk.Entry(root)
entry_manga_name.pack()

# Создаем кнопки
button_ins = tk.Button(root, text="Добавить мангу", command=button_new_manga_ins)
button_ins.pack(pady=20)

button_upd = tk.Button(root, text="Обновить последние главы", command=button_manga_parser)
button_upd.pack(pady=20)

# Запускаем главный цикл обработки событий
root.mainloop()