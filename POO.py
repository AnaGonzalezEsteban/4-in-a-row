# Vamos a crear una applicación de tipo catálogo de personajes de Star Wars, algo similar a la [Wookiepedia](https://starwars.fandom.com/wiki/Wookieepedia).

# Crea una jerarquía de clases sencilla para representar los personajes de Star Wars. 
# Los Jedis y los Sith entienden ambos el mensaje "unsheathe" (desenvaina) que muestra un sable láser. 
# Los sables de los Sith y de Los Jedis son distintos.

from enum import Enum

class Affiliation(Enum):#centraliza la representacion para evitar que en cada clase la llamemos de una forma diferente
    REBEL_ALIANCE=0
    GALACTIC_EMPIRE=1
    UNKNOWN=2


class StarWarsCharacter:
    def __init__(self,name,alias):
        """Crea un personaje con nombre y alias"""
        self.name=name
        self.alias=alias
    def __repr__(self):
        """Muestra la representación textual del objeto"""
        return f'<{self.__class__}:{self.name} {self.alias}>'
        #el metodo especial __class__ indica a que clase pertenece
        
class ForceSensitive(StarWarsCharacter):
    """
    Representa personajes sensibles a la Fuerza
    """
    def __init__(self, name, alias, affiliation, midichlorians):
        super().__init__(name, alias, affiliation)
        self.midichlorians = midichlorians
        
    def unsheathe(self): #desenvaina
        """
        Este método, solo sirve para que mis subclases lo entiendan y no tenga que repetirlo
        """
        raise NotImplementedError()

chewie=StarWarsCharacter('Chewbacca','Chewie')
jabba=StarWarsCharacter('Jabba Dessilic','Jabba The Hutt')

print([chewie,jabba])

    
class Jedi(ForceSensitive):
    @classmethod
    def padawan(clas,name,alias):
        return cls(name,alias,10)

    @classmethod #modificador del metodo (lo transforma en un metodo de clase en este caso)
    def master(cls,name,alias):#lo hacemos asi porque la unica diferencia entre jedi y maestro jedi es un valor de midichlorians
        """Crea un maestro Jedi (con 100K midichlorians)"""
        return cls(name,alias,100000) #cls hace referencia a la clase
        #es algo similar al metodo init pero lleva un return

    def __init__(self, name, alias, midichlorians):
        super().__init__(name, alias, Affiliation.REBEL_ALIANCE, midichlorians) #devuelve lo que ya hay en la superclas
        
    def unsheathe(self):
        return '▐▍░▐░░▣░▒░▒░▒▕|' + "█" * 40

class Sith(ForceSensitive):
    @classmethod
    def darkLord(cls,name,alias):
        return cls(name,alias,120000)

    def __init__(self, name, alias, midichlorians):
        super().__init__(name, alias, Affiliation.GALACTIC_EMPIRE, midichlorians)
        
    def unsheathe(self):
        return '▔▔▔▔▔▔▔▔▔▝▔▔▔ ' + "█" * 40


yoda=Jedi.master('Master Yoda','Minch Yoda') #y aqui ya no hace falta decirle cuantos midiclorianos
yoda.unsheathe()

anakin=Jedi.padawan('Anakin Skywalker','Ani')
print(anakin.midichlorians)

dark_vader=Sith.darkLord('Anakin','Dark Vader')


