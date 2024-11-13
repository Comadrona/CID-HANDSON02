import pandas as pd

#Utiles para plotear elementos del dataset y ecuacion
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class SLRModel:
    def __init__(self,file,ejeX,ejeY):
        self.construirDataSet(file)
        if ejeX not in self.dataset.columns:
            raise ValueError("El nombre de la columna "+ejeX+" no se encuentra en el dataframe")
        elif  ejeY not in self.dataset.columns:
            raise ValueError("El nombre de la columna "+ejeY+" no se encuentra en el dataframe")
        else:
            self.ejeX=ejeX
            self.ejeY=ejeY
            self.dataset=self.dataset[[self.ejeX,self.ejeY]]
            self.calculosPrevios()
            self.calcularBeta0()
            self.calcularBeta1()

    def construirDataSet(self,file):
        self.dataset=pd.read_csv(file)

    #Obteniendo sumatorias 
    def calculosPrevios(self):
        self.Sx2=(self.dataset[self.ejeX]**2).sum()
        self.Sy=self.dataset[self.ejeY].sum()
        self.Sx=self.dataset[self.ejeX].sum()
        self.Sxy=(self.dataset[self.ejeX]*self.dataset[self.ejeY]).sum()

    def calcularBeta0(self):
        #Usando round para redondear y matchear con el valor esperado por la pagina
        self.beta0=round(((self.Sx2*self.Sy)-(self.Sx*self.Sxy))/
                    ((len(self.dataset)*self.Sx2)-(self.Sx)**2))
    
    def calcularBeta1(self):
        #Usando round para redondear y matchear con el valor esperado por la pagina
        self.beta1=round(((len(self.dataset)*self.Sxy)-(self.Sx*self.Sy))/
                    ((len(self.dataset)*self.Sx2)-(self.Sx)**2))
    
    def insertInstance(self,valorX,valorY):
        instancia =  {
            self.ejeX:[valorX],
            self.ejeY:[valorY]
        }
        print(instancia)
        self.dataset = pd.concat([self.dataset, pd.DataFrame(instancia)], ignore_index=True)
        self.calculosPrevios()
        self.calcularBeta0()
        self.calcularBeta1()

    def getDataSet(self):
        return self.dataset
    
    def getEquation(self):
        return " y = "+str(self.beta0)+" + "+str(self.beta1)+"x"
    
    def getEstimatedValue(self,valorX):
        valorY=self.beta0+(self.beta1*valorX)
        return str(valorY)
    
    def plot(self):
        #Graficando puntos y ecuacion obtenida
        plt.scatter(self.dataset[self.ejeX],self.dataset[self.ejeY],color='r',marker='o',label='Datos')
        x = np.linspace(0,max(self.dataset[self.ejeX])+5,100)
        y = self.beta1 * x + self.beta1
        plt.plot(x,y,color='b',label="y = "+str(self.beta0)+" + "+str(self.beta1)+"x")
        plt.title('MODELO')
        plt.xlabel(self.ejeX)
        plt.ylabel(self.ejeY)
        plt.legend()
        plt.show()
        """
        Graficando con regplot para regrecion lineal de la libreria seaborn
        sns.regplot(data=self.dataset,x=self.ejeX,y=self.ejeY,color='b',line_kws={'color':'r'})
        plt.title('MODELO')
        plt.xlabel(self.ejeX)
        plt.ylabel(self.ejeY)
        plt.show()
        """