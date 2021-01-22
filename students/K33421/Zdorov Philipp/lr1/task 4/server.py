import socket
import asyncio


class Server:
    def __init__(self):
        self.connections = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', 9090))
        self.sock.listen(10)
        self.sock.setblocking(False)
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.run())

    async def _handle_connection(self, conn, addr):
        while True:
            request = await self.loop.sock_recv(conn, 128)
            request = request.decode()
            print(f'{addr}: {request}')
            print(len(self.connections))

            for c in self.connections:
                if c != conn:
                    await self.loop.sock_sendall(c, request.encode())

            if request == '/quit':
                self.connections.remove(conn)
                conn.close()
                break

    async def run(self):
        while True:
            conn, addr = await self.loop.sock_accept(self.sock)
            print(addr)
            if conn not in self.connections:
                self.connections.append(conn)
                self.loop.create_task(self._handle_connection(conn, addr))


if __name__ == '__main__':
    server = Server()
