# -*- coding:UTF-8 -*-

class No:

    def __init__(self, dado=None, prioridade=None, prox=None):
        self.__dado = dado
        self.__prioridade = prioridade
        self.__prox = prox


    def __str__(self) -> str:
        return f"Dado: {self.__dado}; Prioridade: {self.__prioridade}"


    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, valor):
        self.__dado = valor


    @property
    def prioridade(self):
        return self.__prioridade
    
    @prioridade.setter
    def prioridade(self, valor):
        self.__prioridade = valor


    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, valor):
        self.__prox = valor

