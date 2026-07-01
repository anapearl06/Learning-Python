chai_type = "Plain Chai"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Cardamom Chai"
    kitchen()

front_desk()
print(f"After the kitchen update: {chai_type}") 