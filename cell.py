from tkinter import Button


class Cell:
    all =[]
    def __init__(self,i,j, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.i = i #feito para manipular cada celula especifica
        self.j = j
        #criar um objeto ao Cell para lista "All"
        Cell.all.append(self)

    def cria_btn_object (self, location):#saber a localizacao do meu botao
        btn = Button(
            location,
            text=f"{self.i}, {self.j}",
            width=12,
            height=4

        )
        btn.bind('<Button-1>',self.botao_esquerdo_click)
        btn.bind('<Button-3>',self.botao_direito_click)
        self.cell_btn_object = btn

    def botao_esquerdo_click(self, evento):
        print("clicado com botao esquerdo")
    def botao_direito_click(self, evento):
        print("clicado com botao direito")
     
    @staticmethod
    def randomize_mines():
        pass

    def __repr__(self):
        return f"Cell({self.i}, {self.j})"