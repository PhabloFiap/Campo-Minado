from tkinter import *  
import settings
import util

root = Tk() #instanciando um objeto pois sera uma janela
root.configure(bg="black") #pintando o fundo
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') #tamanho da janela
root.title("Campo minado")
root.resizable(False, False) #nao redimensionavel

top_frame = Frame (
    root,
    bg= 'red', #vamos mudar mais tarde
     width=settings.WIDTH,
     height= util.height_prct(25)
)
top_frame.place(x=0, y=0) #mapeando a parte superior

left_frame = Frame (
    root,
    bg='blue',#vamos mudar mais tarde tambem
    width=util.width_prct(25),
    height=util.height_prct(75)
)
left_frame.place (x=0, y=util.height_prct(25)) #quero iniciar logo apos o quadrado superior


center_frame = Frame (
    root,
    bg='green', 
    width=util.width_prct(75),
    height=util.height_prct(75)
)

center_frame.place(
    x=util.width_prct(25),
    y=util.height_prct(25)

)

root.mainloop()