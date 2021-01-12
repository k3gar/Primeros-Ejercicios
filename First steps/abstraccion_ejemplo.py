import time

class supermercado:
    def __init__(self):
        pass

    def comprar(self, producto):
        self.producto = producto
        self._pasillo()
        self._caja()

    
    def _pasillo(self):
        print(f'buscando producto')
        time.sleep(5.5)
        print(f'Caminando entre pasillos')
    
    def _caja(self, estado=1):
        while estado != 10:
            print(f'Caja llena, espere un momento')
            time.sleep(3)
            estado += 1
        else:
            print('Compra realizada')
            

if __name__ == '__main__':
    supermercado = supermercado()
    supermercado.comprar('Atun')