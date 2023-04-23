import time
import random
import os
import sys

cookies = 0
display_cookies = 0
cps = 34
cookies_per_click = 1
cookie_clicks = 0

all_commands = {
    "   cookie balance OR cookies OR cookie bal": "Displays the amount of cookies you have.\n",
    "   exit": "Exits the program.\n",
    "   view <item-to-view>": "Views the price (if available, otherwise, shows how to get it), item discription, and "
        "item use (if available).\n",
    "   click": "Why is there a definition for this? It's pretty self-explanatory? This command clicks the cookie, "
        "duhhh!\n"
}

def reset():
    global cookies, cps, cookie_clicks, cookies_per_click
    cookies = 0
    cps = 0
    cookie_clicks = 0
    cookies_per_click = 1
    clear_console()

def click():
    global cookies, cookies_per_click, cookie_clicks
    double_chance = ((random.random() * 100) == 28)

    if cookies_per_click == 1:
        form_of_word_cookie = "cookie"
    else:
        form_of_word_cookie = "cookies"

    if double_chance:
        cookies += (cookies_per_click * 2)
        print(f"A glitch happened. We gave you {cookies_per_click * 2} {form_of_word_cookie}, twice the amount of "
              f"your cookies per click, to resolve it.")
    else: 
        cookies += cookies_per_click
        print(f"Added {cookies_per_click} {form_of_word_cookie} to your bank.")
    
    cookie_clicks += 1

def add_cps_loop():
    global cps, cookies, display_cookies

    cookies += cps / 75
    display_cookies = int(cookies)
    time.sleep(1/1000)

def clear_console():
     os.system("cls")

def format_all_commands():
    all_commands_formatted = ""
    for command, desc in all_commands.items():
        all_commands_formatted += f"{command}: {desc}"
    return all_commands_formatted

def get_user_input():
    inp = input("Enter your command (Enter \"help\" for all commands): ")
    match inp:
        case "clear":
            clear_console()
        case "click":
            click()
        case "cookie balance":
            print(display_cookies)
        case "cookies":
            print(cookies)
        case "cookie bal":
            print(display_cookies)
        case "exit":
            sys.exit()
        case "help":
            print(format_all_commands())
        case _: 
            print("Not recognized as a command. Enter \"help\" for all available commands.")

if __name__ == "__main__":
    clear_console()
    #reset()
    while True:
        get_user_input()
        add_cps_loop()
