# -*- coding: utf-8 -*-
########################################
# Tema: Calculadora de matrices        #
# Presentado por: Natalia Isaza        #
#                 Andres Felipe Farfan #
#                 Juan Felipe Marin    #
# Presentado a: Ing. Carlos Londoño    #
#                                      #
# Materia: Inteligencia Artificial     #
#                                      #
# Corporacion de estudios tecnologios  #
#          Del norte del valle         #
#                                      #
########################################

from random import randint #random para general la matriz automaticamente
#self se usa para tener alcance afuera del metodo
#La función str transforma un dato en una cadena.
class Matriz(object):

# ------------------------------OBTENER-------------------------------#
    def __init__(self, filas=None, columnas=None):


        if filas:
            self.filas=filas
        else:
            self.filas=int(input(" Por favor ingrese el numero de filas "))
        if columnas:
            self.columnas= columnas
        else:
            self.columnas = int(input(" Por favor ingrese el numero de columnas "))

#-------------------------------CREAR----------------------------------#

    def crearMatrizA(self):
        self.matriz = []
        for f in range(self.filas):
            self.matriz.append([randint(0, 100)] * self.columnas)

#-----------------------------LLENAR----------------------------------#
    def llenarmatrizA(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz.append(randint(0, 100))

        return self.matriz

#---------------------------IMPRIMIR MATRIZ A----------------------------------#
    def imprime_matriz(self):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(self.matriz[i][j]) + "\n"
                else:
                    cadena = cadena + str(self.matriz[i][j]) + "  "


        print ("Matriz A "+'\n' + cadena)

#---------------------------IMPRIMIR MATRIZ B----------------------------------#
    def imprime_matrizB(self,matrizB):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(matrizB[i][j]) + "\n"
                else:
                    cadena = cadena + str(matrizB[i][j]) + "  "
        return cadena

#---------------------IMPRIMIR MATRIZ RESULTADO--------------------------------#
    def imprime_matrizC(self):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(self.matriz[i][j]) + "\n"
                else:
                    cadena = cadena + str(self.matriz[i][j]) + "  "


        print ("Matriz B "+'\n' + cadena)

#---------------------------DETERMINANTE----------------------------------#
    def matrizcopy(self, matriz):
        self.result = []
        for f in matriz:
            self.result.append(f[:])
        return self.result

    def primeroNoNulo(self,m,i):
        result = i
        while result < len(m) and m[result][i] == 0:
            result = result + 1
        return result

    def intercambiaFilas(self, m,i,j):
        m[i], m[j] = m[j], m[i]

    def multiplicaFila(self, m, f, e):

        n = len(m)
        for c in range(n):
            m[f][c] = m[f][c] * e

    def combinacion(self, m,i,j,e):
        n = len(m)
        for c in range(n):
            m[j][c] = m[j][c] + e * m[i][c]

    def matriz_det(self,b):
        if (self.filas != self.columnas):
            print (" No se puede hayar el determinante, la matriz no es cuadrada ")
            return True
        elif self.filas==2:
                a=1
                b=1
                for f in range(self.filas):
                    for c in range(self.columnas):
                        if f==c:
                            a*=self.matriz[f][c]
                        else:
                            b*=self.matriz[f][c]
                det=a-b

                print (" El determinante es "+str(det))
                # ---------------------------ARCHIVAR DETERMINANTE----------------------------------#
                archivo = open("matrices.txt", "a")
                archivo.write("Resultado de la Determinante de Matrices:")
                archivo.write("\n")
                archivo.write(str(det))
                archivo.write("\n")
                return det
        else:
                m = self.matrizcopy(b)
                n = len(m)
                det = 1
                for i in range(n):
                    j = self.primeroNoNulo(m,i)
                    if j == n:
                        return 0
                    if i != j:
                        det = -1 * det
                        self.intercambiaFilas(m, i, j)
                    det = det * m[i][i]
                    self.multiplicaFila(m, i, 1. / m[i][i])
                    for k in range(i + 1, n):
                        self.combinacion(m, i, k, -m[k][i])

                print (" El determinante es " + str(det))

# ---------------------------TRANSPUESTA----------------------------------#
    def transpuesta(self):

        self.matrizB = []
        for f in range(self.columnas):
            self.matrizB.append([0] * self.filas)

        for i in range(self.filas):
            for j in range(self.columnas):
                self.matrizB[j][i] = self.matriz[i][j]

        a=self.imprime_matrizB(self.matrizB)
        print (" Matriz Transpuesta " + '\n' + a)

# -------------------ARCHIVAR TRANSPUESTA----------------------------------#
        archivo = open("matrices.txt", "a")
        archivo.write("Resultado de la Transpuesta de la Matrice:")
        archivo.write("\n")
        archivo.write(self.imprime_matrizB(self.matrizB))
        archivo.write("\n")
        return self.matrizB



# ---------------------------ESCALAR----------------------------------#
    def matriz_numero(self):
            self.matrizB = []
            for f in range(self.columnas):
                self.matrizB.append([0] * self.filas)
            a = int(input("Por favor ingrese un numero "))
            for i in range(self.filas):
                for j in range(self.columnas):
                    self.matrizB[i][j]= self.matriz[i][j]*a
            b = self.imprime_matrizB(self.matrizB)
            print (" Matriz Nueva " + '\n' + b)


# -------------------ARCHIVAR ESCALAR----------------------------------#
            archivo = open("matrices.txt", "a")
            archivo.write("Resultado de la ESCALAR de la Matrice:")
            archivo.write("\n")
            archivo.write(self.imprime_matrizB(self.matrizB))
            archivo.write("\n")

# -------------------MULTIPLICACION----------------------------------#
    def multiplicacionmatriz(self, filasA, columnasB, filasB,columnasA,matrizA,matrizB):

        if (filasA == filasB and columnasA == columnasB):

            self.matrizC = []
            for i in range(filasA):
                self.matrizC.append([0] * columnasB)

            for i in range(filasA):
                for j in range(columnasA):
                        self.matrizC[i][j] = matrizA[i][j] * matrizB[i][j]

            b = self.imprime_matrizB(self.matrizC)
            print (" Matriz Resultado " + '\n' + b)

        else:
            print (" No es posible realizar la operacion ")

# -------------------ARCHIVAR MULTIPLICACION----------------------------------#
        archivo = open("matrices.txt", "a")
        archivo.write("Resultado de la Multiplicacion de Matrices:")
        archivo.write("\n")
        archivo.write(self.imprime_matrizB(self.matrizC))
        archivo.write("\n")

# ------------------------SUMA----------------------------------#
    def sumamatriz(self, filasA, columnasB, filasB,columnasA,matrizA,matrizB):

        if (filasA == filasB and columnasA == columnasB):

            self.matrizC = []
            for i in range(filasA):
                self.matrizC.append([0] * columnasB)

            for i in range(filasA):
                for j in range(columnasA):
                        self.matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

            b = self.imprime_matrizB(self.matrizC)
            print (" Matriz Resultado " + '\n' + b)

        else:
            print (" No es posible realizar la operacion ")

# ---------------------ARCHIVAR SUMA----------------------------------#
        archivo = open("matrices.txt", "a")
        archivo.write("Resultado de la Suma de Matrices:")
        archivo.write("\n")
        archivo.write(self.imprime_matrizB(self.matrizC))
        archivo.write("\n")

# ------------------- RESTA ----------------------------------#
    def restamatriz(self, filasA, columnasB, filasB,columnasA,matrizA,matrizB):

        if (filasA == filasB and columnasA == columnasB):

            self.matrizC = []
            for i in range(filasA):
                self.matrizC.append([0] * columnasB)

            for i in range(filasA):
                for j in range(columnasA):
                        self.matrizC[i][j] = matrizA[i][j] - matrizB[i][j]

            b = self.imprime_matrizB(self.matrizC)
            print (" Matriz Resultado " + '\n' + b)

        else:
            print (" No es posible realizar la operacion ")

# -------------------ARCHIVAR RESTAS----------------------------------#
        archivo = open("matrices.txt", "a")
        archivo.write("Resultado de la Resta de Matrices:")
        archivo.write("\n")
        archivo.write(self.imprime_matrizB(self.matrizC))
        archivo.write("\n")

    def getFilas(self):
        return self.filas

    def getColumnas(self):
        return self.columnas

# -----------------------MENU----------------------------------#
class Menu(object) :

    def __init__(self, prompt="Selecione la opcion que desea ejecutar \n>> ") :
        self.presentacion = "------------------ Bienvenido a la Calculadora ------------------\n ----------------- Operaciones con Matrices ------------------\n\n"

        self.prompt = prompt + " "
        self.opciones = [
            self.opcion_Matriz_Suma,
            self.opcion_Matriz_Resta,
            self.opcion_Matriz_Multiplicacion,
            self.opcion_Matriz_Determinante,
            self.opcion_Matriz_Transpuesta,
            self.opcion_Matriz_Escalar,
            self.opcion_Salir,

        ]

        for numero, opcion in enumerate(self.opciones, 1):
            self.presentacion += "{0}. {1}\n".format(numero, opcion.__name__[7:])

    def loop(self):
        while True:
            print (self.presentacion)

            try:
                seleccion = int(input(self.prompt))

                if seleccion >= 1 and seleccion <= len(self.opciones) :

                    return seleccion

            except ValueError:
                input(" Error: Debes introducir un número, presiona enter ")


    def opcion_Matriz_Determinante(self):
        pass

    def opcion_Matriz_Transpuesta(self):
        pass
    def opcion_Matriz_Escalar(self):
        pass
    def opcion_Matriz_Multiplicacion(self):
        pass
    def opcion_Matriz_Suma(self):
        pass
    def opcion_Matriz_Resta(self):
        pass
    def opcion_Salir(self):
        pass
