import socket
import threading

# Dirección y puerto del servidor al que conectarse
HOST = '127.0.0.1'
PORT = 12345

# Función para recibir mensajes del servidor
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Mensaje recibido: {message.decode()}")
            else:
                break
        except:
            break

# Función para enviar mensajes al servidor
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    # Hilos para recibir y enviar mensajes
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    
    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    start_client()
