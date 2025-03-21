import tkinter as tk
from tkinter import messagebox

def verificar_checkbox():
    # Verifica o estado da Checkbutton
    if var_checkbox.get() == 1:
        print("Checkbox está marcada!")
    else:
        print("Checkbox não está marcada.")

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de Checkbutton")

# Variável para armazenar o estado da Checkbutton
var_checkbox = tk.IntVar()

# Cria a Checkbutton
checkbox = tk.Checkbutton(
    root,
    text="Marque aqui",
    variable=var_checkbox,  # Associa a variável à Checkbutton
    command=verificar_checkbox  # Chama a função quando o estado muda
)
checkbox.pack(pady=20)

# Botão para verificar o estado da Checkbutton manualmente
botao_verificar = tk.Button(
    root,
    text="Verificar Estado",
    command=verificar_checkbox
)
botao_verificar.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()