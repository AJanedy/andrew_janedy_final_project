# Andrew Janedy Final Project

# Main menu displaying the three functions of this program
def menu():
    print()
    print("Please select from the following menu:")
    print()
    print("1: Calculate Compound Interest")
    print("2: Reverse List")
    print("3: Draw Some Triangles")
    print()
    selection = input("Please select the number of the function you would like to perform: ")

    return selection

# Recursive interest calculator menu / called upon original selection
# Takes 3 inputs as the function called from here has 3 parameters
def interest_calculator_menu():

    print()
    amount = input("How much is the initial investment?  Use only numbers and decimals: ")
    print("What is the interest rate?  Use only numbers and decimals.")
    print("Example, for a 5% interest rate, type .05 or 0.05.")
    interest_rate = input("For a 50% interest rate, type .5 or 0.5: ")
    years = input("How many years will this be invested?  Use only whole numbers: ")

    return recursive_interest_calculator(amount, interest_rate, years)

# Recursive interest calculator / takes 3 parameters
# Calculates interest and continues upon itself until years remaining = 0
def recursive_interest_calculator(amount, interest_rate, years):

    principle = float(amount)
    rate_of_interest = float(interest_rate)
    years_to_calculate = int(years)
    new_principle = principle
    new_principle += principle * rate_of_interest

    if years == 0:
        return amount
    else:
        return recursive_interest_calculator(new_principle, rate_of_interest, years_to_calculate - 1)

# Reverses the order of a list created from a .txt file using recursion
def reverse_list(list):
    if list == []:
        return None
    else:
        print(list[-1])
        reverse_list(list[:-1])

# Recursive triangle artist menu, asks user how big to draw the triangle
# Calls draw_triangle function with size parameter
def draw_triangles_menu():
    print()
    print("How big would you like the triangle to be?")
    triangle_size = input("Please enter a whole number: ")
    print()
    draw_triangles(triangle_size)

# Recursive triangle artist function
# Parameter is the size of the desired triangle
# Calls upon itself until triangle size = 0
def draw_triangles(triangle_size):
    if int(triangle_size) == 0:
        return None
    else:
        print("#" * int(triangle_size))
        return draw_triangles(int(triangle_size) - 1)

# Main function, calls menu which then returns the selection
# Basic check statements determines desired function
def main():
    selection = menu()

    if int(selection) == 1:
        result = interest_calculator_menu()
        new_result = round(result, 2)
        print(new_result)

    if int(selection) == 2:
        data_list = []
        data = open("Numbers.txt", 'r')
        data_lines = data.readlines()
        for line in data_lines:
            data_list.append(line)
        reverse_list(data_list)

    if int(selection) == 3:
        draw_triangles_menu()

main()