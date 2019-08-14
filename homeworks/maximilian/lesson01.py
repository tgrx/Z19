import platform


def hello_world():
    print("Hello World! \r\n")


def print_info():
    about_me = {"first_name": "Maximilian", "last_name": "Sklyar", "age": "25", "phone": "+375 29 560-46-07",
                "email": "maximilian.sklyar@gmail.com"}
    output = ""
    for key, val in about_me.items():
        output = output + key.capitalize() + ": " + val + "\r\n"
    print(output)


def print_sys_info():
    print("System: ", platform.platform(), "\r\n")


def print_username():
    username = input("What's is your name: ")
    print("Hello, ", username, ". Have a nice day! \r\n")


def choose():
    run = int(input("Choose what you want to run (1 - 5): "))

    if run == 1:
        hello_world()
    if run == 2:
        print_info()
    if run == 3:
        print_sys_info()
    if run == 4:
        print_username()
    if run == 5:
        choose()


choose()