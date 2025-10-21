def addDec(func):
    def wrapper(*args,**kwargs):
        print("Starting addition...")
        a=func(*args,**kwargs)
        print(f"{args[0]}+{args[1]}={a}")
        print("Finished addition...")

    return wrapper

@addDec
def add(a,b):
    return a+b


add(1,2)
