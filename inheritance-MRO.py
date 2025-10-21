class A:
    def call(self):
        print("I am A")

class B:
    def call(self):
        print("I am B")

class C(A,B):
    # def call(self):
    #     print("I am C")
    pass
a = C()
a.call()