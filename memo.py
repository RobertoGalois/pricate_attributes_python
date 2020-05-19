class Hello:
    def __init__(self):
        self._pouet = 42
        print('[+]Initialisation')

    @property
    def  pouet(self):
        print('[+]access to pouet')
        return self._pouet

    @pouet.setter
    def pouet(self, p_value):
        print('[+]setting pouet to ' + str(p_value))
        raise PermissionError("You are not authorized to modify [pouet] attribute")

    def salut(self):
        print(self.salut.__name__)

if __name__ == "__main__":
    obj = Hello()
    obj.salut()

    
