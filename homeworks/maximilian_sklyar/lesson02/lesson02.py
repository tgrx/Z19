import platform
import const


def choose():
    try:
        run = int(input("Choose what you want to run (1 - 5): "))
        if 0 < run < 6:
            if run == 1:
                print("Hello World!")
            if run == 2:
                output = ""
                for key, val in const.about_me.items():
                    output += "{key}: {val} \n".format(key=key.capitalize(), val=val)
                print(output)
            if run == 3:
                print("System: {system}".format(system=platform.system()))
            if run == 4:
                username = input("What's is your name: ")
                print("Hello, {username}. Have a nice day!".format(username=username))
            if run == 5:
                choose()
        else:
            choose()
    except ValueError:
        print("Incorrect value")
    return


choose()
