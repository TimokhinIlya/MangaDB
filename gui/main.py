import tkinter as tk

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

# Создаем функцию, которая будет выполняться при нажатии кнопки
def on_button_click():
    label.config(text="Кнопка нажата!")

# Создаем кнопку
button = tk.Button(root, text="Нажми на меня!", command=on_button_click)
button.pack(pady=20)

# Создаем метку для вывода информации
label = tk.Label(root, text="")
label.pack()

# Запускаем главный цикл обработки событий
root.mainloop()