import tkinter as tk

def click_btn(event):
    global expression
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(expression)
            expression = str(result)
        except Exception as e:
            expression = "Erro"
        finally:
            update_display()
    elif text == "C":
        expression = ""
        update_display()
    else:
        expression += text
        update_display()

def key_press(event):
    global expression
    key = event.char
    if key.isdigit() or key in "+-*/":
        expression += key
        update_display()
    elif key == "\r" or key == "\n":
        try:
            result = eval(expression)
            expression = str(result)
        except Exception as e:
            expression = "Erro"
        finally:
            update_display()

def update_display():
    display_var.set(expression)

# Criar a janela
window = tk.Tk()
window.title("Calculadora Básica")

# Variável para armazenar a expressão
expression = ""

# Variável para atualizar o display
display_var = tk.StringVar()
display_var.set("")

# Criar o display
display = tk.Entry(window, textvariable=display_var, font=("Arial", 18), bd=10, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Adicionar botões à janela
for (text, row, col) in buttons:
    btn = tk.Button(window, text=text, font=("Arial", 18), width=5, height=2)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", click_btn)

# Vincular eventos de teclado
window.bind("<Key>", key_press)

# Rodar a aplicação
window.mainloop()
