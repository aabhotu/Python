from tkinter import *


class ThiSinh():
    def __init__(self, ten, namSinh, dToan, dVan, dnn):
        self.ten = ten
        self.namSinh = namSinh
        self.dToan = dToan
        self.dVan = dVan
        self.dnn = dnn

    def Tuoi(self):
        return 2022-self.namSinh

    def tongDiem(self):
        return self.dToan+self.dVan+self.dnn
