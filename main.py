from time import sleep
from os import system
from string import ascii_uppercase as asciiLetters
from random import randint

# assigning values to every possible character
values = {}
for i in range(0, 10 + len(asciiLetters)):
    if i < 10:
        values[i] = str(i)
    else:
        values[i] = str(asciiLetters[i - 10])


def auto():
    """
    Calculates random number to every possible numeric system

    Returns:
        None
    """
    while True:
        system("cls")
        randomInt = randint(10, 10000)

        print("Generated number: " + str(randomInt))
        print("")

        # from dec to any system
        for numSystem in range(2, 36):
            print(str(numSystem) + ": ", end="")
            num = ""
            tempInt = randomInt

            if numSystem != 10:
                while tempInt >= numSystem:
                    num += str(values.get(tempInt % numSystem))
                    tempInt //= numSystem

                num += str(values.get(tempInt % numSystem))

                print(num[::-1])
            else:
                print(randomInt)
        break

    while True:
        print("\nWhat next?\n1: Menu\n2: Continue\n3: Exit")
        autoMenuOption = input("Choose an option: ")

        if autoMenuOption in ('1', '2', '3'):
            if autoMenuOption == '1':
                main()
            elif autoMenuOption == '2':
                auto()
            elif autoMenuOption == '3':
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


def manual():
    """
    Converts from one to second numeric system depending on user input

    Returns:
        None
    """
    while True:
        try:
            system("cls")
            print(rules)
            number = input("Enter a number in numeric system from 2 to 35: ")
            number = number.upper()
            dictKeys = list(values.keys())
            dictValues = list(values.values())
            conditional = True
            result = 0
            numSytem = int(input("Enter numeric system of the number(2 - 35): "))

            if numSytem in range(2, 36):
                for k in range(numSytem, len(values)):
                    if number.find(values.get(k)) >= 0:
                        conditional = False
                        system("cls")
                        print("Forbidden value found in the number! Enter a different number!")
                        sleep(1)
                        break
                if conditional:
                    if numSytem != 10:
                        number = number[::-1]
                        for char in range(len(number) - 1, -1, -1):
                            result += numSytem ** char * (dictKeys[dictValues.index(number[char])])
                    else:
                        result = number

                    while True:
                        chosenNumSystem = int(input("Enter a chosen numeric system to transform the number: "))
                        if chosenNumSystem in range(2, 36):
                            number = int(result)
                            result = ""

                            while number >= chosenNumSystem:
                                result += str(values.get(number % chosenNumSystem))
                                number //= chosenNumSystem

                            result += str(values.get(number % chosenNumSystem))
                            break
                        else:
                            system("cls")
                            print("Forbidden numeric system! Try again!")
                            sleep(1)

                        system("cls")

                    print("Your number:", result[::-1])

                    while True:
                        print("\nWhat next?\n1: Menu\n2: Continue\n3: Exit")
                        manualMenuOption = input("Choose an option: ")

                        if manualMenuOption in ('1', '2', '3'):
                            if manualMenuOption == '1':
                                main()
                            elif manualMenuOption == '2':
                                manual()
                            elif manualMenuOption == '3':
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
    """
    Menu handler, returns entire menu when it's needed

    Returns:
        Multiline string (menu)
    """
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


def main():
    """
    Script start handler

    Returns:
        None
    """
    while True:
        system("cls")
        print(menu())
        startOption = input("    Choose a mode to start a program: ")

        if startOption in ('1', '2', '3'):
            if startOption == '1':
                auto()
            elif startOption == '2':
                manual()
            elif startOption == '3':
                exit(-1)
        else:
            system("cls")
            print("Option doesn't exist! Choose a different option")
            sleep(1)


if __name__ == "__main__":
    main()
