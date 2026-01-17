import datetime
# Cleanup test
def greet(name):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
<<<<<<< HEAD

    return f"Shalom!!, {name}! The current time is {current_time}."
=======
    return f"Hello, {name}! The current time is {current_time}."
>>>>>>> parent of 0b8c81e (Update Hello to Shalom on main)


if __name__ == "__main__":
    user = "World"
    print(greet(user))
