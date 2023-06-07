class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    total = 0

    def __init__(self):
        self.ip = self.create_ip()
        self.buffer = []
        self.router = None

    @classmethod
    def create_ip(cls):
        cls.total += 1
        return cls.total

    def get_ip(self):
        return self.ip

    def get_data(self):
        result = self.buffer.copy()
        self.buffer.clear()
        return result

    def send_data(self, data):
        self.router.buffer.append(data)


class Router:
    buffer = []
    info = {}

    def link(self, server):
        setattr(server, 'router', self)
        self.info[server.ip] = server

    def unlink(self, server):
        if self.info.get(server.ip, None):
            setattr(server, 'router', None)
            del self.info[server.ip]

    def send_data(self):
        for item in self.buffer:
            if self.info.get(item.ip, None):
                self.info[item.ip].buffer.append(item)
        self.buffer.clear()


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()


def main():
    print('Session started')


if __name__ == '__main__':
    main()