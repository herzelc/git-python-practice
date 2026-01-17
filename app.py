import datetime

def greet(name):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    return f"Shalom!!, {name}! The current time is {current_time}."

>>>>>>> feature/add-time

if __name__ == "__main__":
    user = "World"
    print(greet(user))
