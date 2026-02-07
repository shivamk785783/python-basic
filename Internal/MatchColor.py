color = input("enter color: ")
match color:
    case "green":
        print("green")
    case "yellow":
        print("Look")
    case "Red":
        print("stop")  
    case _:
        print("wrong color!")      