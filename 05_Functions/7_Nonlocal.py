def update_order():
    chai_type ="Elaichi Chai"

    def kitchen():
        nonlocal chai_type
        chai_type = "Tulsi Chai"
    kitchen()
    print(f"After the kitchen update: {chai_type}")