import subprocess
import sys

def lanzar_servidor():
    print("Iniciando servidor...")
    subprocess.run(["python", "servidor.py"])

def lanzar_cliente():
    print("Iniciando cliente...")
    subprocess.run(["python", "cliente.py"])

def main():
    if len(sys.argv) != 2:
        print("Uso: python lanzador.py [servidor|cliente]")
        sys.exit(1)

    if sys.argv[1] == "servidor":
        lanzar_servidor()
    elif sys.argv[1] == "cliente":
        lanzar_cliente()
    else:
        print("Argumento no válido. Usa 'servidor' o 'cliente'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
