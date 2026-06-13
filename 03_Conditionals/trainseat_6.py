seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")

    case "AC":
        print("AC - Proper Air conditioned, comfy journey")

    case "general":
        print("general - Cheapest option, no reservations")

    case "luxury":
        print("luxury - Premium seats and proper meals available, expensive")
   
    case _:
        print("Invalid seat type")
