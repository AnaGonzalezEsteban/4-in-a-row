from Settings import *
from Linear_board import *
from reduce import and_all 
from list_utilities import *


class SquareBoard():
    """
    Clase que representa un tablero cuadrado
    Métodos para:
    1. Añadir un caracter (jugar en una columna)
    2. Detectar la victoria de un jugador
    3. Detectar el empate de dos jugadores
    4. Detectar que el tablero está lleno
    """
    @classmethod
    def fromList(cls,list_of_lists):
        """Transforma una lista de listas en una lista de linearBoards"""
        columns=[]
        for element in list_of_lists:
            columns.append(LinearBoard.fromList(element)) #aqui utilizo el fromList de linear_board
            board=cls()
            board._columns=columns
        return board

    def __init__(self):
        # inicializar las columnas/inicializar varios tableros lineales llamando a tantos tableros lineales como necesitemos y metiendolos en una lista
        # self._columns=[LinearBoard()]*BOARD_SIZE #CUIDADO!!!!!!!!ESTA OPCION NO VALE PORQUE ES EL MISMO TABLERO, APARECERIA LO MISMO EN TODAS LAS COLUMNAS 4 VECES
        self._columns=[LinearBoard() for i in range(BOARD_SIZE)] #list comprehension

    
    def __repr__(self):
        """Devuelve una representacion textual del objeto"""
        # obtengo la representacion como matriz
        matrix=self.as_matrix()
        #le quito los None y los sustituyo por '-'
        matrix=replace_matrix(matrix)
        # transpongo la matriz para tener filas en las listas
        transp=transpose(matrix,lambda x:x==None,'-')
        #la invierto
        transp.reverse()
        #gewnero una cadena con todas esas listas
        tmp='\n' #pongo un salto de linea en lugar de cadena vacia
        for row in transp:
            for element in row:
                tmp=tmp+'\t'+element
            tmp=tmp+'\n'
        return f'<{self.__class__}>{tmp}:'

    def is_full(self): #SE TRATA DE UN REDUCTOR CON AND!!!!!
        all_full = True
        for board in self._columns:
            all_full = all_full and board.is_full() #COMBINO TODOS LOS VALORES BOOLEANOS DE IS_FULL CON ALL_FULL PARA REDUCIR
            #este .is_full llama al is_full de linearboard porque va asociado a un objeto linearboard.
            #Si queremos llamar al is_full aquí tendriamos que hacer  un objeto de tipo Squareboard.is_full.
            return all_full

    def is_full(self):#utilizar and_all
        pass



    def is_victory(self,char): # victoria vertical
        # preguntarle a cada linearboard si tienen una victoria vertical
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)


    def add(self,char,index):
        # por el índice sabes en que tablero lineal se va a añadir
        self._columns[index].add(char) #devuelve la columna con el tablero lineal en el que vamos a añadir el char

    def as_matrix(self): #procesa lista y devuelve una lista procesada --> map!!
        """"Devuelve su representacion como matriz"""
        matrix=[]
        for linear_board in self._columns:
            matrix.append(linear_board.as_list()) #as_list lo creamos como metodo de linear_board    
            return matrix   

    def _any_vertical_victory(self,char): 
        victory=False
        for linear_board  in self._columns:
            victory=victory or linear_board.is_victory(char)
        return

    def _any_horizontal_victory(self,char): #trasponemos el tablero y le aplicamos victoria vertical --> def first_elements
        """averigua si en el tablero hay una victoria horizontal rotando el tablero y al tablero resultante preguntandole si tiene una victoria vertical"""
        #Obtengo la matriz que representa al tablero actual(self)
        #transpongo esa matriz
        #creo un tablero temporal a partir de esa matriz
        #le pregunto si tiene alguna victoria vertical
        #devuelvo ese valor
        pass

    def _any_rising_victory(self, char):
        # obtener las columnas
        m = self.as_matrix()
        # las invertimos
        rm = reverse_matrix(m)
        # creamos tablero temporal con esa matriz
        tmp = SquareBoard.fromList(rm)
        # devolvemos si tiene una victoria descendente
        return tmp._any_sinking_victory(char)

    def _any_sinking_victory(self,char):
        #obtengo la representacion matricial del tablero
        matrix=self.as_matrix()
        #le meto un displace matrix
        matrix=displace_matrix(matrix)
        #si habia victoria descendente, ahora es horizontal
        #creo un tablero temporal con esa matriz desplazada
        #si hay victoria horizontal en la desplazada, en la original habia una victoria descendente
        tmp=SquareBoard.fromList(matrix)
        return tmp._any_horizontal_victory(char)
