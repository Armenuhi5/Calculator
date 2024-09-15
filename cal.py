import tkinter as tk
from tkinter import messagebox

def add_digit(digit):
    value = calc.get() 
    if value == '0':
        value = digit
    else:
        value += digit
    calc.delete(0, tk.END)
    calc.insert(0, value)

def add_operation(operation):
    value = calc.get()
    if value and value[-1] in '-+/*':  
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)  

def calculate():
    value = calc.get()
    try:
        if value and value[-1] in '+-/*':
            value = value[:-1]  
        result = eval(value)
        calc.delete(0, tk.END)
        calc.insert(0, result)
    except (SyntaxError, ZeroDivisionError) as e:
        messagebox.showerror("Ошибка", "Недопустимый ввод или деление на ноль")

def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13),
                     command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=clear)

root = tk.Tk()
root.title("Мой первый калькулятор")
root.geometry("240x270+100+200")
root['bg'] = 'pink'

calc = tk.Entry(root, justify=tk.RIGHT, font=("Arial", 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)


for i in range(1, 10):
    make_digit_button(str(i)).grid(row=(i-1)//3 + 1, column=(i-1)%3, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)


operations = ['+', '-', '*', '/']
for i, op in enumerate(operations):
    make_operation_button(op).grid(row=i+1, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)


for i in range(4):
    root.grid_columnconfigure(i, minsize=60)
    root.grid_rowconfigure(i+1, minsize=60)

root.mainloop()