
def count_digits(n):
    """Return the total number of digits in n"""
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count

def main():
    num = input("Enter a number: ")
    try:
        num = int(num)
        digits = count_digits(abs(num))  # Use abs to handle negative numbers
        print(f"The number {num} has {digits} digits.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

