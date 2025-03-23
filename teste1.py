import  customtkinter
from PIL import Image
import os
from  tkinter import messagebox
from tkinter import ttk
import sqlite3

 
file_path = os.path.dirname(os.path.realpath(__file__))
imagem1 = customtkinter.CTkImage(Image.open(fp="C:/Users/joazr/Downloads/Projetos_senac/lixeira/lixeira 1.png"), size=(35,35))
item_vet = 0
linha_entrada = 0
linha_saida = 0
 
def tela_cadastro():
    quadro_cadastro.grid(row=0 , column=1, pady=5, padx=5)
    quadro_cadastro.grid_propagate(False)
    quadro_edicao.grid_forget()
    quadro_saida.grid_forget()
    quadro_entrada.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_entrada.grid_forget()
    quadro_relatorio_saida.grid_forget()
   
 
def tela_edicao():
    quadro_edicao.grid(row=0 , column=1, pady=5, padx=5)
    quadro_edicao.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_saida.grid_forget()
    quadro_entrada.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_entrada.grid_forget()
    quadro_relatorio_saida.grid_forget()
    dados_edicao()


def tela_saida():
    quadro_saida.grid(row=0 , column=1, pady=5, padx=5)
    quadro_saida.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_edicao.grid_forget()
    quadro_entrada.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_entrada.grid_forget()
    quadro_relatorio_saida.grid_forget()
    dados_saida()

def tela_entrada():
    quadro_entrada.grid(row=0 , column=1, pady=5, padx=5)
    quadro_entrada.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_edicao.grid_forget()
    quadro_saida.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_entrada.grid_forget()
    quadro_relatorio_saida.grid_forget()
    dados_entrada()


def tela_relatorio() :
    quadro_relatorio_estoque.grid(row=0 , column=1, pady=5, padx=5)
    quadro_relatorio_estoque.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_saida.grid_forget()
    quadro_entrada.grid_forget()
    quadro_edicao.grid_forget()
    quadro_relatorio_entrada.grid_forget()
    quadro_relatorio_saida.grid_forget()
    ler_dados_cadastro()


def esconder_relatorio_entrada_saida():
    quadro_relatorio_estoque.grid(row=0 , column=1, pady=5, padx=5)
    quadro_relatorio_estoque.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_saida.grid_forget()
    quadro_entrada.grid_forget()
    quadro_edicao.grid_forget()
    quadro_relatorio_entrada.grid_forget()
    quadro_relatorio_saida.grid_forget()
    ler_dados_cadastro()


def esconder_relatorio_estoque_saida():
    quadro_relatorio_entrada.grid(row=0 , column=1, pady=5, padx=5)
    quadro_relatorio_entrada.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_saida.grid_forget()
    quadro_entrada.grid_forget()
    quadro_edicao.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_saida.grid_forget()

def esconder_relatorio_estoque_entrada():
    quadro_relatorio_saida.grid(row=0 , column=1, pady=5, padx=5)
    quadro_relatorio_saida.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_saida.grid_forget()
    quadro_entrada.grid_forget()
    quadro_edicao.grid_forget()
    quadro_relatorio_estoque.grid_forget()
    quadro_relatorio_entrada.grid_forget()

def abrir_mini_janela():
    mini_janela = customtkinter.CTkToplevel(janela)
    mini_janela.mainloop()

def delete_itens_saida(linhas, botoes):
    linhas.grid_forget()
    botoes.grid_forget()

def adicionar_item_saida():  
    global linha_saida
    item_vet_saida = str(nome_ret.get())
    linha_saida += 1
 
    if item_vet_saida in str(rolagem_saida_checkbox.winfo_children()):    
        try:
            label_saida = customtkinter.CTkLabel(rolagem_saida_selecao_itens, text=item_vet_saida)            
            label_saida.grid(row=linha_saida, column=0, pady=5, padx=5, sticky = "w")    
            lixeira_saida = customtkinter.CTkButton(rolagem_saida_selecao_itens, width=35, height=35, text="", image=imagem1, command=lambda:delete_itens_saida(label_saida, lixeira_saida))
            lixeira_saida.grid(row=linha_saida, column=1, pady=5, padx=100, sticky = "e")
 
        except ValueError:
            return  
 
def delete_itens_entrada(linhas_entrada, botoes_entrada):
    linhas_entrada.grid_forget()
    botoes_entrada.grid_forget()
   
   

def adicionar_item_entrada():  
    global linha_entrada
    item_vet_entrada = str(nome_ent.get())
    linha_entrada += 1
 
    if item_vet_entrada in rolagem_entrada_checkbox:    
        try :  
            label_entrada = customtkinter.CTkLabel(rolagem_entrada_selecao_itens, text=item_vet_entrada)            
            label_entrada.grid(row=linha_entrada, column=0, pady=5, padx=5, sticky = "w")    
            lixeira_entrada = customtkinter.CTkButton(rolagem_entrada_selecao_itens, width=35, height=35, text="", image=imagem1, command=lambda: delete_itens_entrada(label_entrada, lixeira_entrada))
            lixeira_entrada.grid(row=linha_entrada, column=1, pady=5, padx=100, sticky = "e")
 
        except ValueError:
            return  

def export():   
    root_export = customtkinter.CTkToplevel()
    root_export.geometry('300x200')
    root_export.title('')
    root_export.attributes("-topmost", True)
    
    # frame
    frame_root_2 = customtkinter.CTkFrame(master=root_export, width=300, height=200)
    frame_root_2.pack(anchor='center')
    frame_root_2.grid_propagate(False)

    # label
    escolher_relatorio = customtkinter.CTkLabel(master=frame_root_2, text='Escolher Relatorio(s)', text_color="#8471EB")
    escolher_relatorio.grid(row=0, column=0, pady=10)

    Escolher_extensao = customtkinter.CTkLabel(master=frame_root_2, text="Escolher extensão", text_color="#8471EB")
    Escolher_extensao.grid(row=0, column=1, pady=10)

    # checkbox
    exportar_estoque_r2 = customtkinter.CTkCheckBox(master=frame_root_2, text='Exportar estoque', text_color="#8471EB", corner_radius= 30, border_color= '#83A2EB', border_width=2 )
    exportar_estoque_r2.grid(row=1, column=0, sticky='w', )

    exportar_saida_r2 = customtkinter.CTkCheckBox(master=frame_root_2, text='Exportar saida', text_color="#8471EB", corner_radius= 30, border_color= '#83A2EB', border_width=2 )
    exportar_saida_r2.grid(row=2, column=0, sticky='w')

    exportar_entrada_r2 = customtkinter.CTkCheckBox(master=frame_root_2, text='Exportar entrada', text_color="#8471EB", corner_radius= 30, border_color= '#83A2EB', border_width=2 )
    exportar_entrada_r2.grid(row=3, column=0, sticky='w')
    
    word_r2 = customtkinter.CTkCheckBox(master=frame_root_2, text='WORD', text_color="#8471EB", corner_radius= 30, border_color= '#83A2EB', border_width=2 )
    word_r2.grid(row=1, column=1, sticky='e')
    
    pdf_r2 = customtkinter.CTkCheckBox(master=frame_root_2, text='PDF', text_color="#8471EB",  corner_radius= 30, border_color= '#83A2EB', border_width=2 )
    pdf_r2.grid(row=2, column=1, sticky="e")
    
    excel_r2 = customtkinter.CTkCheckBox(master=frame_root_2, text='EXCEL', text_color="#8471EB",  corner_radius= 30, border_color='#83A2EB', border_width=2 )
    excel_r2.grid(row=3, column=1, sticky='e')

    # button
    btn_save_frame_root_2 = customtkinter.CTkButton(master=frame_root_2, text='SALVAR', width=70, corner_radius=30, fg_color="#83A2EB", text_color="black")
    btn_save_frame_root_2.grid(row=4, column=1, sticky="ws")

    btn_cancel_frame_root_2 = customtkinter.CTkButton(master=frame_root_2, text='CANCELAR', width=70, corner_radius= 30, fg_color="#83A2EB", text_color="black")
    btn_cancel_frame_root_2.grid(row=4, column=0, sticky='es')
    
    root_export.mainloop()


def criar_banco():
    BD = sqlite3.connect("BD_GRE.db")
    terminal_sql = BD.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS Produtos (nomes text, quantidade integer, precos float, desc text)")
    BD.commit()
    BD.close()


def salvar_cadastro():
    BD = sqlite3.connect("BD_GRE.db")
    nome_cadastro = entrada_nome_produto.get()
    preco_cadastro = entrada_preco.get()
    quant_cadastro = "0"
    desc_cadastro = textbox_desc.get("1.0", "end")
    terminal_sql = BD.cursor()
    terminal_sql.execute("INSERT INTO produtos VALUES ('"+nome_cadastro+"', '"+quant_cadastro+"', '"+preco_cadastro+"', '"+desc_cadastro+"')")
    entrada_nome_produto.delete(0, "end")
    entrada_preco.delete(0, "end")
    textbox_desc.delete("1.0", "end")
    BD.commit()
    BD.close()


def ler_dados_cadastro():
    BD = sqlite3.connect("BD_GRE.db")
    terminal_sql = BD.cursor()
    terminal_sql.execute("SELECT * FROM Produtos")
    recebe_dados = terminal_sql.fetchall()
    for item in tabela_relatorio_estoque.get_children():
        tabela_relatorio_estoque.delete(item)

    for i in recebe_dados:
        nomes = str(i[0])
        quantidade = str(i[1])
        precos = str(i[2])
        desc = str(i[3])
        tabela_relatorio_estoque.insert("", "end", values=(nomes, quantidade, precos, desc))

    BD.close()

# Variável global para armazenar o checkbox selecionado
item_selecionado = None



def dados_edicao():
    global checkbox_selecionado  # Acessa a variável global
    BD = sqlite3.connect("BD_GRE.db")
    terminal_sql = BD.cursor()
    terminal_sql.execute("SELECT nomes FROM Produtos")
    recebe_dados = terminal_sql.fetchall()

    # Limpa os checkboxes existentes
    for widget in rolagem_edicao.winfo_children():
        widget.destroy()

    # Cria um novo checkbox para cada item
    for item in recebe_dados:
        nome_produto = item[0]

        # Cria uma variável individual para cada checkbox
        var_checkbox = customtkinter.BooleanVar(value=False)

        # Cria o checkbox
        Box_edicao = customtkinter.CTkCheckBox(rolagem_edicao, text=nome_produto, text_color="#8684EB", checkmark_color="#83A2EB", border_color="#83A2EB", variable=var_checkbox, command=lambda n=nome_produto, v=var_checkbox: checkbox_event(n, v))
        Box_edicao.pack(pady=5, padx=5, fill="x")

    BD.close()


def checkbox_event(nome_produto, var_checkbox):
    global checkbox_selecionado, item_selecionado

     # seleciona o checkbox
    if var_checkbox.get(): 
        # Desmarca o checkbox anteriormente selecionado
        if checkbox_selecionado and checkbox_selecionado != var_checkbox:
            checkbox_selecionado.set(False)

        # Atualiza o checkbox selecionado
        checkbox_selecionado = var_checkbox
        # guarda o nome do produto selecionado na variavel item_selecionado
        item_selecionado = nome_produto

        # vai colocar os campos de edição preenchidos com os dados do produto selecionado
        preencher_campos_edicao(nome_produto)

    else:  # Checkbox não selecionado

        # vai limpar os campos de edição se o checkbox nao estiver marcado
        limpar_campos_edicao()
        item_selecionado = None
        checkbox_selecionado = None


def preencher_campos_edicao(nome_produto):
    nome_produto_var = nome_produto[0]
    BD = sqlite3.connect("BD_GRE.db")
    terminal_sql = BD.cursor()
    terminal_sql.execute("SELECT nomes, precos, desc FROM Produtos WHERE nomes = ?", (nome_produto_var,))
    dados_produto = terminal_sql.fetchone()

    if dados_produto:
        # Preenche os campos de edição
        editar_nome.delete(0, "end")
        editar_nome.insert(0, dados_produto[0])  # Nome
        editar_preco.delete(0, "end")
        editar_preco.insert(0, dados_produto[1])  # Preço
        editar_desc.delete("1.0", "end")
        editar_desc.insert("1.0", dados_produto[2])  # Descrição

    BD.close()


def limpar_campos_edicao():
    editar_nome.delete(0, "end")
    editar_preco.delete(0, "end")
    editar_desc.delete("1.0", "end")


def salvar_edicao():
    global item_selecionado

    if item_selecionado:  # Verifica se um item foi selecionado
        BD = sqlite3.connect("BD_GRE.db")
        terminal_sql = BD.cursor()
        nome_edit = editar_nome.get()
        preco_edit = editar_preco.get()
        desc_edit = editar_desc.get("1.0", "end")

        try:
            # Atualiza os dados do produto no banco de dados
            terminal_sql.execute(
                "UPDATE Produtos SET nomes = ?, precos = ?, desc = ? WHERE nomes = ?",
                (nome_edit, preco_edit, desc_edit, item_selecionado)
            )
            BD.commit()  # Salva as alterações
            print(f"Produto '{item_selecionado}' atualizado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao atualizar o produto: {e}")
        finally:
            BD.close()

        # Limpa os campos de edição
        editar_nome.delete(0, "end")
        editar_preco.delete(0, "end")
        editar_desc.delete("1.0", "end")

        # Atualiza a interface
        dados_edicao()
        ler_dados_cadastro()

        # Reseta o item selecionado
        item_selecionado = None
    else:
        print("Nenhum item selecionado para edição.")


def cancelar_edicao():
    global item_selelecionado
    item_selecionado = None
    limpar_campos_edicao()
    dados_edicao()
    ler_dados_cadastro()


def deletar_edicao():
    global item_selecionado

    if item_selecionado:  # Verifica se um item foi selecionado
        BD = sqlite3.connect("BD_GRE.db")
        terminal_sql = BD.cursor()
        # Exclui o produto do banco de dados
        terminal_sql.execute("DELETE FROM Produtos WHERE nomes = ?", (item_selecionado,))
        BD.commit() 
        BD.close()
        editar_nome.delete(0, "end")
        editar_preco.delete(0, "end")
        editar_desc.delete("1.0", "end")

        # Atualiza a interface
        dados_edicao()
        ler_dados_cadastro()

        # Reseta o item selecionado
        item_selecionado = None
    else:
        print("Nenhum item selecionado para exclusão.")



def pesquisar_produto_edicao(event=None):
    global item_selecionado, checkbox_selecionado
    var_nome = pesquisar_edicao.get()
    BD = sqlite3.connect("BD_GRE.db")
    terminal_sql = BD.cursor()
    terminal_sql.execute("SELECT nomes FROM Produtos WHERE nomes LIKE ?", ('%' + var_nome + '%',))
    recebe_pesquisa = terminal_sql.fetchall()
    for item in rolagem_edicao.winfo_children():
        item.destroy()

    for item in recebe_pesquisa:
        item_selecionado = item[0]
        Box_edicao = customtkinter.CTkCheckBox(rolagem_edicao, text=item, text_color="#8684EB", checkmark_color="#83A2EB", border_color="#83A2EB", variable=checkbox_selecionado, command=lambda n=item, v=checkbox_selecionado: checkbox_event(n, v) # Adiciona o evento ao checkbox
        )
        Box_edicao.pack(pady=5, padx=5, fill="x")


    BD.close()
var_nome = None

    



def dados_saida():
    BD = sqlite3.connect("BD_GRE.db")
    terminal_sql = BD.cursor()
    terminal_sql.execute("SELECT nomes FROM Produtos")
    recebe_dados = terminal_sql.fetchall()
    for item in rolagem_saida_checkbox.winfo_children():
        item.destroy()

    for item in recebe_dados:
        Box = customtkinter.CTkCheckBox(rolagem_saida_checkbox, text=item, text_color="#8684EB", checkmark_color="#83A2EB", border_color="#83A2EB")
        Box.pack(pady=5, padx=5, fill="x")
    BD.close()


def dados_entrada():
    BD = sqlite3.connect("BD_GRE.db")
    terminal_sql = BD.cursor()
    terminal_sql.execute("SELECT nomes FROM Produtos")
    recebe_dados = terminal_sql.fetchall()
    for item in rolagem_entrada_checkbox.winfo_children():
        item.destroy()

    for item in recebe_dados:
        box_edit = customtkinter.CTkCheckBox(rolagem_entrada_checkbox, text=item, text_color="#8684EB", checkmark_color="#83A2EB", border_color="#83A2EB")
        box_edit.pack(pady=5, padx=5, fill="x")
    BD.close()

criar_banco()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
 
janela =customtkinter.CTk()
janela.title("Gerenciamento")
janela.geometry('800x410')

checkbox_selecionado = customtkinter.BooleanVar()  # Armazena o checkbox atualmente selecionado

style = ttk.Style(master=janela)
style.theme_use('clam')
style.configure("Treeview", background="#3484F0", fieldbackground="#a9b9e3", foreground="black",rowheight=25, bordercolor="#83A2EB" )
style.configure("Treeview.Heading",background="#83A2EB",bakcground="Black", relief="flat")
style.map("Treeview.Heading",background=[('active', '#a399f9')])


########frames
quadro_menu =customtkinter.CTkFrame(master=janela, width=190, height=400, corner_radius=20, border_color='#83A2EB', border_width=2 )
quadro_menu.grid(row=0 , column=0, pady=5, padx=5)
quadro_menu.pack_propagate(False)
 
quadro_cadastro =customtkinter.CTkFrame(master=janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_cadastro.grid(row=0 , column=1, pady=5, padx=5)
quadro_cadastro.grid_propagate(False)

quadro_edicao = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_edicao.grid_propagate(False)
 
quadro_saida = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_saida.grid_propagate(False)
 
quadro_entrada = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_entrada.grid_propagate(False)
 
quadro_relatorio_estoque = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_relatorio_estoque.grid_propagate(False)

quadro_relatorio_entrada = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_relatorio_entrada.grid_propagate(False)

quadro_relatorio_saida = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2)
quadro_relatorio_saida.grid_propagate(False)


########frame menu
#label

label_principal_menu = customtkinter.CTkLabel(quadro_menu, text="GRE", font=("arial",20,"bold"), text_color="#8471EB", corner_radius= 30)
label_principal_menu.pack(pady=40)
 
# botões do frame cadastro
 
botao_cadastro = customtkinter.CTkButton(master=quadro_menu, corner_radius= 30, text='Cadastrar',fg_color="#83A2EB", command=tela_cadastro, text_color="black")
botao_cadastro.pack(pady=5)
 
botao_edicao =customtkinter.CTkButton(master=quadro_menu, corner_radius= 30, text='Editar',fg_color="#83A2EB", command=tela_edicao, text_color="black")
botao_edicao.pack(pady=5)
 
botao_saida = customtkinter.CTkButton(master=quadro_menu, corner_radius= 30,text='Saída',fg_color="#83A2EB",command=tela_saida, text_color="black")
botao_saida.pack(pady=5)
 
botao_entrada =customtkinter.CTkButton(master=quadro_menu, corner_radius= 30, text='Entrada',fg_color="#83A2EB", command=tela_entrada, text_color="black")
botao_entrada.pack(pady=5)
 
botao_relatorio =customtkinter.CTkButton(master=quadro_menu, corner_radius= 30,text='Relatório',fg_color="#83A2EB", command=tela_relatorio, text_color="black")
botao_relatorio.pack(pady=5)
 
 
########frame Cadastro
#labels frame cadastro

label_do_cadastro = customtkinter.CTkLabel(quadro_cadastro, text="Cadastro do produto", font=("arial",20,"bold"), text_color="#8684EB")
label_do_cadastro.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky ="ne")
 
label_nome_produto = customtkinter.CTkLabel(quadro_cadastro, text="Nome do produto:", text_color="#8684EB", corner_radius= 30)
label_nome_produto.grid(row = 1, column = 0, padx = 5, pady=5)
 
label_preco = customtkinter.CTkLabel(quadro_cadastro, text="Preço(R$):", text_color="#8684EB", corner_radius= 30)
label_preco.grid(row = 2, column = 0, padx = 5, pady=5 ,  sticky ="e")
 
label_desc = customtkinter.CTkLabel(quadro_cadastro, text="Descrição:", text_color="#8684EB", corner_radius= 30)
label_desc.grid(row = 3, column = 0, padx = 5, pady=5,  sticky ="en")
 

#entradas frame cadastro

entrada_nome_produto = customtkinter.CTkEntry(quadro_cadastro, placeholder_text="informe o nome do produto:", width=300, border_color= '#83A2EB', border_width=2, placeholder_text_color="#8684EB", corner_radius= 30)
entrada_nome_produto.grid(row = 1, column = 1, padx = 5, pady=5)
 
entrada_preco=customtkinter.CTkEntry(quadro_cadastro, placeholder_text="R$:(0.00)", width=80, border_color= '#83A2EB', border_width=2, placeholder_text_color="#8684EB", corner_radius= 30 )
entrada_preco.grid(row = 2, column = 1, padx = 5, pady=5, sticky ="w")


#textbox frame cadastro

textbox_desc=customtkinter.CTkTextbox(master=quadro_cadastro, width=300, height=80, border_color= '#83A2EB', border_width=2, corner_radius= 30)
textbox_desc.grid(row = 3, column = 1, padx = 5, pady=5)


#botões frame cadastro
 
botao_salvar = customtkinter.CTkButton(master=quadro_cadastro, corner_radius= 30, text='Salvar',fg_color="#83A2EB", text_color="black", command=salvar_cadastro)
botao_salvar.grid(row = 4, column = 1, padx = 5, pady=5, sticky ="e")
 
 
########frame Edição 
#label de edição
label_edicao = customtkinter.CTkLabel(quadro_edicao, text="Edição", font=("arial",20,"bold"), text_color="#8684EB")
label_edicao.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky ="n")


########tabela de busca de itens de edição
#itens de edição
 
rolagem_edicao = customtkinter.CTkScrollableFrame(quadro_edicao, width=200, border_color="#83A2EB", border_width=2, scrollbar_button_color="#83A2EB")
rolagem_edicao.grid(row=2, column=0, rowspan=4 , pady=10, padx=10)

## entrada para pesquisa
 
pesquisar_edicao = customtkinter.CTkEntry(quadro_edicao, placeholder_text="Pesquisar item", placeholder_text_color="#83A2EB", border_color="#83A2EB", border_width=2, width=230,)
pesquisar_edicao.grid(row=1, column=0, pady=10, padx=10, sticky="e")
pesquisar_edicao.bind("<KeyRelease>", pesquisar_produto_edicao)
 
## entradas de edição
 
editar_nome = customtkinter.CTkEntry(quadro_edicao, placeholder_text="Nome do Produto:", placeholder_text_color="#83A2EB", border_color="#83A2EB", border_width=2, width=320)
editar_nome.grid(row=2, column=1, pady=5, padx=5, sticky="w", columnspan=3,)
 
editar_preco = customtkinter.CTkEntry(quadro_edicao, placeholder_text="R$(0.00):", placeholder_text_color="#83A2EB", border_color="#83A2EB", border_width=2, width=80)
editar_preco.grid(row=3,column=1, pady=5, padx=5, sticky="w", columnspan=3,)
 
editar_desc = customtkinter.CTkTextbox(quadro_edicao, width=320, height=80, border_color= '#83A2EB', border_width=2)
editar_desc.grid(row=4, column=1, columnspan=4, pady=5, padx=5, sticky="w")
 
## botões
 
botao_cancelar_edicao = customtkinter.CTkButton(quadro_edicao, text="Cancelar", text_color="black", fg_color="#83A2EB", width=100, corner_radius=30, command=cancelar_edicao)
botao_cancelar_edicao.grid(row=5 , column=2, columnspan=1, pady=5, padx=5, sticky="w")
 
botao_enviar_edicao = customtkinter.CTkButton(quadro_edicao, text="Enviar", text_color="black", fg_color="#83A2EB", width=100, corner_radius=30, command=salvar_edicao)
botao_enviar_edicao.grid(row=5, column=3, columnspan=1, pady=5, padx=5, sticky="w")
 
botao_remover_edicao = customtkinter.CTkButton(quadro_edicao, text="Remover", text_color="black", fg_color="#83A2EB", width=100, corner_radius=30, command=deletar_edicao)
botao_remover_edicao.grid(row=5, column=1, columnspan=1, pady=5, padx=5, sticky="w")
 
 
########frame saida
#label de saida
label_saida = customtkinter.CTkLabel(quadro_saida, text="Saída de Produtos", font=("arial",20,"bold"), text_color="#8684EB")
label_saida.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky ="n")

##rolagem de itens saida
rolagem_saida_checkbox = customtkinter.CTkScrollableFrame(quadro_saida, width=200, border_color="#83A2EB", border_width=2, scrollbar_button_color="#83A2EB")
rolagem_saida_checkbox.grid(row=3, column=0, rowspan=4 , pady=5, padx=20)

#entrada de pesquisa da saida
pesquisar_saida = customtkinter.CTkEntry(quadro_saida, placeholder_text="Pesquisar item", placeholder_text_color="#8684EB", width=230, border_color="#83A2EB", border_width=2 )
pesquisar_saida.grid(row=1, column=0, rowspan=3, padx=5, sticky="s")


#entradas da saída 
nome_ret = customtkinter.CTkEntry(quadro_saida, placeholder_text="nome", placeholder_text_color="#8684EB", width=300, border_color="#83A2EB", border_width=2 )
nome_ret.grid(row=3, column=1, pady=2, padx=5, sticky="w")
 
nome_quant_estoque = customtkinter.CTkLabel(quadro_saida, text="produtos em estoque: 1")
nome_quant_estoque.grid(row=2, column=1, padx=5, sticky="n")
 
preco_saida = customtkinter.CTkEntry(quadro_saida, placeholder_text="0.00:", placeholder_text_color="#8684EB", width=100, border_color="#83A2EB", border_width=2 )
preco_saida.grid(row=4,column=1, pady=2, padx=5, sticky="w")

#botões do frame saida
 
botao_add_item_saida = customtkinter.CTkButton(quadro_saida, text="Adicionar item", text_color="black", width=110, fg_color="#83A2EB", command=adicionar_item_saida, corner_radius= 30)
botao_add_item_saida.grid(row=4, column=1, columnspan=2, pady=6, sticky="e") 
 
botao_cancel_saida = customtkinter.CTkButton(quadro_saida, text="Cancelar", text_color="black", width=100, fg_color="#83A2EB", corner_radius= 30)
botao_cancel_saida.grid(row=6, column=1, padx=1, sticky="n")
 
botao_salvar_saida = customtkinter.CTkButton(quadro_saida, text="Salvar", text_color="black", width=100, fg_color="#83A2EB", corner_radius= 30)
botao_salvar_saida.grid(row=6, column=1, padx=1, sticky="w")


#tabela de itens selecionados
 
rolagem_saida_selecao_itens = customtkinter.CTkScrollableFrame(quadro_saida)
rolagem_saida_selecao_itens.grid(row=5, column=1, columnspan=2, padx=5, sticky="w")

 
######## quadro entrada 
#label quadro entrada
 
label_entrada = customtkinter.CTkLabel(quadro_entrada, text="Entrada de produtos", font=("arial",20,"bold"), text_color="#8684EB")
label_entrada.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky ="n")

#tabela de busca do quadro entrada

rolagem_entrada_checkbox = customtkinter.CTkScrollableFrame(quadro_entrada, width=200, border_color="#83A2EB", border_width=2, scrollbar_button_color="#83A2EB")
rolagem_entrada_checkbox.grid(row=3, column=0, rowspan=5, padx=20)

 
pesquisar_entrada = customtkinter.CTkEntry(quadro_entrada, placeholder_text="Pesquisar item", placeholder_text_color="#8684EB", width=230, border_color="#83A2EB", border_width=2 )
pesquisar_entrada.grid(row=1, column=0, rowspan=3, padx=5, sticky="s")

 
nome_ent = customtkinter.CTkEntry(quadro_entrada, placeholder_text="nome", placeholder_text_color="#8684EB", width=300, border_color="#83A2EB", border_width=2 )
nome_ent.grid(row=3, column=1,pady=2 , padx=5, sticky="w")

 
nome_quant_estoque_entrada = customtkinter.CTkLabel(quadro_entrada, text="produtos em estoque: 1")
nome_quant_estoque_entrada.grid(row=2, column=1, padx=5, sticky="n")


preco_entrada = customtkinter.CTkEntry(quadro_entrada, placeholder_text="0.00:", placeholder_text_color="#8684EB", width=100, border_color="#83A2EB", border_width=2 )
preco_entrada.grid(row=4,column=1,pady=2 , padx=5, sticky="w")


#botões da entrada
botao_add_item_entrada = customtkinter.CTkButton(quadro_entrada, text="Adicionar item", text_color="black", width=110, fg_color="#83A2EB", command= adicionar_item_entrada, corner_radius= 30)
botao_add_item_entrada.grid(row=4, column=1, columnspan=2, padx= 6,sticky="e")

 
botao_cancel_entrada = customtkinter.CTkButton(quadro_entrada, text="Cancelar", text_color="black", width=100, fg_color="#83A2EB", corner_radius= 30)
botao_cancel_entrada.grid(row=6, column=1, padx=1, sticky="n")

 
botao_salvar_entrada = customtkinter.CTkButton(quadro_entrada, text="Salvar", text_color="black", width=100, fg_color="#83A2EB", corner_radius= 30)
botao_salvar_entrada.grid(row=6, column=1, padx=1, sticky="w")
 

#tabela da itens selecionados

rolagem_entrada_selecao_itens = customtkinter.CTkScrollableFrame(quadro_entrada)
rolagem_entrada_selecao_itens.grid(row=5, column=1, columnspan=2 , pady=5, padx=5, sticky="w")


######## quadro relatório estoque
#label relatorio
label_relatorio_estoque = customtkinter.CTkLabel(quadro_relatorio_estoque, text="Relatório Estoque", font=("arial",20,"bold"), text_color="#8684EB")
label_relatorio_estoque.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky ="ne")


#barra de pesquisa do relatorio de estoque
pesquisar_relatorio_estoque = customtkinter.CTkEntry(quadro_relatorio_estoque, placeholder_text="Pesquisar item", placeholder_text_color="#8684EB", width=170, border_color="#83A2EB", border_width=2 )
pesquisar_relatorio_estoque.grid(row=1, column=0, pady=5, padx=5, sticky="e", columnspan=2)


# tabela relatorio de estoque
colunas_estoque = ["Nome", "Quantidade", "Preço", "Descrição"]
tabela_relatorio_estoque = ttk.Treeview(quadro_relatorio_estoque, columns=colunas_estoque, show="headings", height=10)
tabela_relatorio_estoque.grid(row=2, column=0, columnspan=4, padx=50)

for coluna_estoque in colunas_estoque:
    tabela_relatorio_estoque.heading(coluna_estoque, text=coluna_estoque)
    tabela_relatorio_estoque.column(coluna_estoque, width=120, anchor="center")


#botões do relatorio de estoque
botao_estoque_do_estoque = customtkinter.CTkButton(quadro_relatorio_estoque, text="Relatorio Estoque", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=esconder_relatorio_entrada_saida)
botao_estoque_do_estoque.grid(row=3, column=1, pady=5, padx=5, sticky="w")


botao_entrada_do_estoque = customtkinter.CTkButton(quadro_relatorio_estoque, text="Relatorio Entrada", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command= esconder_relatorio_estoque_saida)
botao_entrada_do_estoque.grid(row=3, column=2, pady=5, padx=5, sticky="w")


botao_saida_do_estoque = customtkinter.CTkButton(quadro_relatorio_estoque, text="Relatorio Saída", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=esconder_relatorio_estoque_entrada)
botao_saida_do_estoque.grid(row=3, column=3, pady=5, padx=5, sticky="w")


botao_exportar_estoque = customtkinter.CTkButton(quadro_relatorio_estoque, text="Exportar", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=export)
botao_exportar_estoque.grid(row=1, column=3, pady=5, padx=5, sticky="w", columnspan=2 )


#relatorio da entrada
label_relatorio_entrada = customtkinter.CTkLabel(quadro_relatorio_entrada, text="Relatório Entrada", font=("arial",20,"bold"), text_color="#8684EB")
label_relatorio_entrada.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky ="ne")


#barra de pesquisa do relatorio da entrada
pesquisar_relatorio_entrada = customtkinter.CTkEntry(quadro_relatorio_entrada, placeholder_text="Pesquisar item", placeholder_text_color="#8684EB", width=170, border_color="#83A2EB", border_width=2 )
pesquisar_relatorio_entrada.grid(row=1, column=0, pady=5, padx=5, sticky ="e", columnspan=2)


# tabela relatorio da entrada
colunas_entrada = ["Nome", "Quantidade", "Data/Hora"]
tabela_relatorio_entrada = ttk.Treeview(quadro_relatorio_entrada, columns=colunas_entrada, show="headings", height=10 )
tabela_relatorio_entrada.grid(row=2, column=0, columnspan=4, sticky="n",padx=50)


for coluna_entrada in colunas_entrada:
    tabela_relatorio_entrada.heading(coluna_entrada, text=coluna_entrada)
    tabela_relatorio_entrada.column(coluna_entrada, width=160)


#botões

botao_estoque_da_entrada = customtkinter.CTkButton(quadro_relatorio_entrada, text="Relatorio Estoque", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=esconder_relatorio_entrada_saida)
botao_estoque_da_entrada.grid(row=3, column=1, pady=5, padx=5, sticky="w")


botao_entrada_da_entrada = customtkinter.CTkButton(quadro_relatorio_entrada, text="Relatorio Entrada", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=esconder_relatorio_estoque_saida)
botao_entrada_da_entrada.grid(row=3, column=2, pady=5, padx=5, sticky="w")


botao_saida_da_entrada = customtkinter.CTkButton(quadro_relatorio_entrada, text="Relatorio Saída", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=esconder_relatorio_estoque_entrada)
botao_saida_da_entrada.grid(row=3, column=3, pady=5, padx=5, sticky="w")


botao_exportar_entrada = customtkinter.CTkButton(quadro_relatorio_entrada, text="Exportar", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=export)
botao_exportar_entrada.grid(row=1, column=3, pady=5, padx=5, sticky="w")


#relatorio da saida
label_relatorio_saida = customtkinter.CTkLabel(quadro_relatorio_saida, text="Relatório Saída", font=("arial",20,"bold"), text_color="#8684EB")
label_relatorio_saida.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky ="ne")


#barra de pesquisa do relatorio de saida
pesquisar_relatorio_saida = customtkinter.CTkEntry(quadro_relatorio_saida, placeholder_text="Pesquisar item", placeholder_text_color="#8684EB", width=170, border_color="#83A2EB", border_width=2 )
pesquisar_relatorio_saida.grid(row=1, column=0, pady=5, padx=5, sticky="e", columnspan=2)


#tabela do relatorio de saida
colunas_saida = ["Nome", "Quantidade", "Data/Hora"]
tabela_relatorio_saida= ttk.Treeview(quadro_relatorio_saida, columns=colunas_saida, show="headings", height=10 )
tabela_relatorio_saida.grid(row=2, column=0, columnspan=4, sticky="n", padx=50)


for coluna_saida in colunas_saida:
    tabela_relatorio_saida.heading(coluna_saida, text=coluna_saida)
    tabela_relatorio_saida.column(coluna_saida, width=160)


#botões do relatorio de saida

botao_estoque_da_saida = customtkinter.CTkButton(quadro_relatorio_saida, text="Relatorio Estoque", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=esconder_relatorio_entrada_saida)
botao_estoque_da_saida.grid(row=3, column=1, pady=5, padx=5, sticky="w")


botao_entrada_da_saida = customtkinter.CTkButton(quadro_relatorio_saida, text="Relatorio Entrada", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=esconder_relatorio_estoque_saida)
botao_entrada_da_saida.grid(row=3, column=2, pady=5, padx=5, sticky="w")


botao_saida_da_saida = customtkinter.CTkButton(quadro_relatorio_saida, text="Relatorio Saída", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=esconder_relatorio_estoque_entrada)
botao_saida_da_saida.grid(row=3, column=3, pady=5, padx=5, sticky="w")


botao_exportar_saida = customtkinter.CTkButton(quadro_relatorio_saida, text="Exportar", text_color="black", width=110, fg_color="#83A2EB", corner_radius= 30, command=export)
botao_exportar_saida.grid(row=1, column=3, pady=5, padx=5, sticky="w", columnspan=2)


janela.mainloop()
