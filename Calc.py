import tkinter as tk
from tkinter import font as tkfont

class Calculadora:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora do Lucas")
        self.janela.geometry("300x400")
        self.janela.resizable(0, 0)
        self.janela.configure(bg='#333')

        self.font_style = tkfont.Font(family='Helvetica', size=15, weight='bold')
        self.entry_font_style = tkfont.Font(family='Helvetica', size=20, weight='bold')

        self.entrada = tk.Entry(self.janela, width=16, font=self.entry_font_style, bd=10, insertwidth=2, bg="#eee", justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
        self.entrada.bind('<Return>', lambda event: self.calcula())  # Vincula a tecla Enter ao cálculo

        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), (',', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)
        ]

        for botao in botoes:
            if len(botao) == 3:
                texto, linha, coluna = botao
                colspan = 1
            else:
                texto, linha, coluna, colspan = botao

            if texto == '=':
                bg_color = "#ff5733"
                fg_color = "#fff"
            elif texto == 'C':
                bg_color = "#ff3333"
                fg_color = "#fff"
            else:
                bg_color = "#555"
                fg_color = "#fff"
            
            button = tk.Button(self.janela, text=texto, width=5, height=2, font=self.font_style, bg=bg_color, fg=fg_color,
                               command=lambda t=texto: self.click(t))
            button.grid(row=linha, column=coluna, columnspan=colspan, sticky='nsew', padx=5, pady=5)

        for i in range(6):
            self.janela.grid_rowconfigure(i, weight=1)
            self.janela.grid_columnconfigure(i, weight=1)

    def click(self, texto):
        if texto == '=':
            self.calcula()
        elif texto == 'C':
            self.limpar()
        else:
            self.adiciona_digito(texto)

    def adiciona_digito(self, digito):
        self.entrada.insert(tk.END, digito)

    def calcula(self):
        try:
            resultado = eval(self.entrada.get().replace(",", "."))
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(resultado))
        except Exception:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Erro")

    def limpar(self):
        self.entrada.delete(0, tk.END)

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()
