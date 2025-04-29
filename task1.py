import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")

# Создаем поле ввода
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Функция для добавления символа в поле ввода
def press(key):
    entry.insert(tk.END, key)

# Функция для вычисления выражения
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

# Функция для очистки поля
def clear():
    entry.delete(0, tk.END)

# Кнопки калькулятора
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Создаем кнопки
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), command=calculate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), command=lambda t=text: press(t)).grid(row=row, column=col)

# Запуск главного цикла
root.mainloop()
