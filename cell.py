from tkinter import Button
import random
import settings


class Cell:
    all =[]
    def __init__(self,i,j, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.i = i 
        self.j = j

        #criar um objeto ao Cell para lista "All"
        Cell.all.append(self)

    def cria_btn_object (self, location):#saber a localizacao do meu botao
        btn = Button(
            location,
            width=12,
            height=4,



        )
        btn.bind('<Button-1>',self.botao_esquerdo_click)
        btn.bind('<Button-3>',self.botao_direito_click)
        self.cell_btn_object = btn

    def botao_esquerdo_click(self, evento):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def pega_celula_por_eixo (self, i,j):
        for cell in Cell.all:
            if cell.i == i and cell.j == j:
                return cell

    @property
    def lista_de_celulas (self):
         celula = [
            self.pega_celula_por_eixo(self.i -1, self.j -1),
            self.pega_celula_por_eixo(self.i -1, self.j),
            self.pega_celula_por_eixo(self.i -1, self.j +1),

            self.pega_celula_por_eixo(self.i , self.j -1),

            self.pega_celula_por_eixo(self.i +1, self.j -1),
            self.pega_celula_por_eixo(self.i +1, self.j),
            self.pega_celula_por_eixo(self.i +1, self.j +1),
            self.pega_celula_por_eixo(self.i, self.j +1),
        ]
         celula = [i for i  in celula if i is not None]
         return celula
        
    @property
    def lista_de_celulas_length (self):
        contador = 0
        for i in self.lista_de_celulas:
            if i.is_mine:
                contador += 1
            return contador


    def show_cell(self):
       
        self.cell_btn_object.configure (text=self.lista_de_celulas_length)
      


    def show_mine(self):
        #logica pra quando jogador clica na mina
        self.cell_btn_object.config(bg='blue')

    def botao_direito_click(self, evento):
        print (evento)
        
     
    @staticmethod
    def randomize_mines():
    
        celulas_pegada = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for i in celulas_pegada:
            i.is_mine = True

    def __repr__(self):
        return f"Cell({self.i}, {self.j})"