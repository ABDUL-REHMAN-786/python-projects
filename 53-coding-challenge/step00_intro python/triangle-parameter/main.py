# ## Problem Statement

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3 

# What is the length of side 2? 4 

# What is the length of side 3? 5.5 

# The perimeter of the triangle is 12.5

def main():

    side1:str = input("What is the length of side 1? ")
    side1:float = float(side1)

    side2:str = input("What is the length of side 2? ")
    side2: float = float(side2)

    side3:str = input("What is the length of side 3? ")
    side3: float = float(side3)

    total: float = side1 + side2 + side3

   
    print("The perimeter of the triangle is " + str(total))



if __name__ == '__main__':
    main()