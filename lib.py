import customtkinter as ctk

def exibetitulo(frame_titulo, texto_titulo):
    lb_tiulo = ctk.CTkLabel(
        master=frame_titulo,
        text=texto_titulo,
        font=('Arial',20,'bold'),
        text_color="white"
         )
    
    lb_tiulo.place(relx=0.5, rely=0.5, anchor='center')

    return lb_tiulo

def exiberesultado(frame_resultado, horx, verty, texto, valor, cor):
    if (cor == 'azul'):
        cor1 = '#008B8B'
        cor2 = "#008B8B"
    elif (cor == 'preto'):
        cor1 = "#000000"
        cor2 = "#606060"
    elif (cor == 'vermelho'):
        cor1 = "#F35317"
        cor2 = "#F34317"
    elif (cor == 'verde'):
        cor1 = "#5DF317"
        cor2 = "#31F317"
    elif (cor == 'amarelo'):
        cor1 = "#F3D217"
        cor2 = "#D2F317"     
    else:
        cor1 = "#00F7FF"
        cor2 = '#00F7FF'
    frexibe = ctk.CTkFrame(frame_resultado, width=250, height=31,fg_color=cor1 ,border_width=2, corner_radius=0)
    frexibe.place(x=horx, y=verty)
    #frame do frame texto

    ltexto = ctk.CTkLabel(frame_resultado, text=texto, font=('Arial', 14),text_color="#FFFFFF", fg_color=cor1, width=200, anchor='w' )
    ltexto.place(x=horx+2, y=verty+2)
     
    lvalor = ctk.CTkLabel(frame_resultado, text=f"R$ {valor:.2f}",text_color="#FFFFFF" ,font=('Arial', 12), fg_color=cor2, width=79)
    lvalor.place(x=horx+170, y=verty+2)


def exiberesultadoimc(frame_imc, horx, verty, texto, valor, cor):
    if (cor == 'azul'):
        cor1 = '#008B8B'
        cor2 = "#008B8B"
    elif (cor == 'vermelho'):
        cor1 = "#F35317"
        cor2 = "#F34317"
    elif (cor == 'verde'):
        cor1 = "#5DF317"
        cor2 = "#31F317"
    elif (cor == 'amarelo'):
        cor1 = "#F3D217"
        cor2 = "#D2F317"
    elif (cor == 'branco'):
        cor1 = "#FFFFFF"
        cor2 = "#FFFFFF"           
    else:
        cor1 = "#DF6161"
        cor2 = "#FFFFFF"
    frexibe = ctk.CTkFrame(frame_imc, width=250, height=31,fg_color=cor1 ,border_width=2, corner_radius=0)
    frexibe.place(x=horx, y=verty)
    #frame do frame texto

    imctexto = ctk.CTkLabel(frame_imc, text=texto, font=('Arial', 14),text_color="#000000", fg_color=cor1, width=200, anchor='w' )
    imctexto.place(x=horx+2, y=verty+2)
     
    imcvalor = ctk.CTkLabel(frame_imc, text=f" {valor:.2f}",text_color="#000000" ,font=('Arial', 12), fg_color=cor2, width=79)
    imcvalor.place(x=horx+170, y=verty+2)

def acessadados(frame_acess, hoex, very, texto, valor):
    ldados = ctk.CTkLabel(frame_acess, text=texto, font=('Arial',12))
    ldados.place(x=hoex, y=very)
    acess = ctk.StringVar(value=valor)
    eacess = ctk.CTkEntry(frame_acess, textvariable=acess, width=100)
    eacess.place(x=hoex+140, y= very) 
    return(eacess)

def acess_radio(frame_radio, hoex, verty, texto, opcoes, opcoes_s):
    lradio= ctk.CTkLabel(frame_radio, text=texto, font=('Arial',12))
    lradio.place(x=hoex, y=verty)

    distancia = 130

    for opcao in opcoes:
        rb = ctk.CTkRadioButton(frame_radio, text=opcao, variable=opcoes_s, value=opcao)
        rb.place(x=hoex + distancia, y=verty)
        distancia += 110

    return opcoes_s

def list_box(frame_combo, hoex, verty, texto, list_opcoes):
    lcombolb = ctk.CTkLabel(frame_combo, text=texto, font=('Arial',12))
    lcombolb.place(x=hoex, y=verty)

    cb = ctk.CTkComboBox(frame_combo, values=list_opcoes, width=200)
    cb.place(x=hoex + 130, y=verty)
    cb.set(list_opcoes[0])

    return cb