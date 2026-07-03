class Coffee:
    pass

class Coffee_Time:
    pass

print(type(Coffee))  # <class '__main__.Coffee'>
print(type(Coffee_Time))  # <class '__main__.Coffee_Time'>

Capacinuo = Coffee()
print(type(Capacinuo))  
print(type(Capacinuo) is Coffee)  # True
print(type(Capacinuo) is not Coffee)  # False