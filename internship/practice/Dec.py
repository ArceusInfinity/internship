def new_dec(func):
    print("hello")
    func()
    print("goodbye")

@new_dec
def need_dec():
    print("this is decorator")
