from tkinter import *  
from cell import Cell
import settings
import util

root = Tk() #instanciando um objeto pois sera uma janela
root.configure(bg="black") #pintando o fundo
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') #tamanho da janela
root.title("Campo minado")
root.resizable(False, False) #nao redimensionavel

top_frame = Frame (
    root,
    bg= 'black',
     width=settings.WIDTH,
     height= util.height_prct(25)
)
top_frame.place(x=0, y=0) #mapeando a parte superior

left_frame = Frame (
    root,
    bg='black',
    width=util.width_prct(25),
    height=util.height_prct(75)
)
left_frame.place (x=0, y=util.height_prct(25)) #quero iniciar logo apos o quadrado superior


center_frame = Frame (
    root,
    bg='black', 
    width=util.width_prct(75),
    height=util.height_prct(75)
)

center_frame.place(
    x=util.width_prct(25),
    y=util.height_prct(25)

)
#toda a parte de frame esta acima


for i in range (settings.GRID_SIZE):
    for j in range (settings.GRID_SIZE):
        c = Cell(i,j)
        c.cria_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=i, row=j 
        )


Cell.randomize_mines()

root.mainloop()