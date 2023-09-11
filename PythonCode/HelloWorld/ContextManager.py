# https://www.geeksforgeeks.org/context-manager-in-python/
# https://realpython.com/python-with-statement/
# https://www.learndatasci.com/solutions/python-context-managers/

class ContextManager:
    def __init__(self, managerName):
        # first call
        print("ContextManager.__init__()")
        self.Name = managerName

    def __enter__(self):
        # second call
        print("ContextManager.__enter__()")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # last call
        print("ContextManager.__exit__()")

with ContextManager("Roshan") as manager:
    # called after enter
    print(manager.Name)

# creating object only calls init
cm = ContextManager("Roshan Kumar").__enter__()
print(cm.Name)

