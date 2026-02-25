# Valor do Emprestimo 				
# Numero de prestações			
# Percentual de Juros			
					
# Juros Simples = Multiplica o valor * n° de prestações * juros					
# Valor do montante: Emprestimo + juros		
# Valor da prestação: Montante / prestações		

# juros compostos = valor + valor * percentual de juros

# preparação de tela --------------------------------------------------------------------

import customtkinter as ctk # importa a biblioteca que será utilizada e cria um apelido

ctk.set_appearance_mode('dark') # estabelece o modo de tela
app = ctk.CTk() # inicia a biblioteca e suas funções
app.title('Cálculo de Juros') # cria o nome do titulo
app.geometry('700x500') # especifica as medidas da tela
app.configure(fg_color = 'black') # estabelece a cor do fundo

# funções -------------------------------------------------------------------------------

def calculajuros ():
    vvaloremp = float(valoremp.get().replace(',', '.')) # Pega o valor que está em string na variável e transforma em decimal
    vprestacoes = int(prestacoes.get().replace(',', '.')) # Pega o valor que está em string na variável e transforma em inteiro
    vpercentual = float(percentual.get().replace(',', '.')) # Pega o valor que está em string na variável e transforma em decimal

    jurosimples = vvaloremp * vprestacoes * vpercentual

# objetos -------------------------------------------------------------------------------

# frame geral
fdados = ctk.CTkFrame(app, width=680, height= 480, border_width=2, fg_color= '#1C1D1D')
fdados.place(x=10, y=10)

# frame titulo
ftitulo = ctk.CTkFrame(fdados, width=200, height= 50, border_width=2, fg_color= '#1C1D1D')
ftitulo.place(x=240, y=10)

# titulo principal
ltitulo = ctk.CTkLabel(ftitulo, text='Cálculo de Juros ', font=('Arial', 22))
ltitulo.place(x = 20, y = 10)

# valor do emprestimo 

lvaloremp= ctk.CTkLabel(fdados, text='Valor do empréstimo: ', font=('Arial', 18))
lvaloremp.place(x = 10, y = 70)

valoremp = ctk.StringVar()
evaloremp = ctk.CTkEntry(fdados, textvariable = valoremp, width = 120)
evaloremp.place(x = 190, y = 70)

# numero de prestacoes

lprestacoes= ctk.CTkLabel(fdados, text='N° de prestações: ', font=('Arial', 18))
lprestacoes.place(x = 10, y = 110)

prestacoes = ctk.StringVar()
eprestacoes = ctk.CTkEntry(fdados, textvariable = valoremp, width = 120)
eprestacoes.place(x = 190, y = 110)

# percentual de juros

lpercentual= ctk.CTkLabel(fdados, text='Percentual de juros: ', font=('Arial', 18))
lpercentual.place(x = 10, y = 150)

percentual = ctk.StringVar()
epercentual = ctk.CTkEntry(fdados, textvariable = valoremp, width = 120)
epercentual.place(x = 190, y = 150)

#  botao para executar e fechar
bexecuta = ctk.CTkButton(fdados, text='Executa', width=200,font= ('Arial', 16) # command = executa 
)
bexecuta.place(x = 470, y = 70)

bfecha = ctk.CTkButton(fdados, text='Fecha', width=200, font= ('Arial', 16), fg_color= "#AA0000", hover_color= "#AA0000", command = app.destroy)
bfecha.place(x= 470, y = 110)

# frame do resultado
fresultado = ctk.CTkFrame (fdados, width=660, height= 260, border_width=2, fg_color="#555555")
fresultado.place(x = 10, y = 210)

# execução ------------------------------------------------------------------------------
app.mainloop()