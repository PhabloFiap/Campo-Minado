from tkinter import *  

root = Tk() #instanciando um objeto pois sera uma janela
root.configure(bg="black") #pintando o fundo
root.geometry('1220x720') #tamanho da janela
root.title("Campo minado")
root.resizable(False, False) #nao redimensionavel

top_frame = Frame (
    root,
    bg= 'red', #vamos mudar mais tarde
     width=1220,
     height= 180
)
top_frame.place(x=0, y=0) #mapeando a parte superior

left_frame = Frame (
    root,
    bg='blue',#vamos mudar mais tarde tambem
    width=305,
    height=540
)
left_frame.place (x=0, y=180)

root.mainloop()