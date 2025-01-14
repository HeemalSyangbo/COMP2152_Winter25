elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
print("elements: ", elements)

# def funct_name():
#     return True

# def say_greeting(name, message="hi"):
#     print(f" {message}, {name}")
# say_greeting("Heemal")
# say_greeting("Heemal", "Hello"
def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(print))
        except ValueError:
            print("Error: Please enter a valid integer!")
            continue


try:
    elements_selected = get_valid_int_input("Enter the index of the element you like")
    # Roll dice
    elementRoll = random.randint(1, 6)
    totalNum = elements_selected + elementRoll

    # Print  the result base on the totalNum
    if elementRoll <= 2:
        print("You rolled a weak element, friend")
    elif elementRoll <= 4:
        print("You rolled a medium element, friend")
    else:
        print("You rolled a strong element, friend")


except Exception as e:
    print("")
