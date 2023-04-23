# import time
# import os

# total = 0
# increment_amount = 20000 / 75

# def add():
#     global total, increment_amount
#     for _ in range(1000):
#         total += increment_amount
#         shortened_amount = int(total)
#         print(shortened_amount)
#         time.sleep(1/1000)
#     add()

# add()

# # clearing the console - test
# user = input("")
# if user == "clear":
#     os.system("cls")

all_commands = {
    "cookie balance": "Displays the amount of cookies you have.",
    "exit": "Exits the program.",
    "view <item-to-view>": "Views the price (if available, otherwise, shows how to get it), item discription, and item "
        "use (if available)."
}

def format_all_commands():
    all_commands_formatted = ""
    for (command, desc) in all_commands.items():
        all_commands_formatted += f"{command}: {desc}\n"
    return all_commands_formatted

print(format_all_commands())

while True:
    a = 2 + 2