def add_its_me(str):
    def wrapped():
        return str()+",it's me!"
    return wrapped

def add_u_sym(u):
    def wrapped():
        return "<u>"+ u() + "</u>"
    return wrapped


@add_u_sym
@add_its_me
def Hi_fun():
    return 'Hi'
print(Hi_fun())

