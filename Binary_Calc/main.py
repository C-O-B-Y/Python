# Converts Integers and strings to binary format

print("Type : exit() at any time to exit the program...")

def main():
    # Get the value to convert from the user
    data = input("Input value to convert: ")

    if (data == "exit()"):
        exit()

    try:
        # try to convert user input to type of int
        data = int(data)
    except ValueError:
        # fails if not an int
        pass

    # set data type
    data_type = type(data)

    if (data_type == int):
        # if type int print the binary value of the int
        print(str(data) + " = " + calculateBinary(data))
    elif (data_type == str):
        # if type str convert to list of chars
        chars = list(data)
        # loop throught all the chars
        for x in chars:
            # print the deci and binary value for the char
            print(str(x) + " = " + str(getDeci(x)) + " : " + calculateBinary(getDeci(x)))

    # loop through the main function to keep using the program
    main()

def getDeci(x):
    # return the deci value of the input
    return ord(x)

def calculateBinary(x):
    bin_x = bin(x)
    # return binary value of the input
    return bin_x

if __name__ == '__main__':
    main()
