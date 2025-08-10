from module5_mod import NumberCollection

def main():
    # Read N
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    collection = NumberCollection()

    # Read N numbers
    print(f"Enter {N} numbers:")
    for i in range(N):
        while True:
            try:
                num = int(input(f"Number {i + 1}: "))
                collection.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Read X
    while True:
        try:
            x = int(input("Enter number X to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Search and output result
    index = collection.search_number(x)
    print(index)


if __name__ == "__main__":
    main()
