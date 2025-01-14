elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
print("elements: ", elements)

# def funct_name():
#     return True

# def say_greeting(name, message):
#     print(f"{message}, {name}")
#
# say_greeting("Heemal")
def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(print))
        except ValueError:
            print("Error: Please enter a valid interger!")
            continue
