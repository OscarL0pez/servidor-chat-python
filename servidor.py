import socket
import threading

# Dirección y puerto del servidor
HOST = '127.0.0.1'  # Dirección local
PORT = 12345  # Puerto para escuchar conexiones

# Lista de clientes conectados
clients = []

# Función para enviar un mensaje a todos los clientes
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

# Función para manejar la comunicación con cada cliente
def handle_client(client_socket):
    # Obtiene el nombre del cliente
    client_socket.send("Bienvenido al servidor de chat!".encode())
    
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Mensaje recibido: {message.decode()}")
                broadcast(message, client_socket)
            else:
                break
        except:
            break
    
    # Cuando un cliente se desconecta, lo eliminamos de la lista de clientes
    clients.remove(client_socket)
    client_socket.close()

# Función para configurar el servidor
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT}...")
    
    while True:
        # Acepta nuevas conexiones de clientes
        client_socket, client_address = server_socket.accept()
        print(f"Cliente {client_address} conectado.")
        
        # Agregar el cliente a la lista de clientes
        clients.append(client_socket)
        
        # Crear un nuevo hilo para manejar la comunicación con este cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
