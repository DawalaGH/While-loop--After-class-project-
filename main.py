def count_digits(n):
    """Return the total number of digits in n"""
    return len(str(abs(n)))

def main():
    num = input("Enter a number: ")
    try:
        num = int(num)
        digits = count_digits(num)
        print(f"The number {num} has {digits} digits.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
