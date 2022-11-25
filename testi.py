class Router:
    def __init__(self):
        self.buffer = []
        self.slovar_podkl = {}

    def link(self, server):
        self.slovar_podkl[server.ip] = server
        server.router = self

    def unlink(self, server):
        s = self.slovar_podkl.pop(server.ip, False)
        if s:
            s.router = None

    def send_data(self):
        for pack in self.buffer:
            if pack.ip in self.slovar_podkl:
                self.slovar_podkl[pack.ip].buffer.append(pack)
        self.buffer.clear()


class Server:

    count_ip = 0

    def __init__(self):
        self.buffer = []
        Server.count_ip += 1
        self.ip = Server.count_ip
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        s = self.buffer[:]
        self.buffer.clear()
        return s

    def get_ip(self):
        return self.ip


class Data:

    def __init__(self, msg, ip):
        self.data = msg
        self.ip = ip