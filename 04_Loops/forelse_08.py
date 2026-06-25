staff = [("Christian", 35), ("Anathesia", 30)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is elegible to manage..")
        #break
    else:
        print(f"No one is elegible for managing")
