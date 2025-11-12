mark = 100

match mark:
    case mark if mark < 0 or mark > 100:
        print("Invalid mark")
    case mark if mark >= 70:
        print("First Class Honours")
    case mark if mark >= 50:
        print("Second Class Honours")
    case mark if mark >= 40:
        print("Pass")
    case _:
        print("No Award")