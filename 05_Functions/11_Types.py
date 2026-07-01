def pure_chai(cups):
    return cups * 10

total_chai = 1

def impure_chai(cups):
    global total_chai
    total_chai += cups * 10

pure_chai(3)
print(total_chai)  

def pour_chai(N):
    if N == 0:
        return
    return pour_chai(N - 1) 

print(pour_chai(3))  # This will print None since the function does not return anything

chai_type = ["Masala", "Ginger", "Cardamom", "Masala"]

strong_chai = list(filter(lambda chai: chai == "Masala", chai_type))
print(strong_chai)  # This will print ['Masala', 'Masala']  

