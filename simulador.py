from tkinter import *
from tkinter.filedialog import askopenfilename
import math


class Simulacao:
    ID = 0
    T_CRIADO = 0
    T_MORTO = 0
    TAMANHO = 0
    qtd_paginas = 0
    tempoMorrer = 0

class Aplication:

    #ID = 0
    #T_CRIADO = 0
    #T_MORTO = 0
    #TAMANHO = 0
    #qtd_paginas = 0
    listaProcessos = []

    def __init__(self, master):
        self.master = master
        self.fontePadrao = ("Arial", "10")
        self.container = Frame(master)
        self.container["height"] = 150
        self.container["width"] = 150
        self.container.pack()

        self.tamanhoPaginaLabel = Label(self.container, text = "Selecione o tamanho da página", font = self.fontePadrao)
        #self.tamanhoPaginaLabel["width"] = 100
        #self.tamanhoPaginaLabel["height"] = 15
        self.tamanhoPaginaLabel.pack()

        self.tamanhosPagina = ["8","16","32","64","128"]
        self.tamanhosPaginaStrings = StringVar(master)
        self.tamanhosPaginaStrings.set(self.tamanhosPagina[1])
        self.tamanhosPaginaMenu = OptionMenu(self.container, self.tamanhosPaginaStrings, *self.tamanhosPagina)
        self.tamanhosPaginaMenu.pack()

        self.tamanhoPaginaLabel = Label(self.container, text = "Selecione o tamanho da memória", font = self.fontePadrao)
        self.tamanhoPaginaLabel.pack()

        self.tamanhosMemoria = ["512","1024","2048","4096"]
        self.tamanhosMemoriaStrings = StringVar(master)
        self.tamanhosMemoriaStrings.set(self.tamanhosMemoria[1])
        self.tamanhosMemoriaMenu = OptionMenu(self.container, self.tamanhosMemoriaStrings, *self.tamanhosMemoria)
        self.tamanhosMemoriaMenu.pack()

        self.label1 = Label(self.container, text = "Selecione o arquivo")
        self.label1.pack()

        self.caminho = Entry(self.container)
       # self.caminho["width"] = 50
        self.caminho.pack(side=LEFT)

        self.filename = Button(self.container, text = "Selecionar arquivo", command = self.openfile)
        self.filename.pack()
        
        self.confirmar = Button(self.container, text = "Começar simulação", command = self.janelaSimulacao )
        self.confirmar.pack()

    def openfile(self):
        self.filename = askopenfilename(title = "Selecionar arquivo",filetypes = (("csv","*.csv"),("txt",".txt"),("all files","*.*"))) 
        print(self.filename)
        self.caminho.delete(0, END)
        self.caminho.insert(0,self.filename)
    
    def lerArquivo(self):
        try:
            arquivo = open(self.caminho.get(), "r")
        except Exception as ex:
            janela = Tk()
            container = Frame(janela, height = 500)
            container.pack()
            janelaErro = Label(container, text = type(ex), font = 100)
            janelaErro.pack()
            return False
        #listaProcessos = []
    
        for lena in arquivo:
            processoAtual = Simulacao()
            linha = lena.split(",")
            processoAtual.ID = int(linha[0])
            processoAtual.T_CRIADO = int(linha[1])
            processoAtual.T_MORTO = int(linha[2])
            processoAtual.TAMANHO = int(linha[3])
            processoAtual.qtd_paginas = math.ceil(processoAtual.TAMANHO/int(self.tamanhosPaginaStrings.get()))

            self.listaProcessos.append(processoAtual)
        arquivo.close()
        #for x in range(0,len(self.listaProcessos)):
        #    print("\nID: ",self.listaProcessos[x].ID,"\nT_CRIADO: ",self.listaProcessos[x].T_CRIADO,"\nT_MORTO: ",self.listaProcessos[x].T_MORTO,"\nTAMANHO: ",self.listaProcessos[x].TAMANHO, "\nQtd páginas: ", processoAtual.qtd_paginas)

   # def janelaSimulacao(self):
        #self.master.withdraw()
        #self.newWindow = Toplevel(self.master)
        #self.container2 = Frame(self.master)
        #self.container2.pack()
       # lerArquivo(self.caminho.get())

    def janelaSimulacao(self):
        
        if(self.lerArquivo() == False):
            return
        tamanhoPagina = int(self.tamanhosPaginaStrings.get())
        tamanhoMemoria = int(self.tamanhosMemoriaStrings.get())
        qtdPaginas = tamanhoMemoria / tamanhoPagina
        print("quantidade paginas: ", qtdPaginas)

        janela2 = Tk()

        container2 = Frame(janela2)
        container2.pack()

        logSaidaTitulo = Label(container2, text = "Log Saida")
        logSaidaTitulo.pack()

        logSaida = Label(container2, text = "Vazio")
        logSaida.pack()


        listaLabels = [] # Lista de Labels das paginas

        for x in range(0, int(qtdPaginas)):
            label = Label(container2, text = "Pagina "+str(x)+"\t")
            listaLabels.append(label)
        for x in range(0, len(listaLabels)):
            listaLabels[x].pack(side = LEFT)
        #listaLabels[0]["text"] = listaLabels[0]["text"]+"\nJNDuebfeubUBB"

        # = math.ceil(self.listaProcessos[0].TAMANHO/tamanhoPagina)
        #print("N = ",n)
        processosDentro = []
        #filaEspera = []
        tempoTotal = 1
        tempoEspera = 0
        #tempoProcessos = 1
        #cond = True
        print("tempo | processo | posicao_inicial_na_memoria | ação")
        input()
        while(True):
            print("Quantidade de páginas disponíveis: ",qtdPaginas)
            #cond2 = True
            #x = 0
            while(True):
                if self.listaProcessos: # Enquanto processos estiverem esperando
                    if(self.listaProcessos[0].qtd_paginas <= qtdPaginas):
                        if(self.listaProcessos[0].T_CRIADO <= tempoTotal):

                            print("Tempo quando entrou: ",tempoTotal," Processo: ",self.listaProcessos[0].ID," NULL"," Entrou")
                            if(self.listaProcessos[0].T_CRIADO == self.listaProcessos[0].T_MORTO):
                                print("Tempo quando saiu: ",tempoTotal," Processo: ",self.listaProcessos[0].ID," NULL","|| Saiu")
                                self.listaProcessos.pop(0)
                            else:
                                qtdPaginas -= self.listaProcessos[0].qtd_paginas
                                self.listaProcessos[0].tempoMorrer = tempoTotal + (self.listaProcessos[0].T_MORTO - self.listaProcessos[0].T_CRIADO)
                                processosDentro.append(self.listaProcessos.pop(0))
                                #tempoTotal += 1
                    else:
                        print("Tempo: ",tempoTotal," Processo: ",self.listaProcessos[0].ID," NULL"," Esperando", "Tempo de espera total: ", tempoEspera)
                        tempoEspera += 1
                        #tempoTotal += 1
                        break
                    if self.listaProcessos: # Caso seja o último processo, vai tentar acessar a primeira posição da lista, que já está vazia, logo o if para verificar
                        if(self.listaProcessos[0].T_CRIADO != tempoTotal): # Caso não tenha mais nenhum processo a ser criado no mesmo tempo sai do loop
                            break
                else:
                    break
            if processosDentro:
                a = 0
                while(True):
                    if(a >= len(processosDentro)):
                        break
                    if(processosDentro[a].tempoMorrer == tempoTotal):
                        qtdPaginas += processosDentro[a].qtd_paginas
                        print("Tempo quando saiu: ",tempoTotal," Processo: ",processosDentro[a].ID," NULL","|| Saiu")
                        processosDentro.pop(a)
                        a-=1
                    a+=1 

            if not self.listaProcessos and not processosDentro: # Quando todos os processos já tiverem entrado e saído
                break
            tempoTotal += 1
            input()
        print("Fim da Simulação")
    
root = Tk()
Aplication(root)
root.mainloop()