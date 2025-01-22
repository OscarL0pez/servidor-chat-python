# Servidor de Chat en Python

Este es un servidor de chat multijugador básico escrito en Python. Permite a los usuarios conectarse y enviar mensajes en tiempo real. Este proyecto está diseñado como una práctica para entender la programación de redes y la creación de servidores en Python.

## Requisitos

- Python 3.x
- Módulos:
  - `socket` (incluido en la biblioteca estándar de Python)
  - `threading` (también incluido en la biblioteca estándar)

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/OscarL0pez/servidor-chat-python.git

2. **Navega al directorio del proyecto:**
  cd servidor-chat-python

3. **Ejecuta el servidor:**
    python servidor.py

4. **Ejecuta el cliente:**
    python cliente.py

**Cómo funciona**
El servidor (servidor.py) escucha las conexiones entrantes de los clientes.
Los clientes pueden conectarse al servidor y enviar mensajes.
El servidor maneja múltiples clientes simultáneamente mediante subprocesos (threads), permitiendo que varios clientes se comuniquen al mismo tiempo.
Los mensajes enviados por un cliente se transmiten a todos los demás clientes conectados.

**Archivos del Proyecto**
servidor.py: El archivo principal que contiene el código para el servidor.
cliente.py: El archivo cliente que se conecta al servidor y envía/recibe mensajes.
lanzador.bat: Un archivo para ejecutar el servidor y cliente en Windows de manera sencilla.
lanzador.py: Un script Python para lanzar tanto el servidor como el cliente, si prefieres no usar el archivo .bat.
