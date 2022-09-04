import argparse
import json
from turtle import color


class colors:
    RED = "\033[91m"
    WHITE = "\033[0m"
    CYAN = "\033[96m"
    GREEN = "\033[32m"


def food():
    food = json.load(open("food.json"))

    print(colors.RED + "Total: " + str(len(food.keys())))
    for item in food.keys():
        print(colors.CYAN + str(item.upper()) + " (" + food[item]["rating"] + ")")
        print(colors.WHITE + ", ".join(food[item]["recommendations"]))
    return

def content():
    content = json.load(open("content.json"))

    for type in content.keys():
        print("\n" + colors.CYAN + type.upper() + " (" + str(len(content[type])) + ")")
        for item in content[type]:
            if item["rating"] == "":
                print(colors.RED + "(Pending) Title: " + item["title"] + " (Rating: " + item["rating"] + ")" + colors.WHITE)
            elif item["rating"] == "-":
                print(colors.GREEN + "(Watching) Title: " + item["title"] + " (Rating: " + item["rating"] + ")" + colors.WHITE)
            else:
                print(colors.WHITE + "Title: " + item["title"] + " (Rating: " + item["rating"] + ")")
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--rating", default="-")
    
    type = parser.parse_args().type
    if type == "food":
        food()
    elif type == "content":
        content()
    else:
        print("Command not found")
    return


if __name__ == "__main__":
    main()
