import socket
import threading

def listen_to_broker(sock):
    try:
        while True:
            msg= sock.recv(1024)
            if not msg:
                break
            print(msg.decode())
    except:
        print("[!] Conexión cerrada por el broker")

def main():
    broker_host = '0.0.0.0'
    broker_port = 14000
    topic = input("tema a suscribirse").strip
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((broker_host, broker_port))
    sock.sendall(f"SUB{topic}".encode())
    print(f"[SUSCRTIPTOR] suscrito al tema: '{topic}'. Escuchando mensajes...")
    trhead = threading.Thread(target=listen_to_broker, args=(sock,), daemon=True).start()
    try:
        while True:
            pass  # Mantener el hilo principal activo
    except KeyboardInterrupt:
        print("\n[SUSCRIPTOR] Saliendo...")
    finally:
        sock.close()

if __name__ == "__main__":
    main()