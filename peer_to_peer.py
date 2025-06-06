from concurrent.futures import thread
import socket 
import threading
import sys
import time

from matplotlib.pylab import f

#funcion para manejar conexionen entrantes
def handle_peer(conn, addr):
    try:
        print(f"Conexión establecida con {addr}")
        data = conn.recv(1024).decode()
        print(f"{addr}-> {data}")
        conn.sendall(f"echo desde {conn.getsockname()}: {data}".encode())

    except Exception as e:
        print(f"Error al manejar la conexión con {addr}: {e}")
    finally:
        conn.close()
        print(f"Conexión con {addr} cerrada")


#Sercidor que escucha conexiones entrantes
def peer_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)   
    print(f"Nodo escuchando en el puerto {port}...")
    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_peer, args=(conn, addr))
        thread.start()
#cliente que envia mensajes a otros peers

def connect_to_peers(peers, message):
    for host, port in peers:
        try:
           with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                sock.sendall(message.encode())
                response = sock.recv(1024).decode()
                print(f"Respuesta de {host}:{port} <- {response}")
        except Exception as e:
            print(f"Error al conectar con {host}:{port} - {e}")

#main

if main == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python peer_to_peer.py <mi_puerto> <peer1_host:port> [peer2_host:port] ...")
        sys.exit(1)

    my_port = int(sys.argv[1])
    peers = [tuple(p.split(":")) for p in sys.argv[2:]]
    peers = [(h, int(p)) for h, p in peers if int (p) != my_port] 

    # Iniciar el servidor en un hilo
    threading.Thread(target=peer_server, args=(my_port,), daemon=True).start()

    # Esperar un momento para asegurarse de que el servidor esté listo
    time.sleep(1)

    # Enviar mensajes a los peers
    while True:
        message = input("Ingrese un mensaje para enviar a los peers (o 'exit' para salir): ")
        if message.lower() == 'exit':
            break
        connect_to_peers(peers, message)
            
       
