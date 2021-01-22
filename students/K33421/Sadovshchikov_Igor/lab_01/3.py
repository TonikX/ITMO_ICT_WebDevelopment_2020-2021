import socket
from functools import lru_cache
from urllib.parse import parse_qs, urlparse


MAX_LINE = 64*1024
MAX_HEADERS = 100

class SampleServer():

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
          server_socket.bind((self.host, self.port))
          server_socket.listen()

          while True:
            conn, addr = server_socket.accept()
            print('Connection from', addr)

            try:
              self.handle_client(conn)
            except Exception as e:
              print('Client serving failed', e)
        finally:
          server_socket.close()

    def handle_client(self, conn):

        while True:
            request = self.parse_request(conn)
            response = self.handle_request(request)
            self.send_response(conn, response)

    def parse_request(self, conn):
        rfile = conn.makefile('rb')
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
          raise Exception('Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        words = req_line.split()
        print(words)
        if len(words) != 3:
          raise Exception('Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
          raise Exception('Unexpected HTTP version')

        headers = self.parse_headers(rfile)

        return Request(method, target, ver, headers, rfile)

    def parse_headers(self, rfile):
        headers = []
        while True:
          line = rfile.readline(MAX_LINE + 1)
          if len(line) > MAX_LINE:
            raise Exception('Header line is too long')

          if line in (b'\r\n', b'\n', b''):
            break

          headers.append(line)
          if len(headers) > MAX_HEADERS:
            raise Exception('Too many headers')

          hdict = {}
          for h in headers:
            h = h.decode('iso-8859-1')
            k, v = h.split(':', 1)
            hdict[k] = v

        return hdict

    def handle_request(self, request):
        if request.path == '/':
            return self.handle_get_index(request)

    def handle_get_index(self, req):
        accept = req.headers.get('Accept')
        if 'text/html' in accept:
          contentType = 'text/html; charset=utf-8'
          body = self.read_html_file()

        else:
          return Response(406, 'Not Acceptable')

        body = body.encode('utf-8')
        headers = [('Content-Type', contentType),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def send_response(self, conn, resp):
        wfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))

        if resp.headers:
          for (key, value) in resp.headers:
            header_line = f'{key}: {value}\r\n'
            wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if resp.body:
          wfile.write(resp.body)

        wfile.flush()
        wfile.close()

    def read_html_file(self):
        with open('index.html', 'r') as f:
            return f.read()

class Request:
  def __init__(self, method, target, version, headers, rfile):
    self.method = method
    self.target = target
    self.version = version
    self.headers = headers
    self.rfile = rfile

  @property
  def path(self):
    return self.url.path

  @property
  @lru_cache(maxsize=None)
  def query(self):
    return parse_qs(self.url.query)

  @property
  @lru_cache(maxsize=None)
  def url(self):
    return urlparse(self.target)

class Response:
  def __init__(self, status, reason, headers=None, body=None):
    self.status = status
    self.reason = reason
    self.headers = headers
    self.body = body

if __name__ == '__main__':
    serv = SampleServer('localhost', 4000)
    serv.serve()
