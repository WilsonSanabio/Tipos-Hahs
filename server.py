import http.server
import socketserver
import webbrowser
import threading
import os
import sys
import keyboard  # Captura de tecla

# Instale a biblioteca keyboard (se ainda não tiver):
# pip install keyboard

PORTA = 8000
ARQUIVO_HTML = sys.argv[1] if len(sys.argv) > 1 else "index.html"

class MeuHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/encerrar':
            self.send_response(200)
            self.end_headers()
            threading.Thread(target=encerrar_servidor).start()
        else:
            self.send_error(404)

def abrir_navegador():
    url = f"http://localhost:{PORTA}/{ARQUIVO_HTML}"
    webbrowser.open(url)

def iniciar_servidor():
    global httpd
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    httpd = socketserver.TCPServer(("", PORTA), MeuHandler)
    print(f"Servidor rodando em http://localhost:{PORTA}/")
    abrir_navegador()
    httpd.serve_forever()

def encerrar_servidor():
    print("Encerrando servidor...")
    httpd.shutdown()

# Inicia o servidor em uma thread
threading.Thread(target=iniciar_servidor).start()

# Aguarda pressionar ESC para encerrar
print("Pressione ESC para encerrar o servidor.")
keyboard.wait('esc')
encerrar_servidor()
