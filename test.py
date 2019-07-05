

def say_it_twice(f):
    def twice():
        f()
        f()
    return twice


@say_it_twice
def say_myname():
    print("my name is sadig")


say_myname()