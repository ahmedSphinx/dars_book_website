import http.server
import ssl
import os

os.chdir('/Volumes/work/workpower2/dars_book_project/dars_book/website')
server_address = ('127.0.0.1', 8000)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Server running at https://myapp.local.com:8000/")
httpd.serve_forever()
