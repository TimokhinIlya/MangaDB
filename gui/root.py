import tkinter as tk
import webbrowser  as wb
from db.db_operations import *
from parsers.mangalib_parser import mangalib_parser
from parsers.readmanga_parser import  readmanga_parser
from parsers.remanga_parser import remanga_parser
import math

def button_new_manga_ins():
    def new_manga_ins_input_window():
        new_name = str(entry.get())
        cr_chap = int(entry_chap.get())
        new_manga_ins(new_name, cr_chap)
        input_window_ins.destroy()

    input_window_ins = tk.Toplevel(root)
    input_window_ins.title("Добавить новую мангу")

    # Устанавливаем размеры окна
    window_width = 300
    window_height = 100
    screen_width = input_window_ins.winfo_screenwidth()
    screen_height = input_window_ins.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    input_window_ins.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

    # Создаем метку для поля ввода текущей главы
    label_chap = tk.Label(input_window_ins, text="Текущая глава:")
    label_chap.pack()

    # Создаем поле ввода для текущей главы
    entry_chap = tk.Entry(input_window_ins, width=30)
    entry_chap.pack()

    # Создаем кнопку для выполнения операции
    button_accept = tk.Button(input_window_ins, text="Принять", command=new_manga_ins_input_window)
    button_accept.pack(pady=20)

def button_manga_chap_upd():
    def manga_chap_upd_input_window():
        name_upd = str(entry.get())
        cr_chap = int(entry_chap_upd.get())
        manga_chap_upd(name_upd, cr_chap)
        input_window_upd_chap.destroy()

    input_window_upd_chap = tk.Toplevel(root)
    input_window_upd_chap.title("Обновить текущую главу манги")

    # Устанавливаем размеры окна
    window_width = 400
    window_height = 100
    screen_width = input_window_upd_chap.winfo_screenwidth()
    screen_height = input_window_upd_chap.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    input_window_upd_chap.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

    # Создаем метку для поля ввода текущей главы
    label_chap = tk.Label(input_window_upd_chap, text="Текущая глава:")
    label_chap.pack()

    # Создаем поле ввода для текущей главы
    entry_chap_upd = tk.Entry(input_window_upd_chap, width=30)
    entry_chap_upd.pack()

    # Создаем кнопку для выполнения операции
    button_accept = tk.Button(input_window_upd_chap, text="Принять", command=manga_chap_upd_input_window)
    button_accept.pack(pady=20)

def button_manga_desc_upd():
    def manga_desc_upd_input_window():
        desc = str(entry_desc.get())
        name = str(entry.get())
        manga_desc_upd(desc, name)
        input_window_upd_desc.destroy()
        
    input_window_upd_desc = tk.Toplevel(root)
    input_window_upd_desc.title("Добавить/Обновить статус манги")

    window_width = 400
    window_height = 100
    screen_width = input_window_upd_desc.winfo_screenwidth()
    screen_height = input_window_upd_desc.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    input_window_upd_desc.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

    label_chap = tk.Label(input_window_upd_desc, text="Статус манги:")
    label_chap.pack()

    entry_desc = tk.Entry(input_window_upd_desc, width=30)
    entry_desc.pack()

    button_accept = tk.Button(input_window_upd_desc, text="Принять", command=manga_desc_upd_input_window)
    button_accept.pack(pady=20)

def button_manga_query():
    def create_input_window():
        input_window_manga_query = tk.Toplevel(root)
        input_window_manga_query.title("Сведения о манге")

        window_width = 600
        window_height = 110
        screen_width = input_window_manga_query.winfo_screenwidth()
        screen_height = input_window_manga_query.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        input_window_manga_query.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

        # Создание поля (Text) для отображения данных JSON
        text = tk.Text(input_window_manga_query)
        text.pack()

        requested_name = str(entry.get())  # Получение введенного значения из поля ввода
        for item in data:
            if item['manga_name'] == requested_name:
                text.delete(1.0, tk.END)  # Очистка содержимого поля
                text.insert(tk.END, f"Имя манги: {item['manga_name']}\n"
                                    f"Ссылка на мангу: {item['manga_url']}\n"
                                    f"Текущая глава: {item['current_chapter']}\n"
                                    f"Последняя глава: {item['last_chapter']}\n"
                                    f"Дата последней главы: {item['last_chapter_date']}\n"
                                    f"Статус манги: {item['manga_desc']}\n"
                                    )
                return  # Используйте break вместо return

        text.delete(1.0, tk.END)
        text.insert(tk.END, "Данные по ключу не найдены.")

    create_input_window()

def button_manga_del():
    manga_name = entry.get()
    manga_del(manga_name)

def button_manga_open():
    manga_name = entry.get()
    url = get_manga_url(manga_name)
    wb.open_new_tab(url)

def button_manga_parser():
    manga_names = [item["manga_name"] for item in data]
    for i in range(len(manga_names)):
        manga_list = []
        manga_list.extend([remanga_parser(manga_names[i]), mangalib_parser(manga_names[i]), readmanga_parser(manga_names[i])])
        result = max(manga_list, key = lambda x: x[1])
        manga_upd(result[0], result[1], result[2], manga_names[i])
# Создаем экземпляр главного окна
root = tk.Tk()
root.title("MangaDB")

# Устанавливаем размеры окна
window_width = 670
window_height = 375
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Создаем кнопки
x_button = 50
y_button = 75
const_coord = 47

button_read = tk.Button(root, text="Читать", command=button_manga_open)
button_read.pack(pady=10)
button_read.place(x=x_button, y=y_button)

button_ins = tk.Button(root, text="Добавить", command=button_new_manga_ins)
button_ins.pack(pady=10)
button_ins.place(x=x_button, y=y_button + const_coord)

button_upd = tk.Button(root, text="Обновить", command=button_manga_chap_upd)
button_upd.pack(pady=10)
button_upd.place(x=x_button, y=y_button + 2 * const_coord)

button_upd_desc = tk.Button(root, text="Изменить статус", command=button_manga_desc_upd)
button_upd_desc.pack(pady=10)
button_upd_desc.place(x=x_button, y=y_button + 3 * const_coord)

button_query = tk.Button(root, text="Сведения", command=button_manga_query)
button_query.pack(pady=10)
button_query.place(x=x_button, y=y_button + 4 * const_coord)

button_del = tk.Button(root, text="Удалить", command=button_manga_del)
button_del.pack(pady=10)
button_del.place(x=x_button, y=y_button + 5 * const_coord)

button_query = tk.Button(root, text="Запуск анализатора", command=button_manga_parser, width=20, height=2)
button_query.place(x=458, y=24)

label = tk.Label(root, text="Введите название манги:")
label.pack(pady=5)
label.place(x=50, y=5)

entry = tk.Entry(root,width=50)
entry.pack(pady=10)
entry.place(x=50, y=25)

manga_names_text = tk.Text(root, height=16, width=45)
manga_names_text.pack(pady=10)
manga_names_text.place(x=200, y=75)
manga_names_text.configure(font=("Georgia", 10, "italic"))

data = manga_query()
manga_details = [(item["manga_name"], math.ceil(item["last_chapter"] - item["current_chapter"])) for item in data]
# Сортируем список по второму элементу каждого кортежа
manga_details.sort(key=lambda x: x[1], reverse=True)

# Очищаем текстовое поле и добавляем имена манги и разницу
manga_names_text.delete(1.0, tk.END)
if manga_details:
    for name, diff in manga_details:
        manga_names_text.insert(tk.END, f"{name}\t:{diff}\n")

# Создаем вертикальный ползунок
scrollbar = tk.Scrollbar(root, command=manga_names_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
manga_names_text.config(yscrollcommand=scrollbar.set)

# Запускаем главный цикл обработки событий
root.mainloop()