import random
import os
def clear():
  """There are many alternatives to clearing the console, this is just one."""
  os.system('cls' if os.name == 'nt' else 'clear')
print('\n' * os.get_terminal_size().lines)
clear()
while True:
    print("Virtual Die Roller")
    print("0. Toss Coin \n1. Tetrahedron (4-sided die) \n2. Cube (6-sided die) \n3. Octahedron (8-sided die) \n4. Pentagonal Trapezohedron (10-sided die) \n5. Dodecahedron (12-sided die) \n6. Icosahedron (20-sided die) \n7. Exit")
    Q = input("Enter the number of the die you need: ")
    clear()
    if Q == '0':
        print('0 = Heads \n1 = Tails')
        print("Tossing...")
        print(random.randint(0,1))
        while True:
            R = input("Would you like to toss again? Y/N?: ")
            if R == "Y" or R == "y":
                clear()
                print('0 = Heads \n1 = Tails')
                print("Tossing...")
                print(random.randint(0,1))
                continue
            elif R == "N" or R == "n":
                clear()
                break
            else:
                clear()
                print("Not even in the choices dude...\n")
                break
    elif Q == '1':
        print("Rolling...")
        print(random.randint(1,4))
        while True:
            R = input("Would you like to roll again? Y/N?: ")
            if R == "Y" or R == "y":
                clear()
                print("Rolling...")
                print(random.randint(1,4))
                continue
            elif R == "N" or R == "n":
                clear()
                break
            else:
                clear()
                print("Not even in the choices dude...\n")
                break
    elif Q == '2':
        print("Rolling...")
        print(random.randint(1,6))
        while True:
            R = input("Would you like to roll again? Y/N?: ")
            if R == "Y" or R == "y":
                clear()
                print("Rolling...")
                print(random.randint(1,6))
                continue
            elif R == "N" or R == "n":
                clear()
                break
            else:
                clear()
                print("Not even in the choices dude...\n")
                break
    elif Q == '3':
        print("Rolling...")
        print(random.randint(1,8))
        while True:
            R = input("Would you like to roll again? Y/N?: ")
            if R == "Y" or R == "y":
                clear()
                print("Rolling...")
                print(random.randint(1,8))
                continue
            elif R == "N" or R == "n":
                clear()
                break
            else:
                clear()
                print("Not even in the choices dude...\n")
                break
    elif Q == '4':
        print("Rolling...")
        print(random.randint(1,10))
        while True:
            R = input("Would you like to roll again? Y/N?: ")
            if R == "Y" or R == "y":
                clear()
                print("Rolling...")
                print(random.randint(1,10))
                continue
            elif R == "N" or R == "n":
                clear()
                break
            else:
                clear()
                print("Not even in the choices dude...\n")
                break
    elif Q == '5':
        print("Rolling...")
        print(random.randint(1,12))
        while True:
            R = input("Would you like to roll again? Y/N?: ")
            if R == "Y" or R == "y":
                clear()
                print("Rolling...")
                print(random.randint(1,12))
                continue
            elif R == "N" or R == "n":
                clear()
                break
            else:
                clear()
                print("Not even in the choices dude...\n")
                break
    elif Q == '6':
        print("Rolling...")
        print(random.randint(1,20))
        while True:
            R = input("Would you like to roll again? Y/N?: ")
            if R == "Y" or R == "y":
                clear()
                print("Rolling...")
                print(random.randint(1,20))
                continue
            elif R == "N" or R == "n":
                clear()
                break
            else:
                clear()
                print("Not even in the choices dude...\n")
                break
    elif Q == '7':
        clear()
        q = input("Are you sure? Y/N: ")
        if q == "Y" or q == "y":
            print("Good game! Smell ya later!")
            exit()
        elif q == "N" or q == "n":
            clear()
            continue
        else:
            clear()
            print("Not even in the choices dude...\n")
            break
    else:
        clear()
        print("Not even in the choices dude...\n")
        continue
