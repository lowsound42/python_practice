class Cookie:
    def __init__(self, flavour):
        self.flavour = flavour

    def get_flavour(self):
        return self.flavour

    def set_flavour(self, new_flavour):
        self.flavour = new_flavour


cookie_one = Cookie("chocolate")
print(cookie_one.get_flavour())
cookie_one.set_flavour("banana")
print(cookie_one.get_flavour())
