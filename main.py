from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo
from carro_corrida import CarroCorrida

def test_drive(carro):
  print(f"\n Testando {carro.__class__.__name__}: ")
  carro.acelerar()
  carro.exibir_velocidade()

if __name__ == "__main__":
  # Testando Carro Inteligente
  carro_inteligente = CarroInteligente(10)
  print("Carro inteligente: ")
  carro_inteligente.acelerar()
  carro_inteligente.exibir_velocidade()
  carro_inteligente.estacionar()
  print()

  # Testando carro_esportivo
  carro_esportivo = CarroEsportivo(50)
  print("Carro esportivo: ")
  carro_esportivo.turbo()
  carro_esportivo.exibir_velocidade()
  carro_esportivo.freiar()
  carro_esportivo.exibir_velocidade()

  # Testando Carro Corrida
  carro_corrida = CarroCorrida(100)



# criar uml