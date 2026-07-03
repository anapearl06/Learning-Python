# Smart Token Dispenser

def token_dispenser(start=1):
    token = start

    try:
        while True:
            new_token = yield token

            if new_token is not None:
                token = new_token
            else:
                token += 1
    except GeneratorExit:
        print("Dispenser closed.")


# Example
dispenser = token_dispenser(1)

print(next(dispenser))      # 1
print(next(dispenser))      # 2
print(dispenser.send(10))   # 10
print(next(dispenser))      # 11

dispenser.close()