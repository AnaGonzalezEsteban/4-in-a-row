from Settings import *
from list_utilities import find_streak

class LinearBoard:
    """Representa un tablero con una sola columna.
    x representa al jugador 1
    o representa al jugador 2
    None representa un espacio vacío
    """
    @classmethod
    def fromList(cls,list):
        """crea y devuelve un linearboard a partir de una lista que representa una jugada"""
        board=cls() #self es una variable que se evalua a la instancia/objeto, y cls es una variable que se evalua a la clase
        board._column=list
        return board

    def __init__(self):
        """Inicializa el tablero vacío, es decir, lleno de None"""
        self._column = [None] * BOARD_SIZE
    
    def is_full(self):
        """Devuelve True si el tablero está lleno"""
        #si el último elemento es None
        if self._column[-1]==None:
            # NO está lleno
            return False
        #en otro caso
        else:
            # SÍ está lleno
            return True

    def as_list(self):
        """devuelve la representacion del tablero como una lista"""
        return 

    def add(self,char):
        """Añade una ficha en dicha columna en el primer espacio disponible"""
        #Si  la columna no está llena:
        if not self.is_full():
            # averiguo donde está el primer None:
            i = self._column.index(None) #la función index devuelve el primer None que encuentra en la lista
            # lo cambio por un char:
            self._column[i] = char

    def is_victory(self,char):
        return find_streak(self.column,char,VICTORY_STRIKE)

    def is_tie(self,char1,char2): #EMPATE arreglarlo sabiendo que el tablero está lleno
        #si no hay victoria de nadie, entonces hay empate:
        if (self.is_victory(char1) == False) and (self.is_victory(char2) == False) and self.is_full():
            return True
        else:
            return False
