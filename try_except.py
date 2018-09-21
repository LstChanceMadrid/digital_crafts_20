while True:
    try:
        x = int(input("Please enter a number: "))
        print("thank you!")
        break
    except ValueError:
        print("Not a valid number, try again...")


def this_fails():
    x = 1/0

try:
    this_falls()
except ZeroDivisionError as error_message:
    print('Handling run-time error', error_message) 