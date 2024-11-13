class sumatorias:
    def __init__(self,dataset,ejeX,ejeY):
        self.ejeX=ejeX
        self.ejeY=ejeY
        self.dataset=dataset
        self.calculosPrevios()

    #Obteniendo sumatorias 
    def calculosPrevios(self):
        self.Sx2=(self.dataset[self.ejeX]**2).sum()
        self.Sy=self.dataset[self.ejeY].sum()
        self.Sx=self.dataset[self.ejeX].sum()
        self.Sxy=(self.dataset[self.ejeX]*self.dataset[self.ejeY]).sum()
