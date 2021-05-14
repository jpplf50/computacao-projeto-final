# Create your models here.
from django.db import models
from graphviz import Digraph
import os, re
from django.conf import settings


class Automato(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    alfabeto = models.CharField(max_length=100)
    estados = models.CharField(max_length=100)
    estadoInicial = models.CharField(max_length=100)
    estadosDeAceitacao = models.CharField(max_length=100)
    dicionarioTransicao = models.CharField(max_length=1000)
    diagrama = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    def printAlfabeto(self):
        return str(set(self.alfabeto.split()))

    def printEstados(self):
        return str(set(self.estados.split()))

    def printEstadosDeAceitacao(self):
        return str(set(self.estadosDeAceitacao.split()))

    def dTransInTable(self):
        dTrans = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicionarioTransicao.split()}

        table = []

        linha = ['']
        for simbolo in self.alfabeto.split():
            linha.append(simbolo)
        table.append(linha)

        for estado in self.estados.split():
            linha =[estado]
            for simbolo in self.alfabeto.split():
                linha.append(dTrans[(estado, simbolo)])
            table.append(linha)

        return table

    def valida_sequencia(self, sequencia):

        estado = self.estadoInicial

        dTrans = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicionarioTransicao.split()}

        for simbolo in sequencia:
            if simbolo in self.alfabeto:
                estado = dTrans[(estado, simbolo)]
            else:
                return False

        if estado in self.estadosDeAceitacao:
            return True
        else:
            return False


    def desenha_diagrama(self):

        d = Digraph(name=self.descricao)

        # configurações gerais
        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        # d.edge_attr['color'] = 'blue'
        d.node_attr['shape'] = 'circle'
        # d.node_attr['color'] = 'blue'

        # Estado inicial
        d.node('Start', label='', shape='none')

        # Estados de transição
        estadosDeTransicao = set(self.estados.split()) - set(self.estadosDeAceitacao.split())
        for estado in estadosDeTransicao:
            d.node(estado)

        # Estado aceitação
        for estado in self.estadosDeAceitacao.split():
            d.node(estado, shape='doublecircle')

        # Transicoes
        d.edge('Start', self.estadoInicial)

        for transicao_comma in self.dicionarioTransicao.split():
            transicao = transicao_comma.split('-')
            d.edge(transicao[0], transicao[2], label=transicao[1])

        d.format = 'svg'
        self.diagrama = f"computacao/images/afd/{str(self.nome).replace(' ', '_')}.svg"
        d.render(f"computacao/static/computacao/images/afd/{str(self.nome).replace(' ', '_')}")


class MaquinaTuring(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    alfabeto = models.CharField(max_length=100)
    estados = models.CharField(max_length=100)
    estadoInicial = models.CharField(max_length=100)
    estadosDeAceitacao = models.CharField(max_length=100)
    dicionarioTransicoes = models.CharField(max_length=100)
    diagrama = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    def printAlfabeto(self):
        return str(set(self.alfabeto.split()))

    def printEstados(self):
        return str(set(self.estados.split()))

    def printEstadosDeAceitacao(self):
        return str(set(self.estadosDeAceitacao.split()))

    def dTransInTable(self):
        dTrans = {(t.split('-')[0], t.split('-')[1][0]):t.split('-')[2] for t in self.dicionarioTransicoes.split()}
        dSecond = {(t.split('-')[0], t.split('-')[2]):t.split('-')[1] for t in self.dicionarioTransicoes.split()}
        table = []

        linha = ['']
        for simbolo in self.alfabeto.split():
            linha.append(simbolo)
        table.append(linha)

        for estado in self.estados.split():
            linha =[estado]
            for simbolo in self.alfabeto.split():
                if(estado,simbolo) in dTrans:
                    linha.append(dSecond[(estado,dTrans[(estado,simbolo)])][1] + "," + dSecond[(estado,dTrans[(estado,simbolo)])][2] + "," + dTrans[(estado, simbolo)])
                else:
                    linha.append(" ")
            table.append(linha)

        return table

    def valida_sequencia(self, sequencia):

        sequencia = list(sequencia)
        sequencia.insert(len(sequencia), 'd')
        sequencia.insert(0, 'd')
        estadoAtual = self.estadoInicial

        dTrans = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicionarioTransicoes.split()}


        for simbolo in sequencia:
            if simbolo in self.alfabeto:
                continue
            else:
                return False

        i = 1
        found = True
        while True:
            if found == False:
                break
            found = False#caso não seja encontrado no loop, proxima vez que correr o for ira ser False, e retornar False para sair do While
            for estado,simbolos in dTrans:
                if estadoAtual == estado and sequencia[i] == simbolos[0]:
                    found = True #neste loop foi encontrado, pode se avançar para o proximo
                    sequencia[i] = simbolos[1]
                    if simbolos[2] == 'R': #se for right move-se para a direita na sequencia
                        i += 1
                    elif simbolos[2] == 'L': #se for left move-se para a esquerda na sequencia
                        i -= 1
                    estadoAtual = dTrans[(estado,simbolos)] #mudamos para o estado correspondente

        if estadoAtual in self.estadosDeAceitacao:
            return True
        else:
            return False

    def desenha_diagrama(self):

        d = Digraph(name=self.descricao)

        # configurações gerais
        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        # d.edge_attr['color'] = 'blue'
        d.node_attr['shape'] = 'circle'
        # d.node_attr['color'] = 'blue'

        # Estado inicial
        d.node('Start', label='', shape='none')

        # Estados de transição
        estadosDeTransicao = set(self.estados.split()) - set(self.estadosDeAceitacao.split())
        for estado in estadosDeTransicao:
            d.node(estado)

        # Estado aceitação
        for estado in self.estadosDeAceitacao.split():
            d.node(estado, shape='doublecircle')

        # Transicoes
        d.edge('Start', self.estadoInicial)

        dicDesenhar =  {}
        for transicao_comma in self.dicionarioTransicoes.split():
            transicao = transicao_comma.split('-')
            if (transicao[0],transicao[2]) in dicDesenhar:
                dicDesenhar[(transicao[0],transicao[2])] += "," + transicao[1]
            else:
                dicDesenhar[(transicao[0],transicao[2])] = transicao[1]


        for key,value in dicDesenhar.items():
            d.edge(key[0], key[1], label=value)

        d.format = 'svg'
        self.diagrama = f"computacao/images/turing/{str(self.nome).replace(' ', '_')}.svg"
        d.render(f"computacao/static/computacao/images/turing/{str(self.nome).replace(' ', '_')}")

class ExpressaoRegular(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    expressao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    def printExpressao(self):
        return self.expressao

    def valida_sequencia(self, sequencia):
        if re.search(self.expressao,sequencia):
            return True
        else:
            return False
