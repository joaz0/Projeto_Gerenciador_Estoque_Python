import  customtkinter
from PIL import Image
import os
from  tkinter import messagebox
 
file_path = os.path.dirname(os.path.realpath(__file__))
imagem1 = customtkinter.CTkImage(Image.open(fp="C:/Users/970973/OneDrive - SENAC em Minas - EDU\Documentos/atv_commit/UC5/UC5_Exercicios/Projetos/image/lixeira 1.png"), size=(35,35))
item_vet = 0
 
def tela_cadastro():
    quadro_cadastro.grid(row=0 , column=1, pady=5, padx=5)
    quadro_cadastro.grid_propagate(False)
    quadro_edicao.grid_forget()
    quadro_saida.grid_forget()
    quadro_entrada.grid_forget()
    quadro_relatorio.grid_forget()
   
 
def tela_edicao():
    quadro_edicao.grid(row=0 , column=1, pady=5, padx=5)
    quadro_edicao.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_saida.grid_forget()
    quadro_entrada.grid_forget()
    quadro_relatorio.grid_forget()
 
def tela_saida():
    quadro_saida.grid(row=0 , column=1, pady=5, padx=5)
    quadro_saida.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_edicao.grid_forget()
    quadro_entrada.grid_forget()
    quadro_relatorio.grid_forget()
 
def tela_entrada():
    quadro_entrada.grid(row=0 , column=1, pady=5, padx=5)
    quadro_entrada.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_edicao.grid_forget()
    quadro_saida.grid_forget()
    quadro_relatorio.grid_forget()
 
def tela_relatorio() :
    quadro_relatorio.grid(row=0 , column=1, pady=5, padx=5)
    quadro_relatorio.grid_propagate(False)
    quadro_cadastro.grid_forget()
    quadro_saida.grid_forget()
    quadro_entrada.grid_forget()
    quadro_edicao.grid_forget()
 
def delete_itens_saida(linhas, botoes):
    linhas.grid_forget()
    botoes.grid_forget()
   
   
linha_saida = 0
def adicionar_item_saida():  
    global linha_saida
    item_vet_saida = str(nome_ret.get())
    linha_saida += 1
 
    if item_vet_saida in itens_saida1:    
        try :  
            label_saida = customtkinter.CTkLabel(rolagem_saida2, text=item_vet_saida)            
            label_saida.grid(row=linha_saida, column=0, pady=5, padx=5, sticky = "w")    
            lixeira_saida = customtkinter.CTkButton(rolagem_saida2, width=35, height=35, text="", image=imagem1, command=lambda: delete_itens_saida(label_saida, lixeira_saida))
            lixeira_saida.grid(row=linha_saida, column=1, pady=5, padx=100, sticky = "e")
 
        except ValueError:
            return  
 
 
def delete_itens_entrada(linhas_entrada, botoes_entrada):
    linhas_entrada.grid_forget()
    botoes_entrada.grid_forget()
   
   
linha_entrada = 0
def adicionar_item_entrada():  
    global linha_entrada
    item_vet_entrada = str(nome_ent.get())
    linha_entrada += 1
 
    if item_vet_entrada in itens_entrada1:    
        try :  
            label_entrada = customtkinter.CTkLabel(rolagem_entrada2, text=item_vet_entrada)            
            label_entrada.grid(row=linha_entrada, column=0, pady=5, padx=5, sticky = "w")    
            lixeira_entrada = customtkinter.CTkButton(rolagem_saida2, width=35, height=35, text="", image=imagem1, command=lambda: delete_itens_entrada(label_entrada, lixeira_entrada))
            lixeira_entrada.grid(row=linha_entrada, column=1, pady=5, padx=100, sticky = "e")
 
        except ValueError:
            return  
 
 
##for item_vet in itens_saida1:
 
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
 
janela =customtkinter.CTk()
janela.title("Gerenciamento")
janela.geometry('800x410')
 
quadro =customtkinter.CTkFrame(master=janela, width=190, height=400, corner_radius=20, border_color='#83A2EB', border_width=2 )
quadro.grid(row=0 , column=0, pady=5, padx=5)
quadro.pack_propagate(False)
 
quadro_cadastro =customtkinter.CTkFrame(master=janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_cadastro.grid(row=0 , column=1, pady=5, padx=5)
quadro_cadastro.grid_propagate(False)
 
quadro_edicao = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
 
quadro_edicao.grid_propagate(False)
 
quadro_saida = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_saida.grid_propagate(False)
 
quadro_entrada = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_entrada.grid_propagate(False)
 
quadro_relatorio = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, border_color= '#83A2EB', border_width=2 )
quadro_relatorio.grid_propagate(False)
 
 
 
 
#frame 01
 
label_principal = customtkinter.CTkLabel(quadro, text="Nome do sistema", font=("arial",20,"bold"), text_color="#8471EB")
label_principal.pack(pady=40)
 
# botões
 
botao_cadastro = customtkinter.CTkButton(master=quadro, corner_radius= 10, text='Cadastrar',fg_color="#83A2EB", command=tela_cadastro, text_color="black")
botao_cadastro.pack(pady=5)
 
botao_edicao =customtkinter.CTkButton(master=quadro, corner_radius= 10, text='Editar',fg_color="#83A2EB", command=tela_edicao, text_color="black")
botao_edicao.pack(pady=5)
 
botao_saida = customtkinter.CTkButton(master=quadro, corner_radius= 10,text='Saída',fg_color="#83A2EB",command=tela_saida, text_color="black")
botao_saida.pack(pady=5)
 
botao_entrada =customtkinter.CTkButton(master=quadro, corner_radius= 10, text='Entrada',fg_color="#83A2EB", command=tela_entrada, text_color="black")
botao_entrada.pack(pady=5)
 
botao_relatorio =customtkinter.CTkButton(master=quadro, corner_radius= 10,text='Relatório',fg_color="#83A2EB", command=tela_relatorio, text_color="black")
botao_relatorio.pack(pady=5)
 
 
 
 
#frame 02
 
label_do_cadastro = customtkinter.CTkLabel(quadro_cadastro, text="Cadastro do produto", font=("arial",20,"bold"), text_color="#8684EB")
label_do_cadastro.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky ="n")
 
label_nome_produto = customtkinter.CTkLabel(quadro_cadastro, text="Nome do produto:", text_color="#8684EB")
label_nome_produto.grid(row = 1, column = 0, padx = 5, pady=5)
 
entrada_nome_produto = customtkinter.CTkEntry(quadro_cadastro, placeholder_text="informe o nome do produto:", width=300, border_color= '#83A2EB', border_width=2, placeholder_text_color="#8684EB")
entrada_nome_produto.grid(row = 1, column = 1, padx = 5, pady=5)
 
label_preco = customtkinter.CTkLabel(quadro_cadastro, text="Preço(R$):", text_color="#8684EB")
label_preco.grid(row = 2, column = 0, padx = 5, pady=5 ,  sticky ="e")
 
entrada_preco=customtkinter.CTkEntry(quadro_cadastro, placeholder_text="R$:(0.00)", width=80, border_color= '#83A2EB', border_width=2, placeholder_text_color="#8684EB" )
entrada_preco.grid(row = 2, column = 1, padx = 5, pady=5, sticky ="w")
 
label_desc = customtkinter.CTkLabel(quadro_cadastro, text="Descrição:", text_color="#8684EB")
label_desc.grid(row = 3, column = 0, padx = 5, pady=5,  sticky ="en")
 
textbox_desc=customtkinter.CTkTextbox(master=quadro_cadastro, width=300, height=80, border_color= '#83A2EB', border_width=2)
textbox_desc.grid(row = 3, column = 1, padx = 5, pady=5)
 
botao_salvar = customtkinter.CTkButton(master=quadro_cadastro, corner_radius= 20, text='Salvar',fg_color="#83A2EB", text_color="black")
botao_salvar.grid(row = 4, column = 1, padx = 5, pady=5, sticky ="e")
 
 
 
 
# frame 3
label_edicao = customtkinter.CTkLabel(quadro_edicao, text="Edição", font=("arial",20,"bold"), text_color="#8684EB")
label_edicao.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky ="n")
 
# tabela
 
items = ["Item 1", "Item 2", "Item 3", "Item 4","Item 5", "Item 6", "Item 7", "Item 8"]
 
rolagem = customtkinter.CTkScrollableFrame(quadro_edicao, width=200, border_color="#83A2EB", border_width=2, scrollbar_button_color="#83A2EB")
rolagem.grid(row=2, column=0, rowspan=4 , pady=10, padx=10)
 
for item in items:  
    Box = customtkinter.CTkCheckBox(rolagem, text=item, text_color="#8684EB", checkmark_color="#83A2EB", border_color="#83A2EB")
    Box.pack(pady=5, padx=5, fill="x")
 
# entrada para pesquisa
 
pesquisar_edicao = customtkinter.CTkEntry(quadro_edicao, placeholder_text="Pesquisar item", placeholder_text_color="#83A2EB", border_color="#83A2EB", border_width=2, width=230)
pesquisar_edicao.grid(row=1, column=0, pady=10, padx=10, sticky="e")
 
# entradas de edição
 
editar_nome = customtkinter.CTkEntry(quadro_edicao, placeholder_text="Nome do Produto:", placeholder_text_color="#83A2EB", border_color="#83A2EB", border_width=2, width=320)
editar_nome.grid(row=2, column=1, pady=5, padx=5, sticky="w", columnspan=3,)
 
editar_preco = customtkinter.CTkEntry(quadro_edicao, placeholder_text="R$(0.00):", placeholder_text_color="#83A2EB", border_color="#83A2EB", border_width=2, width=80)
editar_preco.grid(row=3,column=1, pady=5, padx=5, sticky="w", columnspan=3,)
 
editar_desc = customtkinter.CTkTextbox(quadro_edicao, width=320, height=80, border_color= '#83A2EB', border_width=2)
editar_desc.grid(row=4, column=1, columnspan=3, pady=5, padx=5, sticky="w")
 
# botões
 
botao_cancelar = customtkinter.CTkButton(quadro_edicao, text="Cancelar", text_color="black", fg_color="#83A2EB", width=100)
botao_cancelar.grid(row=5 , column=2, columnspan=1, pady=5, padx=5, sticky="w")
 
botao_enviar = customtkinter.CTkButton(quadro_edicao, text="Enviar", text_color="black", fg_color="#83A2EB", width=100)
botao_enviar.grid(row=5, column=3, columnspan=1, pady=5, padx=5, sticky="w")
 
botao_remover = customtkinter.CTkButton(quadro_edicao, text="Remover", text_color="black", fg_color="#83A2EB", width=100)
botao_remover.grid(row=5, column=1, columnspan=1, pady=5, padx=5, sticky="w")
 
 
 
 
#frame 4
label_saida = customtkinter.CTkLabel(quadro_saida, text="Saída de Produtos", font=("arial",20,"bold"), text_color="#8684EB")
label_saida.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky ="n")
 
 
#tabela de busca
 
itens_saida1 = ["Item 1", "Item 2", "Item 3", "Item 4","Item 5", "Item 6", "Item 7", "Item 8"]
 
rolagem_saida1 = customtkinter.CTkScrollableFrame(quadro_saida, width=200, border_color="#83A2EB", border_width=2, scrollbar_button_color="#83A2EB")
rolagem_saida1.grid(row=3, column=0, rowspan=4 , pady=5, padx=20)
 
for item1 in itens_saida1:  
    box_saida1 = customtkinter.CTkCheckBox(rolagem_saida1, text=item1, text_color="#8684EB", checkmark_color="#83A2EB", border_color="#83A2EB", border_width=2)
    box_saida1.pack(pady=5, padx=5, fill="x")
 
 
pesquisar_saida = customtkinter.CTkEntry(quadro_saida, placeholder_text="Pesquisar item", placeholder_text_color="#8684EB", width=170, border_color="#83A2EB", border_width=2 )
pesquisar_saida.grid(row=1, column=0, rowspan=3, pady=5, padx=5, sticky="n")
 
nome_ret = customtkinter.CTkEntry(quadro_saida, placeholder_text="nome", placeholder_text_color="#8684EB", width=130, border_color="#83A2EB", border_width=2 )
nome_ret.grid(row=3, column=1, pady=5, padx=5, sticky="w")
 
nome_quant_estoque = customtkinter.CTkLabel(quadro_saida, text="produtos em estoque: 1")
nome_quant_estoque.grid(row=2, column=1, pady=5, padx=5, sticky="n")
 
#botões
 
butao_add_item_saida = customtkinter.CTkButton(quadro_saida, text="Adicionar item", text_color="black", width=110, fg_color="#83A2EB", command= adicionar_item_saida)
butao_add_item_saida.grid(row=3, column=2, columnspan=2, pady=5, sticky="n")
 
butao_cancel_saida = customtkinter.CTkButton(quadro_saida, text="Cancelar", text_color="black", width=100, fg_color="#83A2EB")
butao_cancel_saida.grid(row=5, column=1, pady=5, padx=1, sticky="n")
 
butao_salvar_saida = customtkinter.CTkButton(quadro_saida, text="Salvar", text_color="black", width=100, fg_color="#83A2EB")
butao_salvar_saida.grid(row=5, column=2, pady=5, padx=1, sticky="w")
 
#tabela de itens selecionados
 
rolagem_saida2 = customtkinter.CTkScrollableFrame(quadro_saida)
rolagem_saida2.grid(row=4, column=1, columnspan=2 , pady=5, padx=5, sticky="w")
 
 
 
 
#frame 5
 
label_entrada = customtkinter.CTkLabel(quadro_entrada, text="Entrada de produtos", font=("arial",20,"bold"), text_color="#8684EB")
label_entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky ="n")
 
#tabela de busca
 
itens_entrada1 = ["Item 1", "Item 2", "Item 3", "Item 4","Item 5", "Item 6", "Item 7", "Item 8"]
 
rolagem_entrada1 = customtkinter.CTkScrollableFrame(quadro_entrada, width=200, border_color="#83A2EB", border_width=2, scrollbar_button_color="#83A2EB")
rolagem_entrada1.grid(row=3, column=0, rowspan=4 , pady=5, padx=20)
 
for item1 in itens_entrada1:  
    box_entrada1 = customtkinter.CTkCheckBox(rolagem_entrada1, text=item1, text_color="#8684EB", checkmark_color="#83A2EB", border_color="#83A2EB", border_width=2)
    box_entrada1.pack(pady=5, padx=5, fill="x")
 
 
pesquisar_entrada = customtkinter.CTkEntry(quadro_entrada, placeholder_text="Pesquisar item", placeholder_text_color="#8684EB", width=170, border_color="#83A2EB", border_width=2 )
pesquisar_entrada.grid(row=1, column=0, rowspan=3, pady=5, padx=5, sticky="n")
 
nome_ent = customtkinter.CTkEntry(quadro_entrada, placeholder_text="nome", placeholder_text_color="#8684EB", width=130, border_color="#83A2EB", border_width=2 )
nome_ent.grid(row=3, column=1, pady=5, padx=5, sticky="w")
 
nome_quant_estoque_entrada = customtkinter.CTkLabel(quadro_entrada, text="produtos em estoque: 1")
nome_quant_estoque_entrada.grid(row=2, column=1, pady=5, padx=5, sticky="n")
 
#botões
 
butao_add_item_entrada = customtkinter.CTkButton(quadro_entrada, text="Adicionar item", text_color="black", width=110, fg_color="#83A2EB", command= adicionar_item_entrada)
butao_add_item_entrada.grid(row=3, column=2, columnspan=2, pady=5, sticky="n")
 
butao_cancel_entrada = customtkinter.CTkButton(quadro_entrada, text="Cancelar", text_color="black", width=100, fg_color="#83A2EB")
butao_cancel_entrada.grid(row=5, column=1, pady=5, padx=1, sticky="n")
 
butao_salvar_entrada = customtkinter.CTkButton(quadro_entrada, text="Salvar", text_color="black", width=100, fg_color="#83A2EB")
butao_salvar_entrada.grid(row=5, column=2, pady=5, padx=1, sticky="w")
 
#tabela de itens selecionados
 
rolagem_entrada2 = customtkinter.CTkScrollableFrame(quadro_entrada)
rolagem_entrada2.grid(row=4, column=1, columnspan=2 , pady=5, padx=5, sticky="w")
 
 
 
 
# frame 6
label_relatorio = customtkinter.CTkLabel(quadro_relatorio, text="relatório", font=("arial",20,"bold"), text_color="#8684EB")
label_relatorio.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky ="n")
 
janela.mainloop()
 