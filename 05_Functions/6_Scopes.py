def serve_chai():
    chai_type = "Masala Chai"
    print(f"Serving {chai_type}")

    chai_type = "Ginger Chai"
    print(f"Serving {chai_type}")

    chai_type = "Cardamom Chai"
    print(f"Serving {chai_type}")

    chai_type = "Tulsi Chai"    
    print(f"Serving {chai_type}")

    chai_type = "Lemon Chai"
    serve_chai()
    print(f"Outside the function: {chai_type}")


def chai_counter():
    chai_order = "Masala Chai"
    def print_order():
        chai_order = "Ginger Chai"
        print(f"Inside the nested function: {chai_order}")
    print_order()
    print("outer:", chai_order)

chai_order = "Cardamom Chai"
chai_counter()
print("Global:", chai_order)
