#Ejercicio de un metodo que retorna una lista de numeros pares

class ListaPares:
    def __init__(self):
        self.listaPares = []
    
    def listaNumeros(self,numero):
        self.numero = numero
        self.numero += 2
        for i in range(self.numero):
            if i % 2 == 0:
                self.listaPares.append(i)
        print(self.listaPares)

lista = ListaPares()
numero = int(input("Ingresa la longitud de la lista:"))
lista.listaNumeros(numero)

