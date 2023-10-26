from imports import *

# Создаем экземпляр главного окна
root = tk.Tk()
root.title("MangaDB")

# Устанавливаем размеры окна
window_width = 735
window_height = 375
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)    # Вычисляем координату x для размещения окна по центру экрана
y_coordinate = (screen_height / 2) - (window_height / 2)    # Вычисляем координату y для размещения окна по центру экрана
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")    # Устанавливаем геометрию окна

# Создаем метку для ввода названия манги
label = tk.Label(root, text="Введите название манги:")
label.pack(pady=5)
label.place(x=50, y=5)

# Создаем поле ввода
entry = tk.Entry(root, width=50)
entry.pack(pady=10)
entry.place(x=50, y=25)

# Создаем текстовый блок для отображения названий манги
manga_names_text = tk.Text(root, height=16, width=52)
manga_names_text.pack(pady=10)
manga_names_text.place(x=200, y=75)
manga_names_text.configure(font=("Georgia", 10))    # Устанавливаем шрифт текстового блока

# Создаем вертикальный ползунок для текстового блока
scrollbar = tk.Scrollbar(root, command=manga_names_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
manga_names_text.config(yscrollcommand=scrollbar.set)

# Создаем подключение к базе данных с использованием контекстного менеджера
with create_connection() as conn:

    # Функция для кнопки "Читать" мангу
    def button_manga_read():
        manga_name = entry.get()
        url = get_manga_url(manga_name)
        wb.open_new_tab(url)

    x_button = 50
    y_button = 75
    const_coord = 47

    button_read = tk.Button(root, text="Читать", command=button_manga_read)
    button_read.pack(pady=10)
    button_read.place(x=x_button, y=y_button)

    # Функция для кнопки "Добавить" главу манги
    def button_new_manga_ins():

        def input_window_ins():
            new_name = str(entry.get())
            cr_chap = int(entry_chap.get())
            new_manga_ins(new_name, cr_chap)
            input_window.destroy()

        input_window = tk.Toplevel(root)
        input_window.title("Добавить новую мангу")

        # Устанавливаем размеры окна
        window_width = 300
        window_height = 100
        screen_width = input_window.winfo_screenwidth()
        screen_height = input_window.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        input_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

        # Создаем метку для поля ввода текущей главы
        label = tk.Label(input_window, text="Текущая глава:")
        label.pack()

        # Создаем поле ввода для текущей главы
        entry_chap = tk.Entry(input_window, width=30)
        entry_chap.pack()

        # Создаем кнопку для выполнения операции
        button = tk.Button(input_window, text="Принять", command=input_window_ins)
        button.pack(pady=20)

    button_ins = tk.Button(root, text="Добавить", command=button_new_manga_ins)
    button_ins.pack(pady=10)
    button_ins.place(x=x_button, y=y_button + const_coord)

    # Функция для кнопки "Обновить" главу манги
    def button_manga_chap_upd():

        def input_window_upd_chap():
            name_upd = str(entry.get())
            cr_chap = int(entry_chap.get())
            manga_chap_upd(name_upd, cr_chap)
            input_window.destroy()

        input_window = tk.Toplevel(root)
        input_window.title("Обновить текущую главу манги")

        window_width = 400
        window_height = 100
        screen_width = input_window.winfo_screenwidth()
        screen_height = input_window.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        input_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

        label = tk.Label(input_window, text="Текущая глава:")
        label.pack()

        entry_chap = tk.Entry(input_window, width=30)
        entry_chap.pack()

        button = tk.Button(input_window, text="Принять", command=input_window_upd_chap)
        button.pack(pady=20)

    button_upd = tk.Button(root, text="Обновить", command=button_manga_chap_upd)
    button_upd.pack(pady=10)
    button_upd.place(x=x_button, y=y_button + 2 * const_coord)

    # Функция для кнопки "Изменить статус" манги
    def button_manga_desc_upd():

        def input_window_desc_upd():
            desc = str(entry_desc.get())
            name = str(entry.get())
            manga_desc_upd(desc, name)
            input_window.destroy()

        input_window = tk.Toplevel(root)
        input_window.title("Добавить/Обновить статус манги")

        window_width = 400
        window_height = 100
        screen_width = input_window.winfo_screenwidth()
        screen_height = input_window.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        input_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

        label = tk.Label(input_window, text="Статус манги:")
        label.pack()

        entry_desc = tk.Entry(input_window, width=30)
        entry_desc.pack()

        button = tk.Button(input_window, text="Принять", command=input_window_desc_upd)
        button.pack(pady=20)

    button_desc_upd = tk.Button(root, text="Изменить статус", command=button_manga_desc_upd)
    button_desc_upd.pack(pady=10)
    button_desc_upd.place(x=x_button, y=y_button + 3 * const_coord)

    # Функция для кнопки "Сведения" о манге
    def button_manga_query():

        # Получаем данные из функции manga_query
        data = manga_query()

        def input_window_manga_query():

            input_window = tk.Toplevel(root)
            input_window.title("Сведения о манге")

            window_width = 600
            window_height = 110
            screen_width = input_window.winfo_screenwidth()
            screen_height = input_window.winfo_screenheight()
            x_coordinate = (screen_width / 2) - (window_width / 2)
            y_coordinate = (screen_height / 2) - (window_height / 2)
            input_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

            # Создание поля (Text) для отображения данных JSON
            text = tk.Text(input_window)
            text.pack()

            requested_name = str(entry.get())    # Получение введенного значения из поля ввода
            for item in data:
                if item['manga_name'] == requested_name:
                    text.delete(1.0, tk.END)    # Очистка содержимого поля
                    text.insert(tk.END, f"Имя манги: {item['manga_name']}\n"
                                        f"Ссылка на мангу: {item['manga_url']}\n"
                                        f"Текущая глава: {item['current_chapter']}\n"
                                        f"Последняя глава: {item['last_chapter']}\n"
                                        f"Дата последней главы: {item['last_chapter_date']}\n"
                                        f"Статус манги: {item['manga_desc']}\n"
                                        )
                    return

            text.delete(1.0, tk.END)
            text.insert(tk.END, "Данные по ключу не найдены.")

        input_window_manga_query()

    button_comp = tk.Button(root, text="Сведения", command=button_manga_query)
    button_comp.pack(pady=10)
    button_comp.place(x=x_button, y=y_button + 4 * const_coord)

    # Функция для кнопки "Удалить" мангу
    def button_manga_del():
        manga_name = entry.get()
        manga_del(manga_name)

    button_del = tk.Button(root, text="Удалить", command=button_manga_del)
    button_del.pack(pady=10)
    button_del.place(x=x_button, y=y_button + 5 * const_coord)

    # Функция для кнопки "R"
    def button_manga_reset():
        
        data = manga_query()

        # Создаем список кортежей с именами манги и разницей между последней главой и текущей главой
        manga_details = [(item["manga_name"], math.ceil(item["last_chapter"] - item["current_chapter"])) for item in data if item["last_chapter"] is not None]

        # Сортируем список по второму элементу каждого кортежа
        manga_details.sort(key=lambda x: x[1], reverse=True)

        # Очищаем текстовое поле и добавляем имена манги и разницу между главами
        manga_names_text.delete(1.0, tk.END)
        if manga_details:
            for name, diff in manga_details:
                manga_names_text.insert(tk.END, f"{name}: {diff}\n")

    button_reset = tk.Button(root, text="R", command=button_manga_reset, font=("Georgia", 7))
    button_reset.place(x=360, y=23)

    # Функция для кнопки "Copy"
    def copy_text():
        root.clipboard_clear()    # Очищаем буфер обмена
        root.clipboard_append(manga_names_text.selection_get())    # Сохраняем в буфер обмена выделенный текст

    button_copy = tk.Button(root, text="Copy", command=copy_text, font=("Georgia", 7))
    button_copy.place(x=380, y=23)

    # Функция для кнопки "Запуск анализатора"
    def button_manga_parser():
        
        def close_window():
            new_window.destroy()

        data = manga_query()

        # Окно для вывода результатов анализа
        new_window = tk.Toplevel(root)
        new_window.title("Ход выполнения анализа")
        window_width = 435
        window_height = 500
        screen_width = new_window.winfo_screenwidth()
        screen_height = new_window.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        new_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

        text_widget = tk.Text(new_window,height=30, width=40)
        text_widget.place(x=50, y=37)
        text_widget.configure(font=("Georgia", 8))
        
        scrollbar = tk.Scrollbar(new_window, command=text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.config(yscrollcommand=scrollbar.set)

        # Получаем список имен манги
        manga_names = [item["manga_name"] for item in data]

        new_window.update()
        
        # Проходим по списку и обновляем данные из трех разных источников, выбирая максимальное значение
        for i in range(len(manga_names)):

            manga_list = []

            # Используем различные функции парсинга для получения данных
            remanga_result = remanga_parser(manga_names[i])
            if remanga_result is not None:
                manga_list.append(remanga_result)

            mangalib_result = mangalib_parser(manga_names[i])
            if mangalib_result is not None:
                manga_list.append(mangalib_result)

            readmanga_result = readmanga_parser(manga_names[i])
            if readmanga_result is not None:
                manga_list.append(readmanga_result)

            com_x_result = com_x_parser(manga_names[i])
            if com_x_result is not None:
                manga_list.append(com_x_result)

            if manga_list != []:
                # Находим максимальное значение из списка
                result = max(manga_list, key=lambda x: x[1])
                output_text = f'Манга - "{manga_names[i]}" была успешно обновлена\n'
                text_widget.insert(tk.END, output_text)
                new_window.update()
            
                # Обновляем данные манги
                manga_upd(result[0], result[1], result[2], manga_names[i])
            else:
                error_text = f'"{manga_names[i]}" - критический промах\n'
                text_widget.insert(tk.END, error_text)
                new_window.update()
                continue

        button = tk.Button(new_window, text="Принять", command=close_window)
        button.pack(pady=20)
        button.place(x=188, y=467)

    button_start = tk.Button(root, text="Запуск анализатора", command=button_manga_parser, width=20, height=2, font=("Georgia", 10))
    button_start.place(x=501, y=23)

# Запускаем главный цикл обработки событий
root.mainloop()