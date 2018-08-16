def main():
    data = input("Input value to convert: ")

    try:
        data = int(data)
    except ValueError:
        pass

    data_type = type(data)

    if (data_type == int):
        print(calculateBinary(data))
    elif (data_type == str):
        chars = list(data)
        for x in chars:
            print(calculateBinary(getDeci(x)))

    main()

def getDeci(x):
    return ord(x)

def calculateBinary(x):
    bin_x = bin(x)
    return bin_x

if __name__ == '__main__':
    main()

# Need to add long string support
