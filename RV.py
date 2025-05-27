def Value(name):
    return f"Hi, {name}"


message = Value("YASH")
file = open("YASH.txt", "w")
file.write(message)
