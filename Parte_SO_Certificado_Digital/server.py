import http.server
import socketserver
import ssl

# Configurações do servidor
PORT = 8080  # Porta em que o servidor vai rodar
DIRECTORY = "."


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'  # Página padrão para servir
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Inicia o servidor usando ThreadingTCPServer
with socketserver.ThreadingTCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    # Configuração do SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    # Envolvendo o socket do servidor com SSL usando SSLContext
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"Servidor HTTPS iniciado na porta {PORT}. Acesse https://localhost:{PORT}")
    httpd.serve_forever()