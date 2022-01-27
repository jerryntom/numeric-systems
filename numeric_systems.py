from time import sleep
from os import system
from string import ascii_uppercase as ascii_letters
from random import randint

# assigning values to every possible character
values = {}
for i in range(0, 10 + len(ascii_letters)):
    if i < 10:
        values[i] = str(i)
    else:
        values[i] = str(ascii_letters[i - 10])


# generating random int in all numeric systems
def auto():
    while True:
        system("cls")
        random_int = randint(10, 10000)

        print("Generated number: " + str(random_int))
        print("")

        # from dec to any system
        for num_system in range(2, 36):
            print(str(num_system) + ": ", end="")
            num = ""
            temp_int = random_int

            if num_system != 10:
                while temp_int >= num_system:
                    num += str(values.get(temp_int % num_system))
                    temp_int //= num_system

                num += str(values.get(temp_int % num_system))

                print(num[::-1])
            else:
                print(random_int)
        break

    while True:
        print("\nWhat next?\n1: Menu\n2: Continue\n3: Exit")
        option_auto = input("Choose an option: ")

        if option_auto in ('1', '2', '3'):
            if option_auto == '1':
                main()
            elif option_auto == '2':
                auto()
            elif option_auto == '3':
                exit()
        else:
            system("cls")
            print("Option doesn't exist! Choose a different option")
            sleep(1)

        system("cls")


# generating rules for manual mode
rules = """
--- IF YOU DON'T WANT TO START FROM BEGIN READ THIS --- 
1: Number should be build from chars available in specified numer system 
2: Numeric system should be in range from 2 to 35
3: Number should be build from digits and letters

Possible chars in every numeric system:"""

for i in range(2, 36):
    rules += "\n"
    rules += str(i) + " - "
    for j in range(0, i):
        rules += values.get(j) + " "

rules += "\n"


# converting numeric systems by user
def manual():
    while True:
        try:
            system("cls")
            print(rules)
            number = input("Enter a number in numeric system from 2 to 35: ")
            number = number.upper()
            dict_keys = list(values.keys())
            dict_values = list(values.values())
            conditional = True
            result = 0
            numeric_system = int(input("Enter numeric system of the number(2 - 35): "))

            # from any system to dec and then to chosen system
            if numeric_system in range(2, 36):
                for k in range(numeric_system, len(values)):
                    if number.find(values.get(k)) >= 0:
                        conditional = False
                        system("cls")
                        print("Forbidden value found in the number! Enter a different number!")
                        sleep(1)
                        break
                if conditional:
                    if numeric_system != 10:
                        number = number[::-1]
                        for char in range(len(number) - 1, -1, -1):
                            result += numeric_system ** char * (dict_keys[dict_values.index(number[char])])
                    else:
                        result = number

                    while True:
                        chosen_numeric_system = int(input("Enter a chosen numeric system to transform the number: "))
                        if chosen_numeric_system in range(2, 36):
                            number = int(result)
                            result = ""

                            while number >= chosen_numeric_system:
                                result += str(values.get(number % chosen_numeric_system))
                                number //= chosen_numeric_system

                            result += str(values.get(number % chosen_numeric_system))
                            break
                        else:
                            system("cls")
                            print("Forbidden numeric system! Try again!")
                            sleep(1)

                        system("cls")

                    print("Your number:", result[::-1])

                    while True:
                        print("\nWhat next?\n1: Menu\n2: Continue\n3: Exit")
                        option_auto = input("Choose an option: ")

                        if option_auto in ('1', '2', '3'):
                            if option_auto == '1':
                                main()
                            elif option_auto == '2':
                                manual()
                            elif option_auto == '3':
                                exit()
                        else:
                            system("cls")
                            print("Option doesn't exist! Choose a different option")
                            sleep(1)

                        system("cls")
            else:
                system("cls")
                print("Forbidden numeric system! Try again!")
                sleep(1)
        except Exception:
            system("cls")
            print(rules)
            input("Error! Press enter to start again...")


def menu():
    return """
       ▄     ▄   █▀▄▀█ ▄███▄   █▄▄▄▄ ▄█ ▄█▄           ▄▄▄▄▄ ▀▄    ▄  ▄▄▄▄▄      ▄▄▄▄▀ ▄███▄   █▀▄▀█    ▄▄▄▄▄   
        █     █  █ █ █ █▀   ▀  █  ▄▀ ██ █▀ ▀▄        █     ▀▄ █  █  █     ▀▄ ▀▀▀ █    █▀   ▀  █ █ █   █     ▀▄ 
    ██   █ █   █ █ ▄ █ ██▄▄    █▀▀▌  ██ █   ▀      ▄  ▀▀▀▀▄    ▀█ ▄  ▀▀▀▀▄       █    ██▄▄    █ ▄ █ ▄  ▀▀▀▀▄   
    █ █  █ █   █ █   █ █▄   ▄▀ █  █  ▐█ █▄  ▄▀      ▀▄▄▄▄▀     █   ▀▄▄▄▄▀       █     █▄   ▄▀ █   █  ▀▄▄▄▄▀    
    █  █ █ █▄ ▄█    █  ▀███▀     █    ▐ ▀███▀                ▄▀                ▀      ▀███▀      █             
    █   ██  ▀▀▀    ▀            ▀                                                               ▀              

    -------------------------------------------------|
    1: Random number in all available numeric systems|
    2: Convert from one to another system            |
    3: Exit                                          |
    -------------------------------------------------|"""


# script handler
def main():
    while True:
        system("cls")
        print(menu())
        option = input("    Choose a mode to start a program: ")

        if option in ('1', '2', '3'):
            if option == '1':
                auto()
            elif option == '2':
                manual()
            elif option == '3':
                exit(-1)
        else:
            system("cls")
            print("Option doesn't exist! Choose a different option")
            sleep(1)


main()
