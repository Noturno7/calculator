from tkinter import *
from tkinter import ttk
from turtle import right

cor1="#050505" # preto
cor2="#C68714" # laranja
cor3="#EFEFEF" # branco
cor4="#CE0E2B" # vermelho
cor5="#615F5F" # cinza

janela =Tk()
janela.title("calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50,)  
frame_tela.grid(row=0, column=0)
frame_tela.config(bg=cor2)

frame_quadro = Frame(janela, width=235, height=268,)  
frame_quadro.grid(row=1, column=0)

#todos valores variavel

todos_valores = ''
valor_texto=StringVar()


#função
def entrar_valores(event):
    global todos_valores 

    todos_valores = todos_valores + str(event)

    #tela
    valor_texto.set(todos_valores)

#calculo
def calcular():
    global todos_valores
    resultado = eval (todos_valores)
    
    valor_texto.set(str(resultado))


#limpar tela
def limpar_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")

        

#label
app_label =Label(frame_tela,textvariable=valor_texto , width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT,font=('Ivy 18'), bg=cor2, fg=cor3)
app_label.place(x=0,y=0)



#botoes

B_1 = Button(frame_quadro,command = limpar_tela, text="C", width=11, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_1.place(x=0, y=0)
B_2 = Button(frame_quadro, command = lambda: entrar_valores ('%'), text="%", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_2.place(x=120, y=0)
B_3 = Button(frame_quadro, command = lambda: entrar_valores ('/'),text="/", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_3.place(x=175, y=0)

B_7 = Button(frame_quadro,command = lambda: entrar_valores ('7'), text="7", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_7.place(x=0, y=54)
B_E = Button(frame_quadro,command = lambda: entrar_valores ('8'), text="8", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_E.place(x=60, y=54)
B_9 = Button(frame_quadro, command = lambda: entrar_valores ('9'),text="9", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_9.place(x=120, y=54)
B_8 = Button(frame_quadro,command = lambda: entrar_valores ('*'), text="*", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_8.place(x=175, y=54)

B_4 = Button(frame_quadro, command = lambda: entrar_valores ('4'),text="4", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_4.place(x=0, y=108)
B_5 = Button(frame_quadro,command = lambda: entrar_valores ('5'), text="5", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_5.place(x=60, y=108)
B_6 = Button(frame_quadro,command = lambda: entrar_valores ('6'), text="6", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_6.place(x=120, y=108)
B_F = Button(frame_quadro,command = lambda: entrar_valores ('-'), text="-", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_F.place(x=175, y=108)

B_10 = Button(frame_quadro,command = lambda: entrar_valores ('1'), text="1", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_10.place(x=0, y=162)
B_11 = Button(frame_quadro,command = lambda: entrar_valores ('2'), text="2", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_11.place(x=60, y=162)
B_12 = Button(frame_quadro,command = lambda: entrar_valores ('3'), text="3", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_12.place(x=120, y=162)
B_13 = Button(frame_quadro,command = lambda: entrar_valores ('+'), text="+", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_13.place(x=175, y=162)

B_14 = Button(frame_quadro,command = lambda: entrar_valores ('0'), text="0", width=11, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_14.place(x=0, y=216)
B_15 = Button(frame_quadro,command = lambda: entrar_valores ('.'), text=".", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_15.place(x=120, y=216)
B_16 = Button(frame_quadro, command = calcular ,text="=", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B_16.place(x=175, y=216)




janela.mainloop()