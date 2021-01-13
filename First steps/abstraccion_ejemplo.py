import time
item = input('¿Que desea comprar?: ')
capacidad = input('Si la caja se encuentra vacia escrbia ¨libre¨ \nSi la caja se encuentra llena, escriba ¨lleno¨: ')

class supermercado:
    def __init__(self):
        pass

    def comprar(self, producto):
        self.producto = producto
        self._pasillo()
        self._caja()
        #self._estado()

    
    def _pasillo(self):
        print(f'buscando producto')
        time.sleep(5.5)
        print(f'Caminando entre pasillos')
    
    def _caja(self, estado=0):
        if capacidad == 'libre':
            print(f'La caja esta libre, puede pasar')

        elif capacidad == 'lleno':
            while estado != 3:
                print(f'Caja llena, espere un momento')
                time.sleep(2)
                estado += 1
            else:
                print('Compra realizada')
                print(f'Logró comprar {item}')   
        else:
            print('Opcion incorrecta') 
    #def _estado(self, capacidad):
    #    self.capacidad = capacidad
    #    if capacidad == 'libre':
    #        print(f'La caja esta libre, puede pasar')
        
    #    elif capacidad != 'libre':
    #        _caja
    #    else:
    #        pass

if __name__ == '__main__':
    supermercado = supermercado()
    supermercado.comprar(item)
    #supermercado.estado(capacidad)
