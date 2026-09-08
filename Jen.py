
import sys

def main():
    print("--- Windows-Compatible Python Application ---")
    
    # Check for arguments or use defaults for automated pipeline verification
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        except ValueError:
            print("Error: Input arguments must be valid numbers.")
            sys.exit(1)
    else:
        print("No arguments detected. Running validation defaults.")
        num1 = 10.0
        num2 = 25.0

    print(f"First Number:  {num1}")
    print(f"Second Number: {num2}")
    print(f"Total Sum:     {num1 + num2}")
    print("Execution complete.")

if __name__ == "__main__":
    main()
