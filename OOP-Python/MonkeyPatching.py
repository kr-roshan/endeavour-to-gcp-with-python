class Monkey:
    def patch(self):
        print("Monkey Patched!")
    
def monk(self):
    print("Monk!")

Monkey.patch = monk

m = Monkey()
m.patch()





