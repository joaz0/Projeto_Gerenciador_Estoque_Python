import customtkinter 
import sqlite3


def criar_banco():
    banco = sqlite3.connect("banco.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE nomes (nome text)")
    banco.commit()
    banco.close()


def salvar_nome():
    banco = sqlite3.connect("banco.db")
    nome = entry_nome.get()
    cursor = banco.cursor()
    cursor.execute("Insert INTO nomes values ('"+nome+"') ")
    banco.commit()
    banco.close()
    
def listar_nomes():
    banco = sqlite3.connect("banco.db")
    cursor = banco.cursor()
    cursor.execute("select * from nomes")
    recebe_dados = cursor.fetchall()
    banco.close()
    
    nomes = ""
    for i in recebe_dados:
        nomes += "\n" + str(i[0])
    lista.configure(text=nomes)
    

customtkinter.set_appearance_mode("dark")


root = customtkinter.CTk()
root.geometry("300x300")
root.title("Sistema Salva Nome")

text = customtkinter.CTkLabel(root, text="Sistema Salva Nome")
text.pack(pady=10)

entry_nome = customtkinter.CTkEntry(root)
entry_nome.pack(pady= 10)

botao_salvar_nome = customtkinter.CTkButton(root, text="Salvar", command=salvar_nome)
botao_salvar_nome.pack()

botao_listar_nomes = customtkinter.CTkButton(root, text="Listar", command=listar_nomes)
botao_listar_nomes.pack(pady=10)

lista = customtkinter.CTkLabel(root, text="")
lista.pack(pady=10)


root.mainloop()