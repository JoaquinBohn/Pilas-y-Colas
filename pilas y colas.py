
class Nodo:
    def __init__(self,dato=None,prox=None):
        self.dato=dato
        self.prox=prox
    def __str__(self):
        return str(self.dato)


class Pila:
    """Representa una pila con operaciones de apilar, desapilar y verificar si está vacía."""
    
    def __init__(self):
        """Crea una pila vacía."""
        self.items = []
    
    def apilar(self, x):
        """Apila el elemento x."""
        self.items.append(x)
    
    def desapilar(self):
        """Desapila el elemento x y lo devuelve. Si la pila está vacía levanta una excepción."""
        if self.esta_vacia():
            raise ValueError("La pila está vacía")
        return self.items.pop()
    
    def esta_vacia(self):
        """Devuelve True si la lista está vacía, False si no."""
        return len(self.items) == 0



class Cola:
    """Representa a una cola, con operaciones de encolar y
    desencolar. El primero en ser encolado es también el primero
    en ser desencolado. """
    
    def __init__(self):
        """Crea una cola vacía."""
        self.primero = None
        self.ultimo = None
    
    def encolar(self, x):
        """Encola el elemento x."""
        nuevo = Nodo(x)
        if self.ultimo:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        else:
            self.primero = nuevo
            self.ultimo = nuevo
    
    def desencolar(self):
        """Desencola el primer elemento y devuelve su 
        valor. Si la cola está vacía, levanta ValueError."""
        if self.primero is None:
            raise ValueError("La cola está vacía")
        valor = self.primero.dato
        self.primero = self.primero.prox
        if not self.primero:
            self.ultimo = None
        return valor
    
    def esta_vacia(self):
        """Devuelve True si la cola esta vacía, False si no."""
        return self.primero is None





"""Torre de control"""

class TorreDeControl:
    """Representa una torre de control de un aeropuerto."""
    
    def __init__(self):
        """Crea un vuelo vacio. Puede ser vuelo de aterrizaje o de partida."""
        
        self.cola_aterrizar = Cola()
        self.cola_despegar = Cola()
        self.lista_vuelos_aterrizar = []
        self.lista_vuelos_despegar = []
    
    def nuevo_arribo(self, vuelo):
        
        self.cola_aterrizar.encolar(vuelo)
        self.lista_vuelos_aterrizar.append(vuelo)
    
    def nueva_partida(self, vuelo):
        
        self.cola_despegar.encolar(vuelo)
        self.lista_vuelos_despegar.append(vuelo)
    
    def ver_estado(self):
        
        if not self.cola_aterrizar.esta_vacia() or not self.cola_despegar.esta_vacia():
            return "Vuelos esperando para aterrizar: {}.\n Vuelos esperando para despegar: {}.".format(self.lista_vuelos_aterrizar, self.lista_vuelos_despegar)
        else:
            return "No hay vuelos en espera."
    
    def asignar_pista(self):
        
        if not self.cola_aterrizar.esta_vacia():
            aterrizaje = self.cola_aterrizar.desencolar()
            return "El vuelo {} aterrizo con exito.".format(aterrizaje)
        if not self.cola_despegar.esta_vacia():
            partida = self.cola_despegar.desencolar()
            return "El vuelo {} despego con exito.".format(partida)
        return "No hay vuelos en espera."




"""Impresora"""

class Impresora:
    """Representa a una impresora."""
    
    def __init__(self, nombre, capacidad):
        
        if not str(capacidad).isdigit():
            raise ValueError("La capacidad debe ser un numero entero.")
        self.impresora = Cola()
        self.nombre = nombre
        self.capacidad = int(capacidad)
        self.tinta = int(capacidad)
        self.aux = Cola()

    def cant_archivos(self):
        
        contador = 0
        while not self.impresora.esta_vacia():
            doc = self.impresora.desencolar()
            contador += 1
            self.aux.encolar(doc)
        self.impresora = self.aux
        return contador
    
    def cargar_doc(self, documento):
        
        self.impresora.encolar(documento)
    
    def imprimir(self):
        
        if self.tinta==0:
            return "No hay tinta."
        else:
            if not self.impresora.esta_vacia():
                documento = self.impresora.desencolar()
                self.tinta -= 1
                return "Se ha imprimido el archivo {}.".format(documento)
            else:
                return "No hay documentos para imprimir."
    
    def recargar(self):
        
        if self.tinta == self.capacidad:
            return "El cartucho se encuentra lleno."
        else:
            self.tinta = self.capacidad


"""Oficina"""

class Oficina:
    """Representa a una oficina, creo?"""
    
    def __init__(self):
        
        self.diccionario_impresoras = {}

    def agregar_impresora(self, impresora):
        
        nombre = impresora.nombre
        self.diccionario_impresoras[nombre] = impresora
    
    def impresora(self, nombre):
        
        if nombre in self.diccionario_impresoras:
            return self.diccionario_impresoras[nombre]
        else:
            return "La impresora no se encuentra en esta oficina."
    
    def quitar_impresora(self, nombre):
        
        if nombre in self.diccionario_impresoras:
            self.diccionario_impresoras.pop(nombre)
        
        else:
            return "La impresora no se encuentra en esta oficina."
    
    def obtener_impresora_libre(self):
        
        if len(self.diccionario_impresoras)==0:
            return "No hay impresoras en la oficina."
        else:
            menor = 1000
            for clave in self.diccionario_impresoras:
                largo_cola = self.diccionario_impresoras[clave].cant_archivos()
                if largo_cola<menor:
                    menor = self.diccionario_impresoras[clave].cant_archivos
                    impresora_buscada = self.diccionario_impresoras[clave]
                else:
                    return "No hay impresoras libres."
            return impresora_buscada



"""Juegos de cartas"""

class Carta:
    """Representa una carta con su palo y valor."""
    
    def __init__(self, palo, valor):
        
        self.palo = palo
        self.valor = valor
    
    def mostrar(self):
        
        return (str(self.valor),str(self.palo))


class Solitario:
    """Representa un juego de cartas solitario. Consiste en apilar cartas una 
    arriba de otra, solo permite hacerlo si la carta es inmediatamente inferior
    y de distinto palo a la del tope."""
    
    def __init__(self):
        
        self.mazo = Pila()
    
    def apilar(self, carta):
        
        if self.mazo.esta_vacia():
            self.mazo.apilar(carta)
        else:
            tope = self.mazo.desapilar()
            if tope.valor > carta.valor and tope.palo != carta.palo:
                self.mazo.apilar(tope)
                self.mazo.apilar(carta)
            else:
                raise Exception("No se puede apilar esta carta.")






